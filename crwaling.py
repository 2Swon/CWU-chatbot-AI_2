from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse
import re

def extract_all_links(url, base_url, visited_urls):
    links = set()
    try:
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')

        for link in soup.find_all('a', href=True):
            href = link.get('href')
            full_url = urllib.parse.urljoin(base_url, href)

            if full_url.startswith(base_url) and full_url not in visited_urls:
                links.add(full_url)
                visited_urls.add(full_url)
                print(full_url)
                links.update(extract_all_links(full_url, base_url, visited_urls))

    except Exception:
        pass

    return links


def get_all_links(base_url):
    visited_urls = set()
    links = extract_all_links(base_url, 'https://home.chungwoon.ac.kr/', visited_urls)
    return links


base_url = "https://home.chungwoon.ac.kr/home/index.do"
get_all_links(base_url)
