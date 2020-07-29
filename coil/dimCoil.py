import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

mu0 = 1.25663706 * 1e-6

def rCoil(L, N, R):
    r = 1 / N * np.sqrt(2*R / mu0) * L
    return r

def RCoil(L, N, r):
    R = mu0 * N * N  / (2*L) * r * r
    return R


def nCoil(L, r, R):
    N = (L / r) *(np.sqrt(2 * R / mu0))
    return N


L1 = 1.468*1e-6
    
R1 = 9.6*1e-3
r1 = 5*1e-3

rL = rCoil(L1,20,R1)

RL = RCoil(L1,20,r1)

nL = nCoil(L1,r1,R1)

print(RL * 1000)
print(nL)
