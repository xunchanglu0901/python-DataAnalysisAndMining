# -*- coding: utf-8 -*-
# 时间    : 2018/9/13 13:56
# 作者    : xcl
# 餐饮数据相关性分析
import pandas as pd
catering_sale='C:\\Users\\Administrator\\Desktop\\catering_sale_all.xls'

data=pd.read_excel(catering_sale,index_col='日期')
a=data.corr()
b=data.corr()['百合酱蒸凤爪']
c=data['百合酱蒸凤爪'].corr(data['翡翠蒸香茜饺'])
print(a.unstack(),b,c)