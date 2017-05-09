from html_processor import *
from db import *

novels = fetch_all_novel("http://www.truyenngan.com.vn/truyen-ngan.html")
db_add_novel_list(novels)
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
