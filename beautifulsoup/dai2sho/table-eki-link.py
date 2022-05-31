from bs4 import BeautifulSoup
html = open("eki-link.html", encoding = 'utf-8').read()
soup = BeautifulSoup(html, 'html.parser')

#テーブルを解析する
result = []

#<table>タグを得る
table = soup.select_one('table')

#<tr>タグを得る
tr_list = table.find_all('tr')
for a in tr_list:
    result_row = []
    td_list = a.find_all(['td'], ['th'])
    for td in td_list:
        cell = td.get_text()
        result_row.append(cell)
    result.append(result_row)

#リストをCSVファイルとして出力
for row in result:
    print(','.join(row))