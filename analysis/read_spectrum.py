import matplotlib.pyplot as plt
import numpy as np
from jovispec.abcio import read_irddat

wav, spec, order = read_irddat("data/H/reduc/w8034325_mmf12.dat")
#wav, blaze, order = read_irddat("data/H/reduc/nw8034325_mmf12.dat")

for iorder in range(1, np.max(order) + 1):
    mask = order == iorder
    plt.plot(wav[mask], spec[mask])
    plt.plot(wav[mask], spec[mask])

# plt.ylim(-1000.0,5.e4)
plt.show()
