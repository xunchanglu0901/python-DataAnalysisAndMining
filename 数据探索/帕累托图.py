#-*- coding: utf-8 -*-
#菜品盈利数据 帕累托图
from __future__ import print_function
import pandas as pd
dish_profit='C:\\Users\\Administrator\\Desktop\\catering_dish_profit.xls'

data=pd.read_excel(dish_profit,index_col='菜品名')
data=data['盈利'].copy()
data.sort_values(ascending = False)

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
#直方图部分
plt.figure()
data.plot(kind='bar')
plt.ylabel('profit(￥)')
# 贡献率部分
p=data.cumsum()/data.sum()
p.plot(color='b',secondary_y=True,style='-o',linewidth=1)

plt.annotate(format(p[6],'.4%'),xy=(6,p[6]),xytext=(6*0.9,p[6]*0.9),arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
plt.ylabel('盈利(比例)')
plt.show()
