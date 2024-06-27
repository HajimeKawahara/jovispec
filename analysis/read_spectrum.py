import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from jovispec.abcio import read_irddat

wav, spec, order = read_irddat("data/H/reduc/nw8034325_mmf12.dat")
#dat = pd.read_csv("data/H/reduc/nw8034325_mmf12.dat", delimiter="\s", names=("wav","order","err","spec", "a"))
#wav = dat["wav"]
#spec = dat["spec"]
#order = np.array(dat["order"],dtype=int)


for iorder in range(1,np.max(order)+1):
    mask = order==iorder
    plt.plot(wav[mask], spec[mask])

#plt.ylim(-1000.0,5.e4)
plt.show()
