from bs4 import BeautifulSoup
import urllib.request as req
import requests

url_login = 'https://twitter.com/login?lang=ja'

savename = 'twitter.txt'

USER = 's109shu2@icloud.com'
PASS = 'sharkle2020'

session = requests.session()

login_info = {
    'text': USER,
    'password': PASS
}

res = session.post(url_login, data = login_info)
#res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')

#ログイン後の処理
"""
with open(savename, mode = 'wb') as f:
    f.write(data)
    print('保存しました')
"""