import pandas as pd
import numpy as np
a=np.random.randint(1,50,100)
df=pd.read_csv(r'C:\Users\Shrutika\Desktop\spyder programs\Clustering\CC GENERAL.csv')
df.columns
x=pd.DataFrame(df.PAYMENTS)
from sklearn.cluster import KMeans
obj=KMeans(n_clusters=4)
obj.fit_predict(x)
import matplotlib.pyplot as plt
b=obj.cluster_centers_
plt.scatter(x.PAYMENTS,x.PAYMENTS,c=obj.labels_,cmap='rainbow')
