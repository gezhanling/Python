# coding: utf-8

import requests 
from bs4 import BeautifulSoup 
import numpy as np
import re
import os
import pandas as pd
from astropy.io.ascii.tests.test_fixedwidth import table

url = "http://rl.fx678.com/country.html" 
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}##���������ͷ���󲿷���վû���������ͷ�ᱨ������ؼ���Ŷ��
 
r = requests.get(url,  headers=headers) 
html = r.text.encode(r.encoding).decode()
soup = BeautifulSoup(html, 'lxml')
table = soup.find('table', class_ = 'cjsj_tab3')
#查看行数
height = len(table.findAll(lambda tag:tag.name =='tr' and
                           len(tag.findAll('td'))>=1))
#print(height)
#查看列数
for row in table.findAll('tr'):
    print(len(row.findAll('td')),end = '\t') 
#收集表头
columns = [x.text for x in table.tr.findAll('th')]
columns = [x.replace('\xa0',' ') for x in columns]
print(columns)
#构造dataframe 存储表格
width = len(columns)
df = pd.DataFrame(data = np.full((height, width),' ',dtype = 'U'), columns = columns)
rows = [row for row in table.findAll('tr') if row.find('td')!=None]
#逐行填入数据
for i in range(len(rows)):
    cells = rows[i].findAll('td')
    #若该行单元格数量与dataframe列数一样
    if len(cells) == width:
        df.iloc[i] =[cell.text.replace(' ','').replace('/n','') for cell in cells]

print(df)
