from jovispec import chopstacks as cs
import numpy as np


def setls(wav, wavw, mrspec, R, local_median=True):
    c = 299792.0
    if local_median == True:
        norm = np.median(mrspec)
        mspecx = mrspec / norm

    f = np.log(mspecx)
    hx, hxw, hf = cs.setanalogbin(wav, wavw, f, R, 1)
    hx = hx * c
    return hx, hxw, hf, mspecx, norm

