# -*- coding: utf-8 -*-
# 时间    : 2018/9/19 16:14
# 作者    : xcl

import numpy as np
a=([2,5,4,3,8]) # 数据值;()可省略；即一列数据为2、5、4、3、8
print(np.var(a,ddof=1)) #进行方差计算；ddof=1即分母设定为n-1