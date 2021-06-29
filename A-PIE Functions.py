# -*- coding: utf-8 -*-
"""
 A-PIE

"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2

# Import our own Function and Class files and Reload
import stream_functions
importlib.reload(stream_functions)


# Input Parameters
ric = 'DBK.DE'   # DBK.DE -  MXN=X
file_extension = 'csv'

x, x_str, t = stream_functions.load_time_series(ric, file_extension)
stream_functions.plot_timeseries_price(t, ric)

    


# Compute "Risk Metrics" - Con formato 
x_size = len(x)
x_mean = np.mean(x)
x_stdev = np.std(x)    #Volatility 
x_skew = skew(x)
x_kurt = kurtosis(x) # excess kurtosis 
x_sharpe = x_mean / x_stdev * np.sqrt(252)
x_var_95 = np.percentile(x,5)
x_cvar_95 = np.mean(x[x <= x_var_95]) 
jb = x_size/6*(x_skew**2 + 1/4*x_kurt**2)
p_value = 1 - chi2.cdf(jb, df=2) #Degree Freedom 
is_normal = (p_value > 0.05 ) #Equivalenty x_jarque_bera < 6

# Print Metrics in Graph
round_digits = 4
plot_str = 'mean ' + str(np.round(x_mean,round_digits))\
    + ' / std dev ' + str(np.round(x_stdev,round_digits))\
    + ' / skewness ' + str(np.round(x_skew, round_digits))\
    + ' / kurtosis ' + str(np.round(x_kurt, round_digits))\
    + ' / Sharpe ratio ' + str(np.round(x_sharpe, round_digits)) + '\n'\
    + 'VaR 95% ' + str(np.round(x_var_95, round_digits))\
    + ' / CVaR 95% ' + str(np.round(x_cvar_95, round_digits))\
    + ' / Jarque_Bera ' + str(np.round(jb, round_digits))\
    + ' / p_value ' + str(np.round(p_value, round_digits))\
    + ' / is_normal ' + str(is_normal)

stream_functions.plot_histogram(x, x_str, plot_str, bins=500) 


# Print Metrics
print('mean ' + str(x_mean))
print('std ' + str(x_stdev))
print('skewness ' + str(x_skew))
print('kurtosis ' + str(x_kurt))
print('sharpe ' + str(x_sharpe))  
print('VaR 95% ' + str (x_var_95))
print('CVaR 95% ' + str (x_cvar_95))
print('Jarque-Bera ' + str(jb))
print('p_value ' + str(p_value))
print('is_normal ' + str(is_normal))




# plot histogram
plt.figure()
plt.hist(x,bins=100)
plt.title('Histogram ' + x_str)
plt.show()