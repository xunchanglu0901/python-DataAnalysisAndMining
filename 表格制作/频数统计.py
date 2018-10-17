# -*- coding: utf-8 -*-
# 时间    : 2018/10/10 22:48
# 作者    : xcl
import numpy as np
import pandas as pd
#读取
data='C:\\Users\\Administrator\\Desktop\\data.xlsx'
outputfile="C:\\Users\\Administrator\\Desktop\\outcome.xlsx"
data=pd.read_excel(data)

#print(data)
#print(data['贸易方式'])

#转换成list列表
'''
a=data['贸易方式'].tolist()
#print(a)
'''

#频数统计
'''
from collections import Counter
out= Counter(a)
print(out)
'''

#排序并保存
'''
data2=data.sort_values(by='贸易方式')
data2.to_excel(outputfile)


'''