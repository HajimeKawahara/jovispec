"""Raw data analysis of Jupiter/miniIRD using pyird
"""
import matplotlib.pyplot as plt
import pathlib
import numpy as np

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
flat = irdstream.Stream2D("flat", datadir, anadir, rawtag="2017011", fitsid=[8140833, 8140945, 8141330], rotate=True, detector_artifact=True)

# target 34325
target = irdstream.Stream2D("target", datadir, anadir, rawtag="2017011", fitsid=[8034325], rotate=True)

#dark
dark = irdstream.Stream2D("dark", datadir, anadir, rawtag="2017011", fitsid=[8133836], rotate=True)

#Th-Ar wavelength calibration data
thar=irdstream.Stream2D("thar",datadir,anadir,rawtag="2017011",fitsid=[8143952, 8144142, 8144237, 8144415],rotate=True)

# mask from flat
trace_mmf = flat.aptrace(cutrow=580, nap=21)
trace_mask = trace_mmf.mask()

# dark
from pyird.image.bias import bias_subtract_image
from pyird.image.hotpix import identify_hotpix_sigclip
median_image = dark.immedian()
im_subbias = bias_subtract_image(median_image)
hotpix_mask = identify_hotpix_sigclip(im_subbias)

#
trace_mmf.mmf2()

#wavelength calibration
thar.trace = trace_mmf
thar.clean_pattern(trace_mask=trace_mask,extin='', extout='_cp', hotpix_mask=hotpix_mask)
thar.calibrate_wavelength()

