import matplotlib.pyplot as plt
import pandas
import seaborn
users = pandas.read_csv("train_users_2.csv")

#commdehead = users.head(3)
#commde = users.tail()
#commde = users.describe()   #显示数据属性的数据
#commde = users.shape
#commde = users.loc[:3, 'age']   #:3从0到3 1:3从1到3
#commde = users["age"]

#users["date_account_created"] = pandas.to_datetime(users["date_account_created"])  #格式转换
#commde = users.loc[0,"date_account_created"] - users.loc[1,"date_account_created"]

#users["timestamp_first_active"] = pandas.to_datetime(users["timestamp_first_active"],format="%Y%m%d%H%M%S")
#commde = users["timestamp_first_active"]

commde = users["age"].dropna()

#print(commdehead)
#print(commde)

"""
%matplotlib inline #在jupyter中显示图像
seaborn.distplot(commde)
seaborn.boxplot(commde)
users_with_true_age = users[users["age"]<90]
#seaborn.boxplot(users_with_true_age["age"])
users_with_true_age = users[users["age"]<90]
users_with_true_age = users_with_true_age[users_with_true_age["age"]>10]
seaborn.boxplot(users_with_true_age["age"])
seaborn.distplot(users_with_true_age["age"])
"""
#seaborn.distplot(commde)
#seaborn.boxplot(commde)
#print(type(users["age"]))
users_with_true_age = users[users["age"]<90]
#seaborn.boxplot(users_with_true_age["age"])
users_with_true_age = users[users["age"]<90]
users_with_true_age = users_with_true_age[users_with_true_age["age"]>10]
#seaborn.boxplot(users_with_true_age["age"])
seaborn.distplot(users_with_true_age["age"])
plt.show()