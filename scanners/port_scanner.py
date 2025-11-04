import socket
import threading

open_ports = []


def scan_port(target,port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((target, port))
        try:
            banner = sock.recv(1024).decode().strip()
            print(f"Port {port} is open. Banner: {banner}")
            open_ports.append((port, banner))
        except:
            print(f"Port {port} is open. No banner retrieved.")
            open_ports.append((port, "No banner"))
    except:
        pass

def main():
    target = input("Enter IP address to scan : ")
    for port in range(1, 1025):
        thread = threading.Thread(target=scan_port, args=(target,port))
        thread.start()


if __name__ == "__main__":
    main()