# -*- coding=utf-8 -*-
import pandas
import seaborn
import matplotlib.pyplot as plt #pycharm上显示图像的方法
from scipy import stats
testdata = pandas.read_csv("C2_MAIN_PCBA_P2M0CI23.csv");
#print(testdata.head(1));
#print(iris.tail());
#print(iris.sample(10));
#print(testdata.describe());

#%matplotlib inline #jupter上显示图像
#seaborn.countplot("Species", data=iris);    #条形图
#seaborn.barplot(x='测试结果', y='电压值', data=testdata);  #条形图
#seaborn.boxplot(x='测试结果', y='电压值', data=testdata);  #箱型图
#seaborn.boxplot(x='Species', y='PetalWidthCm', data=iris);  #箱型图
seaborn.distplot(testdata['电压值']);  #直方图（, kde=False, fit=stats.gamma不需要用模型参数拟合）

""" #pandas实现数据整合后放在一张表里面显示
iris_vir = iris[iris.Species == "Iris-virginica"];
iris_s = iris[iris.Species == 'Iris-setosa'];
iris_ver = iris[iris.Species == 'Iris-versicolor'];
seaborn.distplot(iris_vir['PetalWidthCm'], label='vir').set(ylim=(0,12));
seaborn.distplot(iris_s['PetalWidthCm'], label='s');
seaborn.distplot(iris_ver['PetalWidthCm'], label='ver').legend();
"""

""" #seaborn实现数据整合后放在一张表里面显示
g = seaborn.FacetGrid(iris, hue='Species');
#g = seaborn.FacetGrid(iris, row='Species');
g.map(seaborn.distplot, 'PetalWidthCm').add_legend();
"""

#seaborn.regplot(x='PetalWidthCm', y='PetalLengthCm', data=iris);    #散点图
''' #seaborn实现散点图
g = seaborn.FacetGrid(iris, hue='Species');
g.set(xlim=(0,2.5));
g.map(seaborn.regplot, 'PetalWidthCm', 'PetalLengthCm');
'''
'''
#matplotlib.pyplo实现散点图
g = seaborn.FacetGrid(iris, hue='测试结果');
g.set(xlim=(0,2.5));
g.map(plt.scatter, 'PetalWidthCm', 'PetalLengthCm');
'''
plt.show();  #pycharm上显示图像的方法
