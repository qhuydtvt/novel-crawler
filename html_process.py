import urllib.request
from bs4 import BeautifulSoup

def get_html(novel_url, chapter):
    with urllib.request.urlopen("{0}/chuong-{1}/".format(novel_url, chapter)) as response:
        html_doc = response.read()
        return html_doc


def get_soup(html_doc):
    return BeautifulSoup(html_doc, "html.parser")


def get_chapter_title(b_soup):
    return b_soup.find('a', 'chapter-title')["title"]


def get_content(b_soup):
    return b_soup.find('div', 'chapter-c')


# def db_save_novel(novel_id):

# def db_save_chapter(novel_id, title, content, chapter):


# html = get_html("http://truyenfull.vn/pham-nhan-tu-tien", 333)
# soup = get_soup(html)
# title = get_chapter_title(soup)
# content = get_content(soup)
# print(title)
# print(content)