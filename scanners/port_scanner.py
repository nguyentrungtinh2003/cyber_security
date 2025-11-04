import socket
import threading


def scan_port(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((target, port))
        try:
            banner = sock.recv(1024).decode().strip()
            print(f"Port {port} is open. Banner: {banner}")
        except:
            print(f"Port {port} is open. No banner retrieved.")
            sock.close()

    except:
        pass

def main():
    target = input("Enter target IP address or hostname : ")
    try:
        for port in range(1,1025):
            thread = threading.Thread(target=scan_port, args=(target, port))
            thread.start()
    except KeyboardInterrupt:
        print("\nExiting program.")


if __name__ == "__main__":
    main()