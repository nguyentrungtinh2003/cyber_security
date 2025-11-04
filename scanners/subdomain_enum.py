import requests

def sub_domain(domain, subdomains):
    try:
        for sub in subdomains:
            url = f"https://{sub}.{domain}"
            response = requests.get(url, timeout=1)
            if response.status_code == 200:
                print(f"Found subdomain: {url}")
    except requests.RequestException:
        pass

def main():
    domain = input("Enter target domain: ")
    subdomains = ['www', 'mail', 'ftp', 'test', 'dev', 'admin', 'blog', 'shop', 'api', 'staging']
    sub_domain(domain, subdomains)

if __name__ == "__main__":
    main()