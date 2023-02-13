import requests
from bs4 import BeautifulSoup

def extract_all_links(site):
    html = requests.get(site).text
    soup = BeautifulSoup(html, "html.parser").find_all("a")
    links = [link.get("href") for link in soup]
    for link in links:
        print("=>",link," ")
    return ""

if __name__ == "__main__":
    try:
        site_link = input("Enter URL of the site : ")
        all_links = extract_all_links(site_link)
        print(all_links)
    except:
            print("Enter Valid URL!")
