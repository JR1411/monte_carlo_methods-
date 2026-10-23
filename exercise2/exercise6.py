import numpy as np 
import matplotlib.pyplot as plt 

def maxwell(x , a=1): 
    return np.sqrt(2  /np.pi) * x**2 / a**3 * np.exp(-x**2 / (2*a**2)) 


def rejection_sampling(N , rng= np.random.default_rng(42)): 
    C = 10 * maxwell(np.sqrt(2)) 
    samples = [] 
    accepted = 0 
    proposed = 0 

    while accepted < N : 
        x = rng.uniform(0,10,size = 1000000) 
        u =  rng.random(1000000) 

        mask = u < maxwell(x) / (C /10) 
        selected = x[mask] 
        samples.append(selected) 
        accepted += len(selected)
        proposed += len(x) 
    samples = np.concatenate(samples)[:N] 
    rejection_rate = 1 - accepted / proposed 
    return samples , rejection_rate 


x , rate = rejection_sampling(100000) 

x_values = 10 * np.linspace(0,1,1000)  


plt.hist(x , density=True , color = "green" , edgecolor = "black",bins=100) 
plt.plot(x_values , maxwell(x_values)) 
plt.show() 
