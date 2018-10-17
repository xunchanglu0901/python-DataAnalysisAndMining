# -*- coding: utf-8 -*-
# 时间    : 2018/10/10 16:01
# 作者    : xcl
import numpy as np
import pandas as pd
#读取
data='C:\\Users\\Administrator\\Desktop\\2.xlsx'
outputfile="C:\\Users\\Administrator\\Desktop\\outcome.xls"
data=pd.read_excel(data)

#交叉表格
r=pd.pivot_table(data,values = '出口金额(美元)',index = ['贸易方式'],columns='最终目的国名称',aggfunc=np.mean)#取和、均值
print(r)

#保存
r.to_excel(outputfile)



'''
data=pd.read_excel(data,index_col='index')
details=data.describe()
print(details)
r=details
r.to_excel(outputfile)
'''

'''#存疑
data=pd.read_excel(data)
#print(data)
import collections
dic = collections.Counter(data)
for key in dic:
    print(key,dic[key])
'''