import requests
response = requests.get('https://2ip.ru')
ip = response.text.split('class="ip"')[1].split('<span>')[1].split('</span>')[0]
geo = response.text.split('href="/geoip/"/>')[1].split('</a')[0]
print(f"Ваш ip: {ip}, {geo}")
