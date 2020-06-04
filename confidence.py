import numpy as np
import scipy.stats as st
d=np.random.randint(1,10,100)
z=st.norm.ppf(q=0.975)
t=st.t.ppf(q=0.975,df=95)
moe=z*np.std(d)/np.sqrt(len(d))
UL=moe+np.mean(d)
LL=moe-np.mean(d)
print(UL,LL)