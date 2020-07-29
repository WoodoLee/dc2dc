import pandas as pd
import csv
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit
from scipy.stats import chisquare

def func(x, a, b):
    return a * (x**-3) + b

dfCoil = pd.read_csv("coilResult.csv")
dfCoils = dfCoil[dfCoil["x"] >= 10]
dfCoils = dfCoils.abs()

dfCoilX = dfCoils["x"]
dfCoilB = dfCoils["b"]

print(dfCoils)
print(dfCoilX)
print(dfCoilB)

popt, pcov = curve_fit(func, dfCoilX, dfCoilB)
print(popt)
#print(pcov)


yFit = func(dfCoilX, *popt)
chi2 = (yFit - dfCoilB) * (yFit - dfCoilB) 
chi2Sum = chi2.sum(axis=0)
#print(yFit)
#print(chi2)
print(chi2Sum)

bEsti = func(400 , *popt)

print(bEsti)
plt.scatter(dfCoilX, dfCoilB,c='blue',marker='.' ,label = 'simulation data')
plt.grid(True, axis='both', color='gray', alpha=0.5, linestyle='--')
plt.xlabel("distance [mm]")
plt.ylabel("B [$\mu$T]")
plt.plot(dfCoilX, func(dfCoilX, *popt), color='red', linewidth=2, label = 'fit line = $\dfrac{a}{x^3}$ +b , a =1.25919956e+04, b = -1.87886297e-02, $\chi^2$ = 0.87')
plt.legend()
plt.show()

