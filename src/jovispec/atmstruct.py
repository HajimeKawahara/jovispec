"""Visualize the temperature-pressure profile of the lower and upper atmosphere of Jupiter taken by Galileo probe.
The data is taken from the PDS Atmospheres Node
https://pds-atmospheres.nmsu.edu/cgi-bin/getdir.pl?volume=gp_0001&dir=data/asi
Put the data in the rawdata directory.

you need 
pdr pavkage (https://github.com/MillionConcepts/pdr)
and 
pvl: (pip install pvl)

"""

import pdr
import matplotlib.pyplot as plt
import numpy as np

data_low = pdr.read("/home/kawahara/jovispec/rawdata/loweratm.lbl")
data_up = pdr.read("/home/kawahara/jovispec/rawdata/upperatm.lbl")
table_low = data_low["TABLE"]
table_up = data_up["TABLE"]

# check units
column = data_low.metadata["TABLE"].getall("COLUMN")
#print(column[1]) bar
column = data_up.metadata["TABLE"].getall("COLUMN")
#print(column[2]) milibar

pressure_low = table_low["PRESSURE"]
temperature_low = table_low["TEMPERATURE"]
pressure_up = table_up["PRESSURE"]*1.e-3
temperature_up = table_up["TEMPERATURE"]

pressures = np.hstack((pressure_up,pressure_low))
temperatures = np.hstack((temperature_up,temperature_low))

plt.plot(temperatures,pressures)
#plt.plot(temperature_low,pressure_low)
#plt.plot(temperature_up,pressure_up)
plt.gca().invert_yaxis()
plt.yscale("log")
plt.ylabel("Pressure (bar)")
plt.xlabel("Temperature (K)")
plt.title("Temperature-Pressure profile of Jupiter")
plt.savefig("jupiter_atm.png")
plt.show()

#save
np.savetxt("jupiter_data/jupiter_atm.txt",np.vstack((temperatures,pressures)).T,delimiter=",",header="Temperature (K),Pressure (bar)",comments="")