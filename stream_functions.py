# -*- coding: utf-8 -*-
"""
 A-PIE
 Stream_function
Vamos a Guardar todas las Funciones 
"""
#Libraries
import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2

def load_time_series(ric, file_extension):
    #  Get Market Data
    path = 'C:\\Users\casa\\Downloads\\Finanzas Cuantitativas Py\\Bases de Datos\\' +ric+ '.' + file_extension
    table_raw = pd.read_csv(path) 
    #Create table of returns
    t = pd.DataFrame()
    t['date'] = pd.to_datetime(table_raw['Date'], dayfirst=True)
    t['close'] = table_raw['Close']
    t.sort_values(by='date', ascending=True)
    t['close_previous'] = table_raw['Close'].shift(1)
    t['returns_close'] = t['close']/t['close_previous'] -1 
    t = t.dropna()
    t = t.reset_index(drop=True)
    # Input for Jarque-Bera
    x = t['returns_close'].values           #Returns - Array
    x_str = 'Real_returns' + ric       #Etiquetas - Label RIC
    
    return x, x_str, t 

def plot_timeseries_price(t, ric):
    # Plot Timeseries of Prices - Gráfica de Series de Tiempo del Precio 
    plt.figure()
    plt.plot(t['date'],t['close'])
    plt.title('Time Series Real Prices' + ric)
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.show()

def plot_histogram(x, x_str, plot_str, bins=100):
    #Plot Histogram
    plt.figure()
    plt.hist(x, bins)
    plt.title('Histogram ' + x_str)
    plt.xlabel(plot_str) 
    plt.show()
    
    
    
    
    