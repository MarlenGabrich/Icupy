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

    def stanjoin(self,setdatos, omixom:bool):

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
        if omixom:
            setdatos['datetime'] = setdatos['Fecha'] + ' ' + setdatos['Hora']

        setdatos['datetime'] = pd.to_datetime(setdatos['datetime'],
                                              dayfirst = True,
                                              infer_datetime_format=True).round('H')

        daset = setdatos.groupby(by=['datetime']).mean().round(2)
        
        return daset

class Comply():
    def __init__(self):
        ...
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
        count = -1
        for j in dataset.index:
            count += 1
            if j==inicio:
                dataset.drop(dataset.index[[0,count]], axis='index', inplace=True)
            if j==fin:
                dataset.drop(dataset.index[[count,-1]], inplace=True)

        if inicio and fin not in dataset.index:
            raise Exception('The selected date range is not included in the dataset')

        return dataset

