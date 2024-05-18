import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./00-insurance.csv')

# df.info()
# print(df.isnull().sum())
# print(df.describe())

# print(df.dtypes)
# print(df.dtypes['age'], type(df.dtypes['sex']))

# f1 = df['sex'] == 'male'
# f2 = df['age'] > 25
# print(df.where(f1 & f2).dropna().sort_values(by='age', ascending=True).head(20))


# -- converting to binary data
# another_df = pd.get_dummies(df["sex"])
# print(another_df)  # return pandas data frame
# print(type(another_df))


# --- Median
"""
The median of a set of numbers is the value separating the higher half from the lower half
of a data sample, a population, or a probability distribution.
"""

# print(df['age'].median())
# print(statistics.median(df['age']))
# print(statistics.mean(df['age']))


# print(statistics.median([1, 2, 3, 4, 5, 6]))  # 3.5
# print(statistics.median_high([1, 2, 3, 4, 5, 6]))  # 4
# print(statistics.median_low([1, 2, 3, 4, 5, 6]))  # 3
# print(statistics.median([1, 2, 3, 4, 5, 6, 7]))  # 4
# print(statistics.median([10, 8, 5, 15, 7, 16, 9]))  # sorted [5, 7, 8, [9], 10, 15, 16], median=9
# print(statistics.median([5, 7, 8, 11, 14, 15]))  # [5, 7, [8, 11], 14, 15], median=(11+8)/2=9.5
# print(statistics.median([5, 7, 8, 11, 14, 15]))  # [5, 7, [8, 11], 14, 15], median=(11+8)/2=9.5


# --- Mean
"""
A mean is a numeric quantity representing the center of a collection of numbers
and is intermediate to the extreme values of a set of numbers.
"""
# print(statistics.mean([1, 2, 3]))  # 2
# print(statistics.mean([10, 10, 10]))  # 10
# print(df['age'].mean())

# --- Geometric mean (GM)
"""
In mathematics, the geometric mean is a mean or average which indicates a [[central tendency]]
of a finite set of real numbers by using the product of their values.
"""
# print(round(statistics.geometric_mean([54, 24, 36]), 1))  # [24, 36, 54]
# print(round(statistics.geometric_mean([1, 2, 3]), 1))  # 1.8
# print(round(statistics.geometric_mean([1, 2, 3]), 2))  # 1.82
# print(round(statistics.geometric_mean([1, 2, 3]), 4))  # 1.8171

# --- Harmonic mean (HM)
"""
The harmonic mean is a numerical average calculated by dividing the number of observations, or entries in the series,
by the reciprocal of each number in the series.
"""
# print(statistics.harmonic_mean([40, 60], weights=[5, 30]))  # 56.0
# print(statistics.harmonic_mean([1, 2, 3], weights=[1, 2, 3]))  # 2.0
# print(statistics.harmonic_mean([1, 2, 3], weights=[1, 2, 1]))  # 1.7142857142857142


# --- Mode
"""
A mode of a continuous probability distribution is often considered to be any value x at
which its probability density function has a locally maximum value.
"""
# print(statistics.mode([1, 1, 2, 5, 5, 5, 5, 1, 2, 6, 10, 12, 6]))  # 5
# print(df.mode())  # for all columns
# print(df["age"].mode())  # for specific column
# print(statistics.mode(['red', 'gray', 'red', 'blue', 'green', 'gray', 'blue', 'gray']))
# print(statistics.multimode('aaabbbdxxxxxcbcc'))  # x

# --- Quantile
"""
In statistics and probability, quantiles are cut points dividing the range of a probability distribution
into continuous intervals with equal probabilities,
or dividing the observations in a sample in the same way.
There is one fewer quantile than the number of groups created.
"""

# print(np.quantile(df['charges'], [0, 0.25, 0.5, 0.75, 1]))  # return type <class 'numpy.ndarray'>
Q1 = df['charges'].quantile(0.25)
Q2 = df['charges'].quantile(0.5)
Q3 = df['charges'].quantile(0.75)
IQR = Q3 - Q1
# print(f"Q1:{Q1} Q2:{Q2} Q3:{Q3} IQR:{IQR}")
df_without_outliers = df[(df['charges'] > (Q1 - (IQR * 1.5))) & (df['charges'] < (Q3 + (IQR * 1.5)))]
# print(df_without_outliers)
# print((df.shape[0] - df_without_outliers.shape[0]), "{} {}".format(df.shape[0], df_without_outliers.shape[0]))

# --- Kurtosis & Skew
"""
In probability theory and statistics, kurtosis is a measure of the "tailedness" of the probability distribution
of a real-valued random variable.

In probability theory and statistics, skewness is a measure of the asymmetry of the probability distribution
of a real-valued random variable about its mean. The skewness value can be positive, zero, negative, or undefined.
"""

# print(df_without_outliers['charges'].kurtosis())
# print(df_without_outliers['charges'].skew())

# df_without_outliers['charges'].hist()
# plt.show()

# plt.boxplot(df_without_outliers['charges'])
# plt.show()

# --- Max and Min, difference of max and min

nums = [1, 2, 3, 4, 5]
max_of_nums = max(nums)
min_of_nums = min(nums)
range_of_min_max = max_of_nums - min_of_nums
# print("min: {}, max: {}, range: {}".format(min_of_nums, max_of_nums, range_of_min_max))


# --- Standard deviation, Variance, Covariance
"""
In statistics, the standard deviation is a measure of the amount of variation of a random variable
expected about its mean. A low standard deviation indicates that the values tend to be close to the mean of the set,
while a high standard deviation indicates that the values are spread out over a wider range

In probability theory and statistics, variance is the expected value of the squared deviation
from the mean of a random variable. The standard deviation is obtained as the square root of the variance.

Covariance in probability theory and statistics is a measure of the joint variability of two random variables.
The sign of the covariance, therefore, shows the tendency in the linear relationship between the variables.

"""

