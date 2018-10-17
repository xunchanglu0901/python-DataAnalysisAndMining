# -*- coding: utf-8 -*-
# 时间    : 2018/10/11 12:59
# 作者    : xcl

import numpy as np
import pandas as pd
#读取
data='C:\\Users\\Administrator\\Desktop\\data_yi.xlsx'
outputfile="C:\\Users\\Administrator\\Desktop\\outcome.xlsx"
data=pd.read_excel(data)




r=pd.pivot_table(data,index=["贸易方式","商品名称",'最终目的国名称',"企业中文名称"])
r.to_excel(outputfile)

'''
#print(data)
#print(data['贸易方式'])

#转换成list列表

a=data['贸易方式'].tolist()
#print(a)


#频数统计

from collections import Counter
out= Counter(a)
print(out)

'''
for items in data['贸易方式']:
    if items == '一般贸易':
        print(items)
'''

        
'''