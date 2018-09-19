#-*- coding: utf-8 -*-
# 基本信息统计
import pandas  as pd
catering_sale='C:\\Users\\Administrator\\Desktop\\data\\catering_sale.xls'
data=pd.read_excel(catering_sale,index_col='日期')
details=data.describe()
print(details)
print('')

# 异常值检测
import matplotlib.pyplot as plt #图像库
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False

plt.figure() #画图
p=data.boxplot(return_type='dict')#画箱线图，直接使用DataFrame的方法
x=p['fliers'][0].get_xdata()# 第一个异常点的数值
y=p['fliers'][0].get_ydata()# 'flies'即为异常值的标签
y.sort()#排序

#用annotate添加注释
#其中有些相近的点，注解会出现重叠，难以看清，需要一些技巧来控制。
#以下参数都是经过调试的，需要具体问题具体调试。
for i in range(len(x)): 
  if i>0:
    plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i]+0.05 -1.8/(y[i]-y[i-1]),y[i]))
  else:
    plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i]+0.08,y[i]))

plt.show() #展示箱线图


#一致性分析
