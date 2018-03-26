import pandas,seaborn
from sklearn import  linear_model
#import seaborn as sns
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt #pycharm上显示图像的方法

data = pandas.read_csv("G0360_Match_180322 - t.csv");

#seaborn.regplot(x='ID', y='11', data=data)
g = seaborn.FacetGrid(data, hue='ID');
#g.set(xlim=(0,2.5));
g.map(seaborn.regplot, '1', '2', '3', '11');

g = seaborn.FacetGrid(data, hue='ID');
g.set(xlim=(0,2.5));
g.map(seaborn.regplot, 'PetalWidthCm', 'PetalLengthCm');

plt.show()