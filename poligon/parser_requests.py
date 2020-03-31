import requests
from bs4 import BeautifulSoup

payload_to_login = {'openid_url':'korzh', 'password':'z_hug_ivsKX08Y'}
headers_to_login = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru,en-US;q=0.9,en;q=0.8,ru-RU;q=0.7,und;q=0.6,de;q=0.5',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '40',
    'Content-Type': 'application/x-www-form-urlencoded',

    'Origin': 'https://openid.sfedu.ru',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
}

# СМОТРИ В УРЛЫ И ПОСТАВЬ ТАМ ЛОГИН СВОЙ ВМЕСТО НАПОЛНИТЕЛЯ
login_url = r'https://openid.sfedu.ru/server.php/login'
url_from_brs_to_openid = r'https://grade.sfedu.ru/handler/sign/openidlogin?loginopenid=korzh@sfedu.ru&user_role=student'

headers_from_brs_to_openid = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru,en-US;q=0.9,en;q=0.8,ru-RU;q=0.7,und;q=0.6,de;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://grade.sfedu.ru',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}

with requests.Session() as s:

    responce_from_brs_to_login = s.get(url_from_brs_to_openid, headers=headers_from_brs_to_openid)
    headers_to_login['Referer'] = responce_from_brs_to_login.url
    login_responce = s.post(login_url, headers=headers_to_login, data=payload_to_login)

brs_table = {}
soup = BeautifulSoup(login_responce.content, 'html.parser')
disc_tag_list = soup.findAll('td', {'class': 'discTitle'})
score_tag_list = soup.findAll('td', {'class': 'discRating'})
score_line = "sep"

for i in range(1, len(score_tag_list)+1):
    key = 'SEP' + disc_tag_list[i].find('a').text

    spans = score_tag_list[i-1].findAll('span')
    for j in range(len(spans)):
        score_line += spans[j].text + 'sep'
    brs_table[key]= score_line
    score_line = ''

student_name = soup.find('div', {'class': 'username'}).text
print(''.join(brs_table.keys()))

