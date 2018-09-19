# -*- coding: utf-8 -*-
# 时间    : 2018/9/18 22:34
# 作者    : xcl

import pandas as pd
filename = 'C:/Users/Administrator/Desktop/sales_data.xls'

data=pd.read_excel(filename, index_col='序号')
data[data=='好']=1
data[data=='高']=1
data[data=='是']=1
data[data != 1]= -1

x=data.iloc[:,:3].values.astype(int)
y=data.iloc[:,3].values.astype(int)
from sklearn.tree import DecisionTreeClassifier as DTC
dtc= DTC(criterion='entropy')

dtc.fit(x,y)

#可视化
#from sklearn.tree import export_graphviz
#from sklearn.externals.six import StringIO
#with open("Dtree.dot","w") as f:
#    f = export_graphviz(dtc, out_file=f)
print(dtc.predict(x))
