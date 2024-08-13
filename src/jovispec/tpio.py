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

    dat = pd.read_csv(tpfile, delimiter=",", names=("Temperature (K)", "Pressure (bar)"))
    return dat

if __name__ == "__main__":
#    dat = read_tpprofile_jupiter("jupiter_data/jupiter_atm.txt")
    dat = read_tpprofile_jupiter()