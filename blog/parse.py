import requests
from bs4 import BeautifulSoup as bs


def get_links():
    n = 1
    all_links = []
    for i in range(50):

        page = f"https://habr.com/ru/search/page{n}/?target_type=posts&order_by=date&q=python&flow="
        r = requests.get(page)
        # print(r.text)
        soup = bs(r.text, 'html.parser')
        links = soup.find_all('h2', class_="post__title")
        for a in links:
            href = a.find('a').get('href')
            print(href)
            all_links.append(href)

        n += 1

    all_links = set(all_links)
    return all_links


url = 'https://habr.com/ru/company/flipperdevices/blog/532028/'
r = requests.get(url)
# print(r.text)
soup = bs(r.text, 'html.parser')
content = soup.find('div', class_='post__body_full')
print(content)
