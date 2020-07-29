import pandas as pd
import csv
import matplotlib.pyplot as plt
import sys
import math
import ROOT
import numpy as np
from ROOT import TCanvas, TGraph



dfCoil = pd.read_csv("coilResult.csv")
dfCoils = dfCoil[dfCoil["x"] >= 10]

dfCoilX = dfCoils["x"]
dfCoilB = dfCoils["b"]


#Some data
x = np.arange(10)
y = x**2

#Canvas to plot on and graph
c = TCanvas()
g = TGraph(len(dfCoilX), dfCoilX,dfCoilB )

#Draw canvas and graph
c.Draw()
g.Draw()