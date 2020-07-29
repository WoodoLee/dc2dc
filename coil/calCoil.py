import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

mu0 = 1.25663706 * 1e-6

def calLR(H, rIn, rOut, N):
    L = ( mu0 * N*N / (2* np.pi) ) * H * (np.log(rOut / rIn))
    return L

def calLC(R, r , N):
    L = ( mu0 * N*N / (2* np.pi * R) ) * (np.pi * r * r)
    return L



H1 = 20 * 1e-3

rIn1 = 8 * 1e-3
rOut1 = rIn1 + H1

rCross = (H1) /2

R1 = rCross + rIn1
N1 = 30.

calL1r = calLR(H1, rIn1,rOut1, N1)

calL1c = calLC(R1, rCross, N1)

print(calL1r)
print(calL1c)