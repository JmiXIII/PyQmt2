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


def file2df(elmnt):
    data = pd.read_csv(elmnt, header=None,
                       sep='\t+',
                       index_col=False,)
    data = data[data[3] == True]
    b = {x: 'c_'+str(x) for x in data.columns}
    data.rename(columns=b, inplace=True)
    data = data.dropna()
    return data


# %% chargement des données
a = scan(path, 'log', '*2016*', None)
dfs = []
for file in a:
    try:
        df = file2df(file)
        df.c_6.astype(np.float)
        df.c_5.astype(np.float)
        dfs.append(df)
    except:
        print("error + "+file)

# %% formatage des données
data = pd.concat(dfs)
data.c_6 = data.c_6.astype(np.float)
data.c_5 = data.c_5.astype(np.float)
data.c_0 = pd.to_datetime(data.c_0)
data.c_0 = data.c_0.dt.week
week = data.c_0.unique()
week.sort()

# %% préparation des données
grouped = data.groupby('c_0', as_index=True)
mean = grouped.c_5.mean().get_values()
std = grouped.c_5.std().get_values()
xx = [x for x in range(len(mean))]
y = [x for x in grouped.size().index]

# %% plot
plt.style.use('seaborn-paper')
#plt.rcParams['figure.figsize']=(20,10)
#plt.rcParams['figure.fontsize']=20
plt.figure(1)
g1 = plt.plot(mean)
plt.fill_between(xx, mean-3*std,
                 mean+3*std, color="#3F5D7D")
plt.figure(2)
sbn.distplot(data.c_5)
# g2 = sbn.stripplot(data.c_5, jitter=True)
plt.figure(3)
sbn.tsplot(mean, time=week)
plt.figure(4)
sbn.violinplot(data.c_5, groupby=data.c_0)
plt.figure(5)
sbn.boxplot(data.c_5, groupby=data.c_0)
# g2.axes.set_xticks(np.linspace(3.95,4.10,16,endpoint=True))
# g2.axes.set_xlim(3.95,4.10)




#plt.plot(xx,6*std)
#sbn.plot(d)
#http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/