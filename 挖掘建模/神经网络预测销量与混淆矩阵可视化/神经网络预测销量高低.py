# -*- coding: utf-8 -*-
# 时间    : 2018/9/19 9:06
# 作者    : xcl
import pandas as pd
filename = 'C:/Users/Administrator/Desktop/sales_data.xls'

data=pd.read_excel(filename, index_col='序号')
data[data=='好']=1
data[data=='高']=1
data[data=='是']=1
data[data != 1]= 0
x=data.iloc[:,:3].values.astype(int)
y=data.iloc[:,3].values.astype(int)

# 模型
from keras.models import Sequential
from keras.layers.core import Dense,Activation

model=Sequential() #建模
model.add(Dense(input_dim=3,units= 10))
model.add(Activation('relu'))
model.add(Dense(input_dim=10,units = 1))
model.add(Activation('sigmoid'))

model.compile(loss="binary_crossentropy",optimizer='adam',metrics=['accuracy'])

model.fit(x,y,epochs=20,batch_size=10)
yp=model.predict_classes(x).reshape(len(y))

from cm_plot import *
cm_plot(y,yp).show()