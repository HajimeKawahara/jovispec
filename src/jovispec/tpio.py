import pandas as pd
import pkg_resources

def read_tpprofile_jupiter(tpfile=None):
    """read temperature-pressure profile of Jupiter, made by atmstruct.py
    
    Args:
        tpfile (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    if tpfile is None:
        path = pkg_resources.resource_filename("jovispec", "jupiter_data/")
        tpfile = path + "jupiter_atm.txt"

    dat = pd.read_csv(tpfile, delimiter=",")
    return dat

if __name__ == "__main__":
#    dat = read_tpprofile_jupiter("jupiter_data/jupiter_atm.txt")
    dat = read_tpprofile_jupiter()
    temperatures = dat["Temperature (K)"]
    pressures = dat["Pressure (bar)"]
    print(temperatures)
    import matplotlib.pyplot as plt
    plt.plot(temperatures,pressures)
    #plt.plot(temperature_low,pressure_low)
    #plt.plot(temperature_up,pressure_up)
    plt.gca().invert_yaxis()
    plt.yscale("log")
    plt.ylabel("Pressure (bar)")
    plt.xlabel("Temperature (K)")
    plt.show()
