import  numpy as np
from numpy._core.multiarray import error

def mean_error(data): 
    N = len(data) 

    mean = np.mean(data) 
    error = np.std(data) / np.sqrt(N) 
    return mean , error 


rng = np.random.default_rng(42) 


N = 1000000 

numbers = rng.random(N * 2) 

x = numbers[0::2]  
x_prime = numbers[1::2] 

for k in range(1,5): 
    for kp in range(1,5) : 
        values = x**k * x_prime**kp 

        mean ,error = mean_error(values) 

        theory = (1 / (k+1)) * (1/(kp+1)) 



        print(f"k : {k} , kp : {kp}") 
        print(f"numerical : {mean:.5f} $\pm$ {error:.5f}") 
        print(f"theory : {theory:.5f}")

