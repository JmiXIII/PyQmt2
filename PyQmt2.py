# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 12:13:54 2016

@author: user11
"""

import pandas as pd
import numpy as np
import glob
import seaborn as sbn
import matplotlib.pyplot as plt
from scipy.stats import sem

path = 'Z:/RESULTATS/807677'
# path = r'C:/Users/user11.HPO-SAMAT/Pictures'


def scan(path, atr, key, size):
    """
    Scan folder for **.x file** containing **string y**
    """
    src = path + "/**/" + key +'.' + atr
    liste = glob.glob(src)
    print(src)
    return liste


# % import
def file2df(elmnt):
    data = pd.read_csv(elmnt, header=None,
                       sep='\t+',
                       index_col=False,)
    data = data[data[3] == True]
    b = {x: 'c_'+str(x) for x in data.columns}
    data.rename(columns=b, inplace=True)
    data = data.dropna()
    return data
#

dfs = []
for file in a:
        df = file2df(file)
        df.c_6.astype(np.float)
        df.c_5.astype(np.float)
        dfs.append(df)
    except:
        print("No+ "+file)
data = pd.concat(dfs)
data.c_6 = data.c_6.astype(np.float)
data.c_5 = data.c_5.astype(np.float)
mean = grouped.c_5.mean().get_values()
std = grouped.c_5.std().get_values()
xx = [x for x in range(len(mean))]
plt.figure(1)
g1 = plt.plot(mean)
plt.fill_between(xx, mean-3*std,
                 mean+3*std, color="#3F5D7D")
plt.figure(2)
plt.style.use('seaborn-paper')
sbn.distplot(data.c_5)
g2 = sbn.stripplot(data.c_5, jitter=True)
#g2.axes.set_xlim(3.95,4.10)




#plt.plot(xx,6*std)
#sbn.plot(d)
#http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/
