import numpy as np 


def estimate(N = 1000000): 
    points = np.random.uniform(-1,1,size = (N,10)) 

    rsquared = np.sum(points**2 , axis = 1) 
    N_inside = np.sum(rsquared <= 1) 
    V10 = N_inside/N * 2**10 
    pi_estimate = (V10 * 120)**(1/5) 

    return pi_estimate 


pi = estimate() 
print(pi)
