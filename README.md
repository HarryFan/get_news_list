引言：
這份技術文件描述了一個Python程式，它可以從SETN網站上提取新聞資訊並將其保存到CSV檔案中。該程式使用 requests 和 BeautifulSoup 庫來發送 HTTP 請求並解析 HTML 內容。

程式概述：
該程式首先設置一個使用者代理頭來模擬瀏覽器請求。然後它向SETN網站發送一個HTTP GET請求，並檢索HTML內容。BeautifulSoup庫被用來解析HTML內容，並從頁面的頂部熱門列表部分提取新聞資訊。然後，該程式將新聞資訊保存到一個CSV檔案中。

程式細節：

導入必要的庫：
程式首先導入request、BeautifulSoup和csv庫。

設置使用者代理頭：
該程式設置一個使用者代理頭，以模擬瀏覽器請求。這樣做是為了防止網站阻斷請求。

發送一個HTTP GET請求：
程式向SETN網站發送一個HTTP GET請求，並檢索HTML內容。

解析HTML內容：
BeautifulSoup庫被用來解析HTML內容，並從頁面的熱門列表部分提取新聞資訊。

保存新聞資訊到CSV檔案：
該程式將新聞資訊保存到一個名為setn_news.csv的CSV檔案中。該CSV檔案包含兩欄：標題和連結。

總結：
這個Python程式演示了如何從一個網站中提取新聞資訊並保存到CSV檔案中。這個程式也可以修改為從其他網站提取訊息。