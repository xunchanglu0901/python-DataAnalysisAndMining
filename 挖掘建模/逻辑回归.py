# -*- coding: utf-8 -*-
# 时间    : 2018/9/15 13:38
# 作者    : xcl
import pandas as pd
filename = 'C:/Users/Administrator/Desktop/bankloan.xls'
data = pd.read_excel(filename)#返回值是DataFrame类型
x = data.iloc[:,:8].values#行全选，列选下标0-7
y = data.iloc[:,8].values#行全选，列选下标8

#使用稳定性选择方法中的随机逻辑回归进行特征筛选，利用筛选后的特征建立逻辑回归模型，输出平均正确率
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR
rlr = RLR(selection_threshold=0.25i) #建立随机逻辑回归模型，筛选变量
rlr.fit(x, y) #训练模型
#print(rlr.get_support()) #获取特征筛选结果，也可以通过.scores_方法获取各个特征的分数
#print(rlr.scores_)
#print('通过随机逻辑回归模型筛选特征结束')



print('有效特征:' , ','.join(data.columns[rlr.get_support(indices=True)]))
#print(data.columns[rlr.get_support(indices=True)])
#data.columns[rlr.get_support()]返回的是筛选后的列名,是一个迭代器
#S.join(iterable) 将iterable里面的元素用S连起来，S就是分隔符


x = data[data.columns[rlr.get_support(indices=True)]].values

lr = LR() #建立逻辑回归模型
lr.fit(x, y) #用筛选后的特征数据来训练模型
#print('逻辑回归模型训练结束')
#print('模型的平均正确率为:',lr.score(x, y))#给出模型的平均正确率，本例为81.4%

#a=lr.predict(x) #用指标数据X去预测Y 得到由训练模型预测出来的结果 即a

'''
#写入文件
import pandas as pd
outputfile="C:\\Users\\Administrator\\Desktop\\outcome.xls"
pd.DataFrame(a).to_excel(outputfile)
'''