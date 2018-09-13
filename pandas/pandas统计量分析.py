from __future__ import print_function
import pandas as pd
catering_sale='C:\\Users\\Administrator\\Desktop\\catering_sale.xls'

data=pd.read_excel(catering_sale,index_col='日期')
data=data[(data['销量']>400)&(data['销量']<5000)] #异常值的初步过滤
statistics=data.describe()
print(statistics)
print(' ')
statistics.loc['range']=statistics.loc['max']-statistics.loc['min']
statistics.loc['var']=statistics.loc['std']/statistics.loc['mean']
statistics.loc['dis']=statistics.loc['75%']-statistics.loc['25%']
print(statistics)
