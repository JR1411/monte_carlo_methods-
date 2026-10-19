import numpy as np 
import matplotlib.pyplot as plt 


#parameters for the simulation  
L = 20 
m2 = -1 
lam = 6 
step_size = 1 

n_thermal  = 1000 
n_measures = 3000 

rng = np.random.default_rng(42) 

#initial field  

phi = rng.normal(0,0.1,size = (L,L)) 

def potential(x):
    return m2 /2 * np.abs(x)**2 + lam / 24 * np.abs(x)**4 



