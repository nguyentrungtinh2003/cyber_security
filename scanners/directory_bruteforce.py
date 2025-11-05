import requests

def directory_bruteforce(base_url):
    try:
        with open('payloads/directories.txt') as f:
            for directory in f:
                directory = directory.strip()
                url = f"https://{base_url}/{directory}"
                response = requests.get(url, timeout=2)
                if(response.status_code == 200):
                    print(f"Found directory: {url}")
    except requests.RequestException:
        pass
def main():
    base_url = input("Enter target URL (e.g., https://example.com): ")
    directory_bruteforce(base_url)

if __name__ == "__main__":
    main()