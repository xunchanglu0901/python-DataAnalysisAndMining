# -*- coding: utf-8 -*-
# 时间    : 2018/9/14 9:12
# 作者    : xcl

import pandas as pd
import numpy as np

datafile='C:\\Users\\Administrator\\Desktop\\normalization_data.xls'
data=pd.read_excel(datafile,header=None)
print(data)
a=(data-data.min())/(data.max()-data.min())
b=(data-data.mean())/data.std()
c=data/10**np.ceil(np.log(
    data.abs().max()))
#print(a,b,c,sep='\n'*3)