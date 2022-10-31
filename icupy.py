import pandas as pd
from datetime import datetime

class standary():
    def __init__(self):
        ...
    def standa01(setdatos,deltatime):
        setdatos['datetime'].isoformat()
        period = setdatos['datetime'].to_period("Y")
        groupe = pd.Grouper(level=0,freq='H')
        setdatos.groupby([period,groupe]).count()

        return setdatos


