import os
import pandas as pd
from matplotlib import pyplot as plt

HOUSING_PATH = "datasets/housing"
HOUSING_CSV = "housing.csv"

def load_housing_data(path = HOUSING_PATH):
    csv_path = os.path.join(path, HOUSING_CSV)
    return pd.read_csv(csv_path)

# 查看数据集的基本信息
housing_data = load_housing_data()
print(housing_data.info())
print(housing_data.describe())

# 查看前5行数据
head_data = housing_data.head()
print(head_data)

# ocean_proximity列的不同数值数量
ocean_proximity_value_counts = housing_data["ocean_proximity"].value_counts()
print(ocean_proximity_value_counts)

# 显示直方图
housing_data.hist(bins = 50, figsize = (20, 15))
plt.show()