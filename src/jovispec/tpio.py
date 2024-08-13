import pandas as pd
import pkg_resources

def read_tpprofile_jupiter(tpfile=None):
    if tpfile is None:
        path = pkg_resources.resource_filename("jovispec", "jupiter_data/")
        tpfile = path + "jupiter_atm.txt"

    dat = pd.read_csv(tpfile, delimiter=",", names=("Temperature (K)", "Pressure (bar)"))
    return dat

if __name__ == "__main__":
#    dat = read_tpprofile_jupiter("jupiter_data/jupiter_atm.txt")
    dat = read_tpprofile_jupiter()