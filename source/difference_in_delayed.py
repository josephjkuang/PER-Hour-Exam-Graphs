import csv  # to read csv files
import numpy as np  # to use statistics functions
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import scipy
import pandas as pd
from scipy import stats
d02=[]
d12=[]
d03=[]
d13=[]
e2="../data/Sp21_Physics_211_HE2_data.csv"
e3="../data/Sp21_Physics_211_HE2_data.csv"

with open(e2) as f:
    reader = csv.reader(f)
    list_2=list(reader)
    labels=list_2.pop(0)
with open(e3) as f:
    reader = csv.reader(f)
    list_3=list(reader)
    labels=list_3.pop(0)
for i in list_2:
    if(i[5]!="NULL" and i[6]!="NULL"):
        if(float(i[5])==0):
            if (float(i[6])<100):
                d02.append(float(i[6]))
            else:
                print(i[0])
        elif(float(i[5])==1):
            if (float(i[6])<100):
                d12.append(float(i[6]))
            else:
                print(i[0])
for j in list_3:
    if(j[5]!="NULL" and j[6]!="NULL"):
        if(float(j[5])==0):
            if (float(j[6])<100):
                d03.append(float(j[6]))
            else:
                print(j[0])
        elif(float(j[5])==1):
            if (float(j[6])<100):
                d13.append(float(j[6]))
            else:
                print(j[0])
d02=np.array(d02)
d12=np.array(d12)
d03=np.array(d03)
d13=np.array(d13)
plt.boxplot((d02,d12),labels=("delayed=0","delayed=1"),showmeans=True, meanline=True,medianprops={'linewidth': 2, 'color': 'orange'},
           meanprops={'linewidth': 2, 'color': 'red'})
plt.title("Hour exam 2")
plt.ylabel("Questions answered")
plt.savefig("../graphs/difference_in_delay_HE2.png")
plt.show()
plt.boxplot((d03,d13),labels=("delayed=0","delayed=1"), showmeans=True, meanline=True,medianprops={'linewidth': 2, 'color': 'orange'},
           meanprops={'linewidth': 2, 'color': 'red'})
plt.title("Hour exam 3")
plt.ylabel("Questions answered")
plt.savefig("../graphs/difference_in_delay_HE3.png")
plt.show()




