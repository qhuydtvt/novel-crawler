import sqlite3
from models.novel import Novel
from models.chapter import Chapter

conn = sqlite3.connect("novel.db")


def db_read_all_novel():
    cursor = conn.cursor()
    for row in cursor.execute("SELECT * FROM tbl_novel"):
        print(row)
        print("-------------------------------------------")
        novel = Novel.from_row(row)
        db_read_all_chapter(novel)
        print("-------------------------------------------")
    cursor.close()


def db_add_novel(novel):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tbl_novel (title, description, author, genre) VALUES (?,?,?,?)",
                   novel.get_insert_params())
    conn.commit()
    novel.id = cursor.lastrowid
    cursor.close()


def db_add_chapter(chapter):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tbl_chapter (novel_id, title, page_number, content) VALUES (?,?,?,?)",
                   chapter.get_insert_params())
    conn.commit()


def db_read_all_chapter(novel):
    cursor = conn.cursor()
    for row in cursor.execute("SELECT * FROM tbl_chapter WHERE novel_id=?", [novel.id]):
        print(row)

# db_read_all_novel()

n = Novel(title="Abc", description="def", author="xxx", genre="xxx")
db_add_novel(n)
db_read_all_novel()

c = Chapter(n.id, "Chuong 1", 1, "xxx")
db_add_chapter(c)


c = Chapter(n.id, "Chuong 2", 2, "yyy")
db_add_chapter(c)

#
# db_read_all_chapter(n)

db_read_all_novel()
