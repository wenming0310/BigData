import pandas
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
import copy

iris = pandas.read_csv("..\\pandas&seaborn\\iris.csv");
le = LabelEncoder()
le.fit(iris['Species'])
lm = linear_model.LogisticRegression()#这里可以换成其他的模块
features = ['PetalLengthCm','PetalWidthCm','SepalLengthCm','SepalWidthCm']
y = le.transform(iris['Species'])

selected_features = []
print(id(features[0]))
# 赋值：简单地拷贝对象的引用，两个对象的id相同。
#rest_features = features    # 赋值操作不可取，两个变量指向同一个地址
# 浅拷贝：创建一个新的组合对象，这个新对象与原对象共享内存中的子对象。
# 常见的浅拷贝有：切片操作、工厂函数、对象的copy()方法、copy模块中的copy函数。
#rest_features = features[:] # [:]表示切片操作，切片操作会造成浅拷贝，之所以变量没改是因为修改不可变对象（str、tuple）需要开辟新的空间，
                             # 修改可变对象（list等）不需要开辟新的空间
#rest_features = copy.copy(features) #浅拷贝
# 深拷贝：创建一个新的组合对象，同时递归地拷贝所有子对象，新的组合对象与原对象没有任何关联。虽然实际上会共享不可变的子对象，但不影响它们的相互独立性。
# 深拷贝只有一种方式：copy模块中的deepcopy函数。
# 浅拷贝和深拷贝的不同仅仅是对组合对象来说，所谓的组合对象就是包含了其它对象的对象，如列表，类实例。而对于数字、字符串以及其它“原子”类型，没有拷贝一说，产生的都是原对象的引用。
rest_features = copy.deepcopy(features)
# 对于不可变对象，当需要一个新的对象时，python可能会返回已经存在的某个类型和值都一致的对象的引用。
# 而且这种机制并不会影响 a 和 b 的相互独立性，因为当两个元素指向同一个不可变对象时，对其中一个赋值不会影响另外一个。
print(id(rest_features[0]))

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
print("features: ", features, "rest_features: ", rest_features)    #检验深度复制

