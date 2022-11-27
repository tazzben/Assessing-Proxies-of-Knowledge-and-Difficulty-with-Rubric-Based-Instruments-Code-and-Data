import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

df = pd.read_csv('Project1Time.csv')
s = df['Number of Students'].to_list()
t = df['Time'].to_list()
f = interp1d(s, t, kind='cubic', fill_value="extrapolate")
xnew = np.linspace(3, 150, num=1000, endpoint=True)
plt.figure()
ax = plt.axes()
ax.set_ylabel('Time')
ax.set_xlabel('Students')
ax.plot(xnew, f(xnew), color='black', linestyle='-')
plt.savefig('TimeToExec.pdf')