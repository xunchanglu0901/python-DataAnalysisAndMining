# -*- coding: utf-8 -*-
# 时间    : 2018/9/13 14:50
# 作者    : xcl



#基本信息 相关系数
'''
import pandas as pd
D=pd.DataFrame([range(1,8),range(2,9)])
D.corr(method='kendall')
s1=D.loc[1]
s2=D.loc[0]
s1.corr(s2)
print(s1.corr(s2)'''
'''
import pandas as pd
import numpy as np

d=pd.DataFrame(np.random.randn(6,5))

d.cov()
print(d.cov())
print(d.skew(),d.kurt())

print(d.describe())
'''

# 拓展函数统计特征
import pandas as pd
import numpy as np

d=pd.Series(range(0,20))
d.cumsum()
#print(d.cumsum())
print(d.rolling(2).mean())