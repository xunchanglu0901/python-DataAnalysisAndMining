# -*- coding: utf-8 -*-
# 时间    : 2018/9/15 9:24
# 作者    : xcl

inputfile='C:\\Users\\Administrator\\Desktop\\leleccum.mat'
from scipy.io import loadmat
mat=loadmat(inputfile)

signal=mat['leleccum'][0]


#分析
import pywt
coeffs= pywt.wavedec(signal,'bior3.7',level=5)


# 保存
import numpy as np
np.savetxt('C:\\Users\\Administrator\\Desktop\\coeffs.txt',coeffs[0], fmt='%s',delimiter=",")

import pandas as pd
outputfile="C:\\Users\\Administrator\\Desktop\\outcome.xls"
pd.DataFrame(coeffs[0]).to_excel(outputfile)
