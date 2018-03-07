import pandas,seaborn
import matplotlib.pyplot as plt #pycharm上显示图像的方法
from sklearn import  linear_model
from sklearn.model_selection import cross_val_score
import numpy as np

iris = pandas.read_csv("..\\pandas&seaborn\\iris.csv");
#sample5 = iris.sample(5);
#print(sample5)

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

#检验回归模型
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





plt.show()