# -*- coding: utf-8 -*-
# 时间    : 2018/9/15 10:33
# 作者    : xcl

inputfile='C:\\Users\\Administrator\\Desktop\\principal_component.xls'
outputfile="C:\\Users\\Administrator\\Desktop\\outcome.xls"

import pandas as pd
data=pd.read_excel(inputfile,header=None)

from sklearn.decomposition import PCA
pca=PCA()
pca.fit(data)
#print(pca.components_)
print(pca.explained_variance_ratio_)

#a=pca.explained_variance_ratio_
#print(a.cumsum())

pca=PCA(3)
pca.fit(data)
low_d=pca.transform(data)
pd.DataFrame(low_d).to_excel(outputfile)
pca.inverse_transform(low_d)