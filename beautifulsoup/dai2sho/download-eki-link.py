from urllib import parse, request
from bs4 import BeautifulSoup
import os
import os.path
import time

#リンクを抽出する
html = open("eki-link.html", encoding='utf-8').read()
soup = BeautifulSoup(html, 'html.parser')
links = soup.select('a[href]')
result = []
for a in links:
    href = a.attrs['href']
    title = a.attrs['title']
    result.append((title, href))

#リンク先をダウンロードする
savepath = "./out"
if not os.path.exists(savepath):
    os.mkdir(savepath)
for title, url in result:
    path = savepath + '/' + url + '.html'
    #相対URLを絶対URLに変換
    a_url = parse.urljoin('http://example.com', url)
    print('download=' + a_url)
    #ダウンロード
    request.urlretrieve(a_url, path)
    time.sleep(1)