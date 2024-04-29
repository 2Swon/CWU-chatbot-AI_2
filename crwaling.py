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

            # 해당 도메인으로 시작하는지 확인
            if full_url.startswith(base_url) and full_url not in visited_urls:
                links.add(full_url)
                visited_urls.add(full_url)
                print(full_url)
                links.update(extract_all_links(full_url, base_url, visited_urls))

    except Exception:
        # 오류 발생 시 무시하고 진행
        pass

    return links


def get_all_links(base_url):
    visited_urls = set()
    links = extract_all_links(base_url, 'https://home.chungwoon.ac.kr/', visited_urls)
    return links


base_url = "https://home.chungwoon.ac.kr/home/index.do"
get_all_links(base_url)
