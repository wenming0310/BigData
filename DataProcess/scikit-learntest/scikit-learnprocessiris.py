import pandas,seaborn
import seaborn as sns
import matplotlib.pyplot as plt #pycharm上显示图像的方法
from sklearn import  linear_model
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn import neighbors
from sklearn import tree
from sklearn import ensemble
from  sklearn.cluster import KMeans
from  sklearn.cluster import DBSCAN
from sklearn import datasets
from pandas import DataFrame
iris = pandas.read_csv("..\\pandas&seaborn\\iris.csv");
#sample5 = iris.sample(5);
#print(sample5)
#计算回归模型
'''#计算回归模型
#matplotlib inline
#seaborn.regplot(x='PetalLengthCm', y='PetalWidthCm', data=iris)

lm = linear_model.LinearRegression();
#features=['PetalLengthCm'];    #1 X
features=['PetalLengthCm', 'SepalLengthCm'];    #2 X1 X2
X = iris[features];
y = iris['PetalWidthCm'];

print(X.shape, y.shape);
model = lm.fit(X,y);
print(model.intercept_, model.coef_);

#-0.3665140452167275 [0.41641913]   #1
#y = -0.3665140452167275 + 0.41641913*X #1
#print(model.predict(4));   #1

#-0.013852011013003152 [ 0.44992999 -0.08190841]    #2
#y = -0.013852011013003152 + 0.44992999*X1 + (-0.08190841*X2)   #2
'''
#交叉检验回归模型
'''
#交叉检验回归模型
lm = linear_model.LinearRegression();
#features=['PetalLengthCm'];    #1 X
#features=['PetalLengthCm', 'SepalLengthCm'];    #2 X1 X2
features=['PetalLengthCm', 'SepalLengthCm', 'SepalWidthCm'];    #3 X1 X2 X3 选对预测组合是很重要的
X = iris[features];
y = iris['PetalWidthCm'];
#score = cross_val_score(lm, X, y, cv=5, scoring='neg_mean_absolute_error');
#score = -cross_val_score(lm, X, y, cv=5, scoring='neg_mean_absolute_error');
score = -cross_val_score(lm, X, y, cv=5, scoring='neg_mean_squared_error');
print(np.mean(score));
'''
#分类及逻辑回归
'''
#分类及逻辑回归
le = LabelEncoder();
le.fit(iris['Species']);

#lm = linear_model.LinearRegression();
lm = linear_model.LogisticRegression();
#features=['PetalLengthCm'];    #1 X
#features=['PetalLengthCm', 'SepalLengthCm'];    #2 X1 X2
features=['PetalLengthCm', 'PetalWidthCm', 'SepalLengthCm', 'SepalWidthCm'];    #3 X1 X2 X3 选对预测组合是很重要的
X = iris[features];
y = le.transform(iris['Species']);
#print(y)
score = cross_val_score(lm, X, y, cv=5, scoring='accuracy');
print(np.mean(score));
'''
#K近邻
'''
#K近邻
le = LabelEncoder();
le.fit(iris['Species']);
features=['PetalLengthCm', 'PetalWidthCm', 'SepalLengthCm', 'SepalWidthCm'];    #3 X1 X2 X3 选对预测组合是很重要的
X = iris[features];
y = le.transform(iris['Species']);
#knn = neighbors.KNeighborsClassifier(5, weights='distance')
knn = neighbors.KNeighborsClassifier(6, weights='uniform')
scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')
print(np.mean(scores));
'''
#决策树
'''
#决策树，大部分为二叉树
dt = tree.DecisionTreeClassifier();
le = LabelEncoder();
le.fit(iris['Species']);
features=['PetalLengthCm', 'PetalWidthCm', 'SepalLengthCm', 'SepalWidthCm'];    #3 X1 X2 X3 选对预测组合是很重要的
X = iris[features];
y = le.transform(iris['Species']);
scores = cross_val_score(dt, X, y, cv=5, scoring='accuracy');
print(np.mean(scores));
'''
#随机森林
'''
#随机森林
#rf = ensemble.RandomForestClassifier(10);
le = LabelEncoder();
le.fit(iris['Species']);
features=['PetalLengthCm', 'PetalWidthCm', 'SepalLengthCm', 'SepalWidthCm'];    #3 X1 X2 X3 选对预测组合是很重要的
X = iris[features];
y = le.transform(iris['Species']);
#scores = cross_val_score(rf, X, y, cv=5, scoring='accuracy');
#print(np.mean(scores));

#随机森林回归
rf = ensemble.RandomForestRegressor(50);
scores = -cross_val_score(rf, X, y, cv=5, scoring='neg_mean_squared_error');
print(np.mean(scores));
'''
#聚类问题
'''
  #数据演示
#%matplotlib inline
g = sns.FacetGrid(iris, hue='Species');
g.set(xlim=(0, 2.5), ylim=(0, 7));
g.map(plt.scatter, 'PetalWidthCm', 'PetalLengthCm').add_legend();
'''
'''
  #聚类
X = iris[[ 'PetalWidthCm', 'PetalLengthCm']];
#km = KMeans(2);
km = KMeans(3);
km.fit(X);
#iris['cluster_k2'] = km.predict(X);
iris['cluster_k3'] = km.predict(X);
g = sns.FacetGrid(iris, hue='cluster_k3');
g.set(xlim=(0, 2.5), ylim=(0, 7));
g.map(plt.scatter, 'PetalWidthCm', 'PetalLengthCm').add_legend();
'''

#DBSCAN
#两个同心圆数据生成
noisy_circles = datasets.make_circles(n_samples=1000, factor=.5, noise=.05);
#print(noisy_circles);

df = DataFrame();
df['x1'] = noisy_circles[0][:,0];
df['x2'] = noisy_circles[0][:,1];
df['label'] = noisy_circles[1];
#print(df.sample(10));
'''
#数据演示
#%matplotlib inline
g = sns.FacetGrid(df, hue='label')
g.map(plt.scatter, 'x1', 'x2').add_legend()
'''
'''
#K均值聚类产生错误分类
km = KMeans(2)
X = df[['x1', 'x2']]
km.fit(X)
df['kmeans_label'] = km.labels_
g = sns.FacetGrid(df, hue='kmeans_label')
g.map(plt.scatter, 'x1', 'x2').add_legend()
'''
#DBSCAN，使用时注意调增eps值
dbscan = DBSCAN(eps=0.15, min_samples=10)
X = df[['x1', 'x2']]
dbscan.fit(X)
df['dbscan_label'] = dbscan.labels_
g = sns.FacetGrid(df, hue='dbscan_label')
g.map(plt.scatter, 'x1', 'x2').add_legend()
#回归、分类属于监督学习，需要x和y，检测模型性能时需要使用交叉检验（区分出训练集和测试集）
#聚类属于无监督学习，只需要x（两大类Kmeans、SBSCAN）


plt.show()