from urllib.parse import urlsplit, urljoin
from bs4 import BeautifulSoup

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