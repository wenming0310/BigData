import pandas
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder

iris = pandas.read_csv("..\\pandas&seaborn\\iris.csv");
le = LabelEncoder()
le.fit(iris['Species'])
lm = linear_model.LogisticRegression()#这里可以换成其他的模块
features = ['PetalLengthCm','PetalWidthCm','SepalLengthCm','SepalWidthCm']
y = le.transform(iris['Species'])

selected_features = []
rest_features = features[:] #[:]表示深度复制。如果不用深度复制，当仅用rest_features = features时，
                            # 在内存中指向相同的内存地址，如果改其中一个另一个也会改变
best_acc = 0
while len(rest_features)>0:
    temp_best_i =  ''
    temp_best_acc = 0
    for feature_i in rest_features:
        temp_features = selected_features + [feature_i,]#将feature_i变成列表，列表只能和列表相加
        X = iris[temp_features]
        scores = cross_val_score(lm, X, y, cv=5, scoring='accuracy')#交叉检验
        acc = np.mean(scores)
        if acc > temp_best_acc:
            temp_best_acc = acc
            temp_best_i = feature_i
    print("select", temp_best_i, "acc:", temp_best_acc)
    if temp_best_acc > best_acc:
        best_acc = temp_best_acc
        selected_features += [temp_best_i,]
        rest_features.remove(temp_best_i)
    else:
        break
print("best feature set: ", selected_features, "acc: ", best_acc)
#print("features: ", features, "rest_features: ", rest_features)    #检验深度复制

