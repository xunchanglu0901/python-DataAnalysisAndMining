# -*- coding: utf-8 -*-
# 时间    : 2018/9/25 13:09
# 作者    : xcl

#使用K-Means算法聚类消费行为特征数据

import numpy as np
import pandas as pd

#参数初始化
inputfile = 'C:/Users/Administrator/Desktop/consumption_data.xls' #销量及其他属性数据
k = 3 #聚类的类别
threshold = 2 #离散点阈值
iteration = 500 #聚类最大循环次数
data = pd.read_excel(inputfile, index_col = 'Id') #读取数据
data_zs = 1.0*(data - data.mean())/data.std() #数据标准化

from sklearn.cluster import KMeans
model = KMeans(n_clusters = k, n_jobs =1, max_iter = iteration) #分为k类，并发数1
model.fit(data_zs) #开始聚类
#print(model.labels_)

#标准化数据及其类别
r = pd.concat([data_zs, pd.Series(model.labels_, index = data.index)], axis = 1)  #每个样本对应的类别
#print(r)
r.columns = list(data.columns) + ['聚类类别'] #重命名表头
outputfile="C:\\Users\\Administrator\\Desktop\\outcome.xls"
r.to_excel(outputfile) #保存结果
#print(r)
#print(model.cluster_centers_)

norm = []
for i in range(k): #逐一处理
  norm_tmp = r[['R', 'F', 'M']][r[u'聚类类别'] == i]-model.cluster_centers_[i]
  norm_tmp = norm_tmp.apply(np.linalg.norm, axis = 1) #求出绝对距离
  norm.append(norm_tmp/norm_tmp.median()) #求相对距离并添加

norm = pd.concat(norm) #合并
#print(norm)
#print(norm[norm])
#print(r["R"])

#保存文件
#normfile="C:\\Users\\Administrator\\Desktop\\outcome.xls"
#norm[norm].to_excel(normfile) #保存结果

#画图
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
norm[norm <= threshold].plot(style = 'go') #正常点

discrete_points = norm[norm > threshold] #离群点
discrete_points.plot(style = 'ro')

for i in range(len(discrete_points)): #离群点做标记
  id = discrete_points.index[i]
  n = discrete_points.iloc[i]
  plt.annotate('(%s, %0.4f)'%(id, n), xy = (id, n), xytext = (id, n))

plt.xlabel(u'编号')
plt.ylabel(u'相对距离')
plt.show()