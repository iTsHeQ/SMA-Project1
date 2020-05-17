from numpy.random import randn
from numpy.random import seed
from scipy.stats import pearsonr


array1 = [55, 46, 73, 55, 37, 73, 54, 37, 46, 54, 38, 46, 55, 38, 34, 38, 23, 34, 30, 23, 20, 30,
38, 20, 19, 38, 34, 20, 23, 20, 14, 23, 14, 19, 24, 17, 15, 14, 19, 24, 17, 15]

array2 = [46, 55, 55, 73, 73, 37, 37, 54, 54, 46, 46, 38, 38, 55, 38, 34, 34, 23, 23, 30, 30, 20
, 20, 38, 38, 19, 20, 34, 20, 23, 23, 14, 19, 14, 17, 24, 14, 15, 24, 19, 15, 17]

corr, _ = pearsonr(array2, array1)
print(corr)