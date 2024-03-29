# JoviSpec

### Jupiter high-dispersion spectra collection as observed by Subaru/HDS and its spectral decomposition


This repository provides high-dispersion spectra of Jupiter as observed Subaru/HDS (PI: H.Kawahara) and a little analysis of them. It includes an algorithm for decomposing the spectra of Jupiter, the Sun, and the Earth (telluric). This algorithm was developed by me ( @HajimeKawahara ) and @kemasuda, but the code is an old one I wrote back **in 2016**. Moreover, it was written for Python 2.7. This time, with minimal changes (such as making it run on Python 3), I am publishing it for use in high-dispersion retrievals of reflected light.


<img src="https://github.com/HajimeKawahara/jovispec/assets/15956904/bdc252de-b642-4f42-a163-50e52df93413" Titie="jovispec" Width=1200px>


### Install

```sh
python setup.py install
```

### Get Started

See notebooks in ipynb.

### Gallery

<img src="https://github.com/HajimeKawahara/jovispec/assets/15956904/87f10019-dc39-43c5-bca2-f538496e28c2" Titie="jovispec" Width=500px> <img src="https://github.com/HajimeKawahara/jovispec/assets/15956904/52db67d9-6b0b-48c1-b14c-f957b5b1bb7b" Titie="jovispec" Width=500px>

x-axis = angstrom, setting = NIRc


<img src="https://github.com/HajimeKawahara/jovispec/assets/15956904/ee19fb37-60f7-49b1-8b6f-5442207d0b74" Titie="jovispec" Width=1200px>


## Data Infomation

- ObsID 14199
- Date 2014-10-20 (UT)
- NIRc, IS#2 (0.45"x3), 2x1bin 

### Objects

- 60000-08 WASP33 (A-type star)
- 60030/31 HD13041
- 60032/33 - 36/37 JUPITER CENTER
- 60038/39, 40/41 JUPITER NORTH
- 60042/43, 44/45 JUPITER SOUTH
- 60048/47 JUPITER WEST
- 60050/49 JUPITER EAST

