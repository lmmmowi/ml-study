import os
import tarfile
from six.moves import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"
HOUSING_TGZ = "housing.tgz"
HOUSING_URL =  DOWNLOAD_ROOT + HOUSING_PATH + "/" + HOUSING_TGZ

def fetch_housing_data(url = HOUSING_URL, path = HOUSING_PATH):
    if not os.path.isdir(path):
        os.makedirs(path)
    tgz_path = os.path.join(path, "housing.tgz")
    urllib.request.urlretrieve(url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path = path)
    housing_tgz.close()

# 加载数据
fetch_housing_data()