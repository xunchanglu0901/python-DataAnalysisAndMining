# -*- coding: utf-8 -*-
# 时间    : 2018/9/15 9:03
# 作者    : xcl

# 线损率
import pandas as pd
inputfile='C:\\Users\\Administrator\\Desktop\\electricity_data.xls'
outputfile="C:\\Users\\Administrator\\Desktop\\electricity_outcome_data.xls"
data=pd.read_excel(inputfile) #读取
data['线损率']=(data['供入电量']-data['供出电量'])/data['供入电量']

data.to_excel(outputfile,index=False)