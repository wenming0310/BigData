import pandas
import seaborn
import matplotlib.pyplot as plt #pycharm上显示图像的方法
iris = pandas.read_csv("iris.csv");
#print(iris.head());
#print(iris.tail());
#print(iris.sample(10));
#print(iris.describe());

#%matplotlib inline #jupter上显示图像
#seaborn.countplot("Species", data=iris);    #条形图
#seaborn.barplot(x='Species', y='PetalLengthCm', data=iris);  #条形图
#seaborn.boxplot(x='Species', y='PetalLengthCm', data=iris);  #箱型图
#seaborn.boxplot(x='Species', y='PetalWidthCm', data=iris);  #箱型图
#seaborn.distplot(iris['PetalWidthCm']);  #直方图

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
#matplotlib.pyplo实现散点图
g = seaborn.FacetGrid(iris, hue='Species');
g.set(xlim=(0,2.5));
g.map(plt.scatter, 'PetalWidthCm', 'PetalLengthCm');

plt.show();  #pycharm上显示图像的方法
