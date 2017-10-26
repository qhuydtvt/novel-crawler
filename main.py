from bs4 import BeautifulSoup
from urllib.request import urlopen
from db import db_add_topic, db_add_word
import re

url = "http://600tuvungtoeic.com/"

def fetch_topics():
    html = urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')
    div_topics = soup.find_all('div', "gallery-item")

    contents = [
        {
            'title': div_topic.find('div', 'content-gallery').h3.string,
            'img': div_topic.img,
            'a': div_topic.find('div', 'overlay').a
        }
        for div_topic in div_topics
    ]

    topics = [
        {
            "name": content['title'].split('-')[1].strip(),
            "no": int(content['title'].split('-')[0].strip()),
            "url": url + "/" + content['a']['href'],
            'image_url': content['img']['src'],
        }
        for content in contents
    ]

    return topics

def fetch_words(topic):
    html = urlopen(topic['url']).read().decode("utf-8").replace('<hr>', '')
    soup = BeautifulSoup(html, 'html.parser')
    div_tuvungs = soup.find_all('div', 'tuvung')

    contents = [
        {
            'div': div_tuvung,
            'span_origin': div_tuvung.find('div', 'noidung').find_all('span')[0],
            'span_pronun': div_tuvung.find('div', 'noidung').find_all('span')[1],
            'example_translation': div_tuvung.find('div', 'noidung').find('b'),
            'image': div_tuvung.find('img'),
            'bundle': [str(content) for content in div_tuvung.find('div', 'noidung').contents if (content is not None) and str(content).strip() != ""]
        }
        for div_tuvung in div_tuvungs
    ]

    words = [
        {
            'origin': content['span_origin'].string,
            'explanation': content['bundle'][4],
            'pronunciation': content['span_pronun'].string,
            'type': content['bundle'][7],
            'image_url': content['image']['src'],
            'audio_url': url + BeautifulSoup(contents[0]['bundle'][-1], 'html.parser').find('source')['src'],
            'example': content['bundle'][10],
            'example_translation': content['example_translation'].string if content["example_translation"] is not None else ""
        }
        for content in contents
    ]

    return words

if __name__ == "__main__":
    topics = fetch_topics()
    with open('words.json', 'w') as f:
        for topic in topics:
            print("Adding topic", topic['name'])
            db_add_topic(topic)
            words = fetch_words(topic)
            for word in words:
                print('Adding word', word['origin'])
                word['topic'] = topic['name']
                word['topic_id'] = topic['id']
                db_add_word(word)


##novels = fetch_all_novel("http://www.truyenngan.com.vn/truyen-ngan.html")
##db_add_novel_list(novels)
#
# def save_a_novel(novel_info):
#     novel_url = novel_info["novel_url"]
#     chapter_url_prefix = novel_info["chapter_url_prefix"]
#     max_chapter = novel_info["max_chapter"]
#     start_chapter = novel_info["start_chapter"]
#
#     print("Fetching novel Info")
#     novel = fetch_novel(novel_url)
#     print("Done")
#     print("Adding novel info to database")
#     db_add_novel(novel)
#     print("Done")
#
#     for chapter_number in range(start_chapter, max_chapter):
#         print("Fetching chapter {0}".format(chapter_number))
#         chapter = fetch_chapter(chapter_url_prefix, chapter_number)
#         print("Done")
#         print("Adding chapter {0} to database".format(chapter_number))
#         chapter.novel_id = novel.id
#         db_add_chapter(chapter)
#         print("Done")
#
#
# novel_info_list = [
#     # {
#     #     "name": "Than khong thien ha",
#     #     "novel_url": "http://truyenfull.vn/truyen-than-khong-thien-ha/",
#     #     "chapter_url_prefix": "http://truyenfull.vn/truyen-than-khong-thien-ha",
#     #     "start_chapter": 1,
#     #     "max_chapter": 2763
#     # },
#     {
#         "name": "De ton",
#         "novel_url": "http://truyenfull.vn/de-ton/",
#         "chapter_url_prefix": "http://truyenfull.vn/de-ton",
#         "start_chapter": 1,
#         "max_chapter": 2922
#     }
# ]
#
# for novel_info in novel_info_list:
#     print("Fetching novel: {0}, chapters: {1}".format(novel_info["name"], novel_info["max_chapter"]))
#     save_a_novel(novel_info)
