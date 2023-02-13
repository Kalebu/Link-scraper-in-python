import requests
from bs4 import BeautifulSoup


def extract_all_links(site):
    html = requests.get(site).text
    soup = BeautifulSoup(html, "html.parser").find_all("a")
    links = [link.get("href") for link in soup]
    for link in links:
        print("=>",link," ")
    return ""


def on_site_extraction_error(site_link):
    print(f"Error: Could not extract links from {site_link}.")


if __name__ == "__main__":
    site_link = input("Enter URL of the site : ")
    try:
        all_links = extract_all_links(site_link)
        print(all_links)
    except Exception as e:
        on_site_extraction_error(site_link)
