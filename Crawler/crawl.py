from urllib.parse import urlsplit, urljoin
from bs4 import BeautifulSoup
import requests

def normalize_url(url):
    url = urlsplit(url)
    return url.netloc + url.path

def get_heading_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    if soup.find('h1') is not None:
        return soup.find('h1').get_text()
    elif soup.find('h2') is not None:
        return soup.find('h2').get_text()
    else:
        return ""

def get_first_paragraph_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    if soup.main is not None:
        if soup.main.p is not None:
            return soup.main.p.get_text()
    if soup.p == None:
        return ""
    return soup.p.get_text()

def get_urls_from_html(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    lista = list()
    for link in soup.find_all('a'):
        lista.append(urljoin(base_url, link.get('href')))
    return lista

def get_images_from_html(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    lista = list()
    for link in soup.find_all('img'):
        if link.get('src') is not None:
            lista.append(urljoin(base_url, link.get('src')))
    return lista

def extract_page_data(html, page_url):
    dicta = dict() #example dicta["age"] = 31
    dicta["url"] = page_url
    dicta["heading"] = get_heading_from_html(html)
    dicta["first_paragraph"] = get_first_paragraph_from_html(html)
    dicta["outgoing_links"] = get_urls_from_html(html, page_url)
    dicta["image_urls"] = get_images_from_html(html, page_url)
    return dicta

def get_html(url):
    r = requests.get(url, headers={"User-Agent": "BootCrawler/1.0"})
    if r.status_code >= 400:
        raise Exception(f"Error with url: {url}")
    if "text/html" not in r.headers.get("Content-Type", ""):
        raise Exception(f"found no text/html on: {url}")
    return r.text

def crawl_page(base_url, current_url=None, page_data=None):
    if page_data is None: page_data = {}
    if current_url is None: current_url = base_url
    url1, url2 = urlsplit(base_url), urlsplit(current_url)
    if url1.netloc != url2.netloc:
        return
    normalized_url = normalize_url(current_url)
    if normalized_url in page_data:
        return
    print(current_url)
    page_data[normalized_url] = None
    try:
        html = get_html(current_url)
    except Exception:
        return
    page_data[normalized_url] = extract_page_data(html, current_url)
    loop = get_urls_from_html(html, base_url)
    for url in loop:
        crawl_page(base_url, url, page_data)
    return page_data