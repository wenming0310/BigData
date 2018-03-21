import pandas
from scipy import stats
from scipy.stats.stats import pearsonr
import numpy as np
import statsmodels.stats.weightstats
iris = pandas.read_csv("..\\pandas&seaborn\\iris.csv");
'''
#假设检验
iris_sample = iris.sample(10);
print(np.mean(iris['SepalLengthCm']));
#z检验
z = statsmodels.stats.weightstats.ztest(iris_sample['SepalLengthCm'], value=7);
print(z);
#t检验
t = stats.ttest_1samp(iris_sample['SepalLengthCm'], popmean=7);
print(t);
'''
'''
iris_1 = iris[iris.Species == 'Iris-setosa'];
iris_2 = iris[iris.Species == 'Iris-virginica'];
ind = stats.ttest_ind(iris_1['SepalLengthCm'], iris_2['SepalLengthCm']);
print(ind);
print(np.mean(iris_1['SepalLengthCm']));
print(np.mean(iris_2['SepalLengthCm']));
'''
'''
list_fudan = [ 170.6, 169.5, 176.2, 181.5, 174.5, 167. , 175.2, 177.8, 171.3, 178.5];
list_jiaoda = [ 164.1, 170.5, 165.7, 167.2, 168. , 167.7, 168.3, 167.6, 170.6, 166.6];
ind = stats.ttest_ind(list_fudan, list_jiaoda);
print(ind);
'''

#相关性系数：皮尔逊系数
pearsonr_value = pearsonr(iris['SepalLengthCm'], iris['SepalWidthCm'])
print(pearsonr_value)

#跌倒特征选择，先假定选定模型，然后可使用
#用暴力解法，枚举/穷举法（把所有可能组合全部试一遍，复杂度2^N，在特征量少时可以使用，但是不建议使用）
#递增/递减

