from re import error
import numpy as np 


def mean_error(data): 
    N = len(data) 

    mean = np.mean(data)
    error = np.std(data) / np.sqrt(N) 

    return mean , error 

N = 1000000 

rng = np.random.default_rng(42) 

x = rng.random(N) 

for k in range(1,5): 
    values = x**k 

    mean , error = mean_error(values) 
    theoret = 1 / (k+1) 

    print(f"{k}")
    print(f"Numerical = {mean:.4f} $\pm$ {error:.4f}")
    print(f"theoretical = {theoret:.4f}") 
