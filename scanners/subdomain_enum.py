import requests

def sub_domain(domain):
    try:
        with open('payloads/subdomains.txt') as f:
            for sub in f:
                sub = sub.strip()
                url = f"https://{sub}.{domain}"
                response = requests.get(url, timeout=1)
                if response.status_code == 200:
                    print(f"Found subdomain: {url}")
    except requests.RequestException:
        pass

def main():
    domain = input("Enter target domain: ")
    sub_domain(domain)

if __name__ == "__main__":
    main()