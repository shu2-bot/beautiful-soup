from bs4 import BeautifulSoup
import urllib.request as req

url = "https://login.shinshu-u.ac.jp/cgi-bin/Login.cgi"
savename = 'acsu-login.txt'

res = req.urlopen(url)
data = res.read()

with open(savename, mode = "wb") as f:
    f.write(data)
    print('保存しました')
