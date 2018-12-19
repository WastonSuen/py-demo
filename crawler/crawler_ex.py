# coding=utf-8
"""
@version: 2017/11/21 021
@author: Suen
@contact: sunzh95@hotmail.com
@file: crawler_ex
@time: 14:06
@note:  ??
"""
import requests
import bs4

resp = requests.get(url='')
soup = bs4.BeautifulSoup(resp.content, 'html.parser')
with open('npm.txt', str('wb')) as f:
    for tag in soup.find_all('div', attrs={'class': 'lists'}):
        title = tag.find('a', attrs={'title': True}).attrs.get('title')
        content = tag.find('p', attrs={'class': 'description'}).text
        time = tag.find('span', {'class': 'col-xs-6'}).text
        print(title, content, time)
        context = '\n'.join([title, time, content])
        f.write(context)
        f.write('\n')
