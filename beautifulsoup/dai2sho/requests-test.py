import requests

'''
#getメソッドを送信
r = requests.get('http://google.com')
#postメソッドを送信
formdata = {"key1": "value1", "key2": "value2"}
r = requests.post('http://google.com', data = formdata)
'''

#データwp取得
r = requests.get('http://api.aoikujira.com/time/get.php')

#テキスト形式でデータを得る
text = r.text
print(text)

#バイナリ形式でデータを得る
bin = r.content
print(bin)