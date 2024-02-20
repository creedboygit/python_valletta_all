import sqlite3
import time


# 블로그 목록 조회 함수
def get_blog_list():
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("select * from blog")
    result = c.fetchall()
    conn.close()

    return result


# get_blog_list()


# 신규 블로그 글 작성 함수
def add_blog(subject, content):  # 제목, 내용
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row

    c = conn.cursor()
    today = time.strftime('%Y%m%d')  # 현재 시간
    c.execute("insert into blog (subject, content, date) values (?, ?, ?)",
              (subject, content, today))
    conn.commit()
    conn.close()


# 블로그 읽기 함수
def read_blog(_id):
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("select * from blog where id = ?", (_id,))
    result = c.fetchone()
    conn.close()

    return result


# 블로그 수정 함수
def modify_blog(_id, subject, content):
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("update blog set subject = ?, content = ? where id = ?",
              (subject, content, _id))
    conn.commit()
    conn.close()


# 블로그 글 삭제 함수
def remove_blog(_id):
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("delete from blog where id = ?", (_id,))
    conn.commit()
    conn.close()
