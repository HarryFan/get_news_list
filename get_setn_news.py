import requests
from bs4 import BeautifulSoup
import csv

# 設定 header，模擬使用者使用瀏覽器訪問網頁
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

# 發送 request 請求，並使用 BeautifulSoup 解析網頁
url = "https://www.setn.com/"
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

# 找到新聞列表區塊
hot_list = soup.find("div", class_="top-hot-list")
li_list = hot_list.find_all("li")

# 儲存新聞資訊
news_list = []
for li in li_list:
    title = li.a.text.strip()
    link = "https://www.setn.com" + li.a["href"]
    news_list.append((title, link))

# 儲存新聞資訊到 csv 檔
with open("setn_news.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "link"])
    for news in news_list:
        writer.writerow(news)