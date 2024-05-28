import requests
import sys

def get_content(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
    return response.text

def write_content(content, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"written to {file_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python web_sync.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    content = get_content(url)

    file_path = './URL'
    write_content(content, file_path)

if __name__ == "main":
    main()