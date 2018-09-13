# -*- coding: utf-8 -*-
# 时间    : 2018/9/13 16:03
# 作者    : xcl

# 通常加载代码
import matplotlib.pyplot as plt #导入作图库
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']
plt.figure(figsize=(7,5)) #指定比例
'''
#曲线星星图
import numpy as np
x=np.linspace(0,2*np.pi,10)
y=np.sin(x)
plt.plot(x,y,'bp--')
#plt.show()

#饼图
labels='A','B','C','D'
sizes=[1,3,5,9]
colors=['yellow','gold','red','lightcoral']
explode=(0,0.1,0,0)

plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.5f%%',
        shadow=True,startangle=90)
plt.axis('equal')
#plt.show()
'''
'''
#二维条形直方图
import numpy as np
x=np.random.randn(1000)
plt.hist(x,10)
plt.show()
'''
'''
# 箱图
import numpy as np
import pandas as pd
x=np.random.randn(1000)
d=pd.DataFrame([x,x+1])
print(d)
d.plot(kind='box')
plt.show()
'''
'''
# 对数图像
import numpy as np
import pandas as pd
plt.rcParams['font.sans-serif']
plt.rcParams['axes.unicode_minus']=False
x=pd.Series(np.exp(np.arange(20)))
x.plot(label='原',legend=False)
#plt.show()
x.plot(logy=True,label='处理后',legend=True)
plt.show()
'''
# 误差条形图
import numpy as np
import pandas as pd
plt.rcParams['font.sans-serif']
plt.rcParams['axes.unicode_minus']=False
error=np.random.randn(20)
y=pd.Series(np.sin(np.arange(20)))
y.plot(yerr=error,label='E',legend=True)
plt.show()