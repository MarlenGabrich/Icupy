import pandas as pd
from datetime import datetime

class Standary():
    def __init__(self):
        ...
    def standa01(self,setdatos):
        arraset = setdatos.to_xarray()
        arraset['datetime'].isoformat()
        period = arraset['datetime'].to_period("Y")
        groupe = pd.Grouper(level=0,freq='H')
        arraset.groupby([period,groupe]).count()

        return arraset


