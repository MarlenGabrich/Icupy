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

        limite_inferior = media-5*dest
        limite_superior = media+5*dest

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
        omixom: bool
            si es True, concatena las columnas de fecha y hora
        
        Returns
        -------
        setdatos: set
            modificado

        """
        
        setdatos['datetime'] = pd.to_datetime(setdatos['datetime'],
                                              dayfirst = True,
                                              infer_datetime_format=True).round('H')

        daset = setdatos.groupby(by=['datetime']).mean().round(2)
        
        return daset

    def fill_in(self,dataset):

        """Función para rellenar con valores nulos los datos faltantes en 
        el set

        Parameters
        ----------
        dataset: set
            set de datos a rellenar

        Returns
        -------
        dataset: set
            set del rango buscado
        """

        dataset.resample('H').fillna(None)

        return dataset

class Comply():
    def __init__(self):
        ...

    def cuty(self,dataset,inicio, fin):
        
        """Función para cortar el set de datos
        
        Parameters
        ----------
        dataset: set
            set de datos a recortar
        
        Returns
        -------
        dataset_cut: set
            set recortado
        """

        dataset.reset_index(drop=False, inplace=True)
        
        indice_fin = dataset.loc[dataset['datetime']==fin].index[0]
        indice_inicio = dataset.loc[dataset['datetime']==inicio].index[0]
        datas = dataset[indice_inicio:indice_fin]

        if dataset.isin(['datetime',inicio] or dataset.isin(['datetime'],fin)) is False:
            raise Exception('The selected date range is not included in the dataset')

        return datas

class Icu():
    def __init__(self):
        ...
    def promaxmy(self,dataset, omixom:bool):
        
        if omixom:
            dataset['temperature']=dataset['Temperatura [°C]']

        dataset['datetime'] = pd.to_datetime(dataset['datetime'], infer_datetime_format= True)

        day_mean = dataset.groupby(dataset['datetime'].dt.date)['temperature'].mean()
        day_min = dataset.groupby(dataset['datetime'].dt.date)['temperature'].min()
        day_max = dataset.groupby(dataset['datetime'].dt.date)['temperature'].max()

        day = {'day_min': day_min,
               'day_mean': day_mean,
               'day_max': day_max}

        return day
