import numpy as np
from decimal import *
from astropy.io import fits


def read_qfits(fitsnum, dir, ext="q"):
    # read scombined spectra
    getcontext().prec = 15
    pfits = dir + "/" + ext + fitsnum + ".fits"
    hduread = fits.open(pfits)
    crval1 = hduread[0].header["CRVAL1"]
    cd1_1 = hduread[0].header["CD1_1"]
    data = hduread[0].data

    lamb = []
    for i in range(0, len(data)):
        lamtmp = Decimal(crval1) + i * Decimal(cd1_1)
        lamb.append(lamtmp)
    lamb = np.array(lamb)
    spec = np.array(data)
    hduread.close()

    return lamb, spec, hduread[0].header
