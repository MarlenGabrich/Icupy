import pandas as pd
import numpy as np
from datetime import datetime
import statistics

class Staty():
    def __init__(self):
        ...
    def soutliers(self,conj_datos):

        """ Función de criterio estadístico para detectar 
        valores extremos.

        Parameters
        ----------
        conj_datos: narray
            columna del set de datos que se quiere analizar
            (se recomienda: temperatura, humedad y presión)

        Returns
        -------
        statistics_par: dict
            retorna un aviso de éxito y los valores de la 
            media y el desvío estándar. 
        """

        media = conj_datos.mean()
        dest = np.std(conj_datos)

        statistics_par = {'media': round(media,2),
                          'desvio_estandar': round(dest,2)}

        limite_inferior = media-3*dest
        limite_superior = media+3*dest

        for i in conj_datos:
            if i<limite_inferior or i>limite_superior:
                raise statistics.StatisticsError('The standard deviation exceeds the defined limit')

        return 'Singular analysis passed! ;) ', statistics_par

class Standary():
    def __init__(self):
        ...

    def stanjoin(self,setdatos):

        """ Función para unir columnas de fecha y hora en una única con
        formato datetime y homogeneizar por hora. Agrupa valores repetidos
        dejando la media.

        Parameters
        ----------
        setdatos: set
            data set crudo (omixom requiere)
        
        Returns
        -------
        setdatos: set
            modificado

        """

        setdatos['datetime'] = setdatos['Fecha'] + ' ' + setdatos['Hora']
        setdatos['datetime'] = pd.to_datetime(setdatos['datetime'],
                                              dayfirst = True,
                                              infer_datetime_format=True).round('H')

        daset = setdatos.groupby(by=['datetime']).mean().round(2)
        
        return daset

