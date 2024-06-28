import numpy as np
from decimal import *
from astropy.io import fits
import pandas as pd


def read_irddat(datfile):
    """
    Reads petitIRD JUPITER data (NIR),

    Args:
    datfile: dat file name (e.g. data/H/reduc/nw8034325_mmf12.dat)

    Returns:
        ndarray real, real, int : wavelength (uncalibrated, angstrom), spectrum, order
    """

    dat = pd.read_csv(
        datfile,
        delimiter="\s",
        names=("wav", "order", "err", "spec", "a"),
    )
    wav = np.array(dat["wav"])*10 #AA
    spec = np.array(dat["spec"])
    order = np.array(dat["order"], dtype=int)

    return wav, spec, order


def read_qfits(fitsnum, dir, ext="q"):
    """
    Reads HDS JUPITER data (visible)

    Args:
        fitsnum (_type_): _description_
        dir (_type_): _description_
        ext (str, optional): _description_. Defaults to "q".

    Returns:
        _type_: _description_
    """
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
