from urllib.parse import urljoin

base = 'http://example.com/html/a.html'

print(urljoin(base, 'b.html'))
print(urljoin(base, '../img/hoge.png'))
print(urljoin(base, '/hoge.html'))
print(urljoin(base, 'http://kujirahand.com/wiki'))

#<a>タグのhref属性に指定したパスをいい感じに絶対パスに変換してくれる