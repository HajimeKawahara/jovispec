import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dat = pd.read_csv("data/H/reduc/w8034325_mmf12.dat", delimiter="\s", names=("wav","err","spec"))

#dat = pd.read_csv("data/H/reduc/nw8034325_mmf12.dat", delimiter="\s", names=("wav","err","spec"))
wav = dat["wav"]
spec = dat["spec"]

# intra detector gaps 
mask_1 = 63 + 128*np.array(range(0,256+64+16),dtype=int)
mask_2 = 64 + 128*np.array(range(0,100),dtype=int)

rm = True
if rm:
    ns=6
    #ns=4
    for i in mask_1:
        #    plt.plot(wav[i],spec[i],"*",color="blue")
        #    plt.plot(wav[i+1],spec[i+1],"*",color="red")
        for j in range(0,ns):
            spec[i+j]=None
            spec[i-j]=None

    #outlier
    spec[spec<=0.0]=None
    spec[spec>50000.0]=None        

plt.plot(wav, spec)

    #spec[i]=None
    
#plt.ylim(-1000.0,5.e4)
plt.show()
