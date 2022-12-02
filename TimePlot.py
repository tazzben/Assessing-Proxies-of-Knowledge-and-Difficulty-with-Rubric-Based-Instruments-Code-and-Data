import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import statsmodels.api as sm
from patsy import dmatrices

CalculateDistance = lambda x, y: np.abs(x-y)
CalculateWeight = lambda d: (70/81)*np.power((1-np.power(np.abs(d),3)),3)

def FindValue(x, df, bandwidth):
    bwcount = int(np.ceil(bandwidth*df['Number of Students'].count()))
    df['distance'] = df['Number of Students'].apply(func=CalculateDistance, args=(x,))
    subsample = df.sort_values(by=['distance', ])[:bwcount]
    maxsubvalue = subsample['distance'].max()
    subsample['wdistance'] = subsample['distance']/maxsubvalue
    weight = np.array(subsample['wdistance'].apply(func=CalculateWeight).tolist())
    y, XM = dmatrices("Time ~ Q('Number of Students') + np.power(Q('Number of Students'),2) + np.power(Q('Number of Students'),3)", subsample)
    r = sm.WLS(y, XM, weights=weight).fit().params
    xvals = np.array([1, x, np.power(x,2), np.power(x,3)]).T
    projection = np.dot(r,xvals)
    return projection

def RunLOESS(bandwidth, data):
    xinterval = np.linspace(data['Number of Students'].min(), data['Number of Students'].max(), 1000).tolist()
    yprojections = [FindValue(x, data, bandwidth) for x in xinterval]
    return (xinterval, yprojections)

df = pd.read_csv('Project1Time.csv')
xinterval, yprojections = RunLOESS(0.6, df)
plt.figure()
ax = plt.axes()
ax.set_ylabel('Time (Minutes)')
ax.set_xlabel('Students')
ax.plot(xinterval, yprojections, color='black', linestyle='-')
plt.savefig('TimeToExec.pdf')