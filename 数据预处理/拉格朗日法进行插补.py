# -*- coding: utf-8 -*-
# 时间    : 2018/9/13 21:32
# 作者    : xcl

import pandas as pd
from scipy.interpolate import lagrange
inputfile='C:\\Users\\Administrator\\Desktop\\catering_sale.xls'
outputfile='C:\\Users\\Administrator\\Desktop\\sales.xls'

data = pd.read_excel(inputfile)  # 读入数据
# data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None #过滤异常值，将其变为空值
row_indexs = (data[u'销量'] < 400) | (data[u'销量'] > 5000)  # 得到过滤数据的索引
data.loc[row_indexs, u'销量'] = None  # 过滤数据

# 自定义列向量插值函数
# s为列向量，n为被插值的位置，k为取前后的数据个数，默认为5
def ployinterp_column(s, n, k=5):
    y = s[list(range(n - k, n)) + list(range(n + 1, n + 1 + k))]  # 取数
    y = y[y.notnull()]  # 剔除空值
    return lagrange(y.index, list(y))(n)  # 插值并返回拉格朗日插值结果
# 逐个元素判断是否需要插值
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:  # 如果为空即插值。
            #       data[i][j] = ployinterp_column(data[i], j)
            data.loc[j, i] = ployinterp_column(data[i], j)
data.to_excel(outputfile)  # 输出结果，写入文件 即文件sales.xls
