import urllib.request
from bs4 import BeautifulSoup
from models.novel import Novel
from models.chapter import Chapter
import re

def no_accent_vietnamese(s):
    s = re.sub(u'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub(u'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    s = re.sub(u'èéẹẻẽêềếệểễ', 'e', s)
    s = re.sub(u'ÈÉẸẺẼÊỀẾỆỂỄ', 'E', s)
    s = re.sub(u'òóọỏõôồốộổỗơờớợởỡ', 'o', s)
    s = re.sub(u'ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ', 'O', s)
    s = re.sub(u'ìíịỉĩ', 'i', s)
    s = re.sub(u'ÌÍỊỈĨ', 'I', s)
    s = re.sub(u'ùúụủũưừứựửữ', 'u', s)
    s = re.sub(u'ƯỪỨỰỬỮÙÚỤỦŨ', 'U', s)
    s = re.sub(u'ỳýỵỷỹ', 'y', s)
    s = re.sub(u'ỲÝỴỶỸ', 'Y', s)
    s = re.sub(u'Đ', 'D', s)
    s = re.sub(u'đ', 'd', s)
    s = re.sub(u'ở', 'o', s)
    s = re.sub(u'ô', 'o', s)
    s = re.sub(u'ỏ', 'o', s)
    s = re.sub(u'ò', 'o', s)
    s = re.sub(u'Ô', 'O', s)
    s = re.sub(u'í', 'i', s)
    s = re.sub(u'Í', 'I', s)
    s = re.sub(u'ờớợở', 'o', s)
    s = re.sub(u'ỜỚỢỞ', 'O', s)
    s = re.sub(u'ùúụủ', 'u', s)
    s = re.sub(u'ÙÚỤỦ', 'O', s)
    s = re.sub(u'òóọỏ', 'o', s)
    s = re.sub(u'ÒÓỌỎ', 'O', s)
    s = re.sub(u'ữ', 'u', s)
    s = re.sub(u'ư', 'u', s)
    s = re.sub(u'ự', 'u', s)
    s = re.sub(u'ừ', 'u', s)
    s = re.sub(u'Ư', 'U', s)
    s = re.sub(u'ớ', 'o', s)
    s = re.sub(u'ộ', 'o', s)
    s = re.sub(u'ố', 'o', s)
    s = re.sub(u'ủ', 'u', s)
    s = re.sub(u'ế', 'e', s)
    s = re.sub(u'ũ', 'u', s)
    s = re.sub(u'ờ', 'o', s)
    s = re.sub(u'ề', 'e', s)
    s = re.sub(u'ó', 'o', s)
    s = re.sub(u'ể', 'e', s)
    s = re.sub(u'ệ', 'e', s)
    s = re.sub(u'ồ', 'o', s)
    s = re.sub(u'ơ', 'o', s)
    s = re.sub(u'ọ', 'o', s)
    s = re.sub(u'ê', 'e', s)
    s = re.sub(u'ù', 'u', s)
    s = re.sub(u'ụ', 'u', s)
    s = re.sub(u'ì', 'i', s)

    return s

def get_soup(html_doc):
    return BeautifulSoup(html_doc, "html.parser")


def get_html(url):
    with urllib.request.urlopen(url) as response:
        html_doc = response.read()
        return html_doc

# Novel

def get_novel_html(novel_url):
    return get_html(novel_url)


def get_novel_title(b_soup):
    return b_soup.find("h3", "title").string


def get_novel_description(b_soup):
    return str(b_soup.find("div", "desc-text desc-text-full"))

def get_novel_author(b_soup):
    return b_soup.find("a", itemprop="author")["title"]

def get_novel_picture(b_soup):
    return b_soup.find("div", "book").img["src"]

def get_novel_genre(b_soup):
    div_info = b_soup.find("div", "info")
    genres = [el["title"] for el in div_info.find_all("a", itemprop="genre")]
    ret = ""
    for i in range(len(genres)):
        ret += genres[i]
        if i < len(genres) - 1:
            ret += ", "
    return ret

def fetch_all_novel(novel_list_url):
    soup = get_soup(get_html(novel_list_url))
    novels = []
    all_story_group = soup.find_all("div", "wrap-carousel-cate")
    for story_group_bsoup in all_story_group:
        story_bsoups = story_group_bsoup.find("ul").find_all("li")
        story_bsoup = story_bsoups[0]
        detail_link = "http://www.truyenngan.com.vn/" + story_bsoup.find("div", "carousel-cate-img").a["href"]
        detail = get_soup(get_html(detail_link))
        image = story_bsoup.find("div", "carousel-cate-img").a.img["src"]
        title = story_bsoup.find("div", "carousel-cate-title").a.get_text()
        description = detail.find("strong").get_text()
        novel = Novel(title, "", description, image, "Truyện ngắn")
        novel.chapters = []
        novels.append(novel)

        no = 1
        for story_bsoup in story_bsoups:
            detail_link = "http://www.truyenngan.com.vn/" + story_bsoup.find("div", "carousel-cate-img").a["href"]
            title = story_bsoup.find("div", "carousel-cate-title").a.get_text()
            detail = get_soup(get_html(detail_link))
            author = detail.find("div", "details-poster").a.strong.get_text()
            content = str(detail.find("div", "maincontent"))
            chapter = Chapter(no, title + " - " + author, content)
            novel.chapters.append(chapter)
            no += 1

    return novels

def truyen8_mobi_fetch_novel(bsoup):
    ps = [p.get_text() for p in bsoup.find_all("p", "magb5 dot")]

    title = bsoup.h3.a.get_text()
    image = bsoup.a.img["src"]
    author = (ps[1]).replace("Tác giả:", "").strip()
    description = bsoup.find("p", "descrip").get_text().strip()
    genre = "Short story"

    detail_link = None

    search_string = no_accent_vietnamese(title)\
        .replace("-", "")\
        .replace(" ", "-")\
        .replace(",","")\
        .replace("!", "")\
        .lower()

    #
    search_html = get_html("http://webtruyen.com/searching/{0}/".format(search_string))
    search_bsoup = get_soup(search_html)
    list_story = search_bsoup.find("div", "list-story")
    if list_story is not None:
        content = list_story.find("div", "w3-row list-content")
        detail_link = content.find("div").a["href"]
    else:
        print("Not found: ", search_string)

    novel = Novel(title=title, author=author, description=description, genre=genre, image=image)
    novel.detail_link = detail_link
    return novel

def fetch_novel(novel_url):
    novel_bsoup = get_soup(get_novel_html(novel_url))
    novel_title = get_novel_title(novel_bsoup)
    novel_author = get_novel_author(novel_bsoup)
    novel_description = get_novel_description(novel_bsoup)
    novel_genre = get_novel_genre(novel_bsoup)
    novel_image = get_novel_picture(novel_bsoup)
    novel = Novel(title=novel_title, author=novel_author, description=novel_description, image=novel_image, genre=novel_genre)

    return novel


def get_chapter_list(novel_detail_url):
    novel_detail_bsoup = get_soup(get_html(novel_detail_url))
    chapter_table_bsoup = novel_detail_bsoup.find("table")
    trs = chapter_table_bsoup.tbody.find_all("tr")
    trs.pop(0)
    for tr in trs:
        tds = tr.find_all("td")
        if len(tds) >= 2:
            link = "http://truyen8.mobi" + tr.find_all("td")[1].a["href"]
            title = tr.find_all("td")[1].a.get_text()


def get_chapter_html(chapter_prefix, chapter):
    with urllib.request.urlopen("{0}/chuong-{1}/".format(chapter_prefix, chapter)) as response:
        html_doc = response.read()
        return html_doc

def get_chapter_title(b_soup):
    title_el = b_soup.find('a', 'chapter-title')
    if title_el is not None:
        return title_el["title"]
    else:
        return ""

def get_chapter_content(b_soup):
    content = b_soup.find('div', 'chapter-c')
    if content is not None:
        return content.get_text()
    else:
        return ""


def fetch_chapter(chapter_prefix, chapter):
    chapter_bsoup = get_soup(get_chapter_html(chapter_prefix, chapter))
    chapter_title = get_chapter_title(chapter_bsoup)
    chapter_content = get_chapter_content(chapter_bsoup)
    return Chapter(no=chapter, title=chapter_title, content=chapter_content)


# novels = fetch_all_novel("http://www.truyenngan.com.vn/truyen-ngan.html")
# for novel in novels:
#     # novel.print()
#     for chapter in novel.chapters:
#         chapter.print()
#     # print("--------------------------------------------------------")
# chapter = fetch_chapter("http://truyenfull.vn/truyen-than-khong-thien-ha", 1)
# chapter.print()

# def db_save_novel(novel_id):

# def db_save_chapter(novel_id, title, content, chapter):

# html = get_html("http://truyenfull.vn/pham-nhan-tu-tien", 333)
# soup = get_soup(html)
# title = get_chapter_title(soup)
# content = get_content(soup)
# print(title)
# print(content)

# html = get_novel_html("http://truyenfull.vn/truyen-than-khong-thien-ha/")
# soup = get_soup(html)
# print(get_novel_genre(soup))