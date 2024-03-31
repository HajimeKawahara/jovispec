"""Raw data analysis of Jupiter/miniIRD using pyird
"""

import pathlib

basedir = pathlib.Path("~/jovispec/analysis/data/H").expanduser()

band = "h"  #'h' or 'y'
mmf = "mmf2"  #'mmf1' (comb fiber) or 'mmf2' (star fiber)
skipLFC = (
    False  # if False, uncertainties are output. mmf1 of y band must be reduced first.
)

from pyird.utils import irdstream

## FLAT
datadir = basedir / "raw/"
anadir = basedir / "reduc/"

# flat
flat = irdstream.Stream2D(
    "flat", datadir, anadir, rawtag="2017011", fitsid=[8140833, 8140945, 8141330], rotate=True
)
trace_mmf = flat.aptrace(cutrow=1200, nap=21)

# target 34325
target = irdstream.Stream2D(
    "target", datadir, anadir, rawtag="2017011", fitsid=[8034325]
)

dark = irdstream.Stream2D("dark", datadir, anadir, rawtag="2017011", fitsid=[8133836])
