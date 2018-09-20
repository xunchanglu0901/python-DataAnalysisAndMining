# -*- coding: utf-8 -*-
# 时间    : 2018/9/20 14:22
# 作者    : xcl

#-*- coding: utf-8 -*-

# 作者    : xcl

# #使用K-Means算法聚类消费行为特征数据


import pandas as pd

#参数初始化
inputfile="C:\\Users\\Administrator\\Desktop\\consumption_data.xls"
outputfile="C:\\Users\\Administrator\\Desktop\\outcome.xls"
k = 3 #聚类的类别
iteration = 500 #聚类最大循环次数
data = pd.read_excel(inputfile, index_col = 'Id') #读取数据
data_zs = (data - data.mean())/data.std() #数据标准化

from sklearn.cluster import KMeans
model = KMeans(n_clusters = k, n_jobs = 1, max_iter = iteration) #分为k类，并发数4
model.fit(data_zs) #开始聚类
#print(model.labels_)

#简单打印结果
#r1 = pd.Series(model.labels_).value_counts() #统计各个类别的数目
#r2 = pd.DataFrame(model.cluster_centers_) #找出聚类中心
#r = pd.concat([r2, r1], axis = 1) #横向连接（0是纵向），得到聚类中心对应的类别下的数目
#r.columns = list(data.columns) + [u'类别数目'] #重命名表头
#print(r)

#详细输出原始数据及其类别
r = pd.concat([data, pd.Series(model.labels_, index = data.index)], axis = 1)  #详细输出每个样本对应的类别
r.columns = list(data.columns) + ['聚类类别'] #重命名表头
r.to_excel(outputfile) #保存结果


# 降维画图
from sklearn.manifold import TSNE

tsne = TSNE()
tsne.fit_transform(data_zs) #进行数据降维
tsne = pd.DataFrame(tsne.embedding_, index = data_zs.index) #转换数据格式
print(tsne)
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

#不同类别用不同颜色和样式绘图
d = tsne[r[u'聚类类别'] == 0]
plt.plot(d[0], d[1], 'r.')
d = tsne[r[u'聚类类别'] == 1]
plt.plot(d[0], d[1], 'go')
d = tsne[r[u'聚类类别'] == 2]
plt.plot(d[0], d[1], 'b*')
plt.show()
