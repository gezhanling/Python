# coding: utf-8

import requests 
from bs4 import BeautifulSoup 
import os
 
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}##���������ͷ���󲿷���վû���������ͷ�ᱨ������ؼ���Ŷ��
all_url = 'http://www.mzitu.com/all'  
start_html = requests.get(all_url,  headers=headers) 
Soup = BeautifulSoup(start_html.text, 'lxml')
all_a = Soup.find('div', class_='all').find_all('a') ##意思是先查找 class为 all 的div标签，然后查找所有的<a>标签。
for a in all_a:
    title = a.get_text() #取出a标签的文本
    href = a['href'] #取出a标签的href 属性
    
    html = requests.get(href, headers=headers) ##上面说过了
    html_Soup = BeautifulSoup(html.text, 'lxml') ##上面说过了
    
    max_span = html_Soup.find('div', class_='pagenavi').find_all('span')[-2].get_text() ##查找所有的<span>标签获取第十个的<span>标签中的文本也就是最后一个页面了。
    for page in range(1, int(max_span)+1): ##不知道为什么这么用的小哥儿去看看基础教程吧
        page_url = href + '/' + str(page) ##同上
        print(page_url) ##这个page_url就是每张图片的页面地址啦！但还不是实际地址！

    