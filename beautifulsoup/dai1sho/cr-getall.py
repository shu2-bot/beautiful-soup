#pythonのマニュアルを再帰的にダウンロード
#モジュールの取り込み
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as parse
from os import makedirs
import os.path
import time
import re

#処理済み判断変換
proc_files = {}

#HTML内にあるリンクを抽出する関数
def enum_links(html, base):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select("link[rel='stylesheet']") #CSS
    links += soup.select("a[href]") #リンク
    result = []
    #href属性を取り出し、リンクを絶対パスに変換
    for a in links:
        href = a.attrs['href']
        url = parse.urljoin(base, href)
        result.append(url)
    return result

#ファイルをダウンロードし保存する関数
def download_file(url):
    o = parse.urlparse(url)
    savepath = "./" + o.netloc + o.path
    if re.search(r"/$",savepath):
        savepath += "index.html"
    savedir = os.path.dirname(savepath)
    #既にダウンロード済み？
    if os.path.exists(savepath): return savepath
    #ダウンロード先のディレクトリを作成
    if not os.path.exists(savedir):
        print("mkdir=", savedir)
        makedirs(savedir)
    #ファイルをダウンロード
    try:
        print('download=', url)
        req.urlretrieve(url, savepath)
        time.sleep(1)
        return savepath
    except:
        print('ダウンロード失敗 :', url)
        return None

#HTMLを解析してダウンロードする関数
def analize_html(url, root_url):
    savepath = download_file(url)
    if savepath is None: return
    if savepath in proc_files: return #解析済みなら処理しない
    proc_files[savepath] = True
    print('analize_html=', url)
    #リンクを抽出
    html = open(savepath, "r", encoding = 'utf-8').read()
    links = enum_links(html, url)
    for link_url in links:
        #リンクがルート以外のパスを指していたら無視
        if link_url.find(root_url) != 0:
            if not re.search(r'.css$', link_url): continue
        #HTMLか？
        if re.search(r".(html|htm)$", link_url):
            #再帰的にHTMLファイルを解析
            analize_html(link_url, root_url)
            continue
        #それ以外のファイル
        download_file(link_url)

if __name__ == "__main__":
    #URLを丸ごとダウンロード
    url = "http://docs.python.jp/3.5/library/"
    analize_html(url, url)
        