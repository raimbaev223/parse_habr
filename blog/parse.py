import requests
from bs4 import BeautifulSoup as bs
import sqlite3


class Data:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def save_data(self, link, title, post):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'blog_content' WHERE 'link' = ?", (link,)).fetchall()
            if not result:
                return self.cursor.execute(
                    f"INSERT INTO 'blog_content' "
                    f"('link', 'title', 'post') "
                    f"VALUES(?, ?, ?)",
                    (link, title, post)
                )


def get_links():
    n = 1
    all_links = []
    for i in range(2):

        page = f"https://habr.com/ru/search/page{n}/?target_type=posts&order_by=date&q=python&flow="
        r = requests.get(page)
        # print(r.text)
        soup = bs(r.text, 'html.parser')
        links = soup.find_all('h2', class_="post__title")
        for a in links:
            href = a.find('a').get('href')
            all_links.append(href)

        n += 1

    all_links = set(all_links)
    return all_links


def get_posts():
    db = Data('../db.sqlite3')
    links = get_links()
    for link in links:
        r = requests.get(link)
        soup = bs(r.text, 'html.parser')
        content = soup.find('div', class_='post__body_full')
        title = soup.find('span', class_='post__title-text')
        db.save_data(str(link), str(title), str(content))
        print(f"post {link} saved!")

get_posts()