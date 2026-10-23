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

def stats(x): 
    mean = np.mean(x) 
    var = np.var(x) 

    skew = np.mean((x-mean)**3 / var**1.5) 

    return mean , var , skew 



x_values = 10 * np.linspace(0,1,1000)


N = 10**6 
M = 50 

results = np.zeros((M,3)) 

for i in range(M): 
    x , rate = rejection_sampling(N) 
    results[i] = stats(x) 

means = np.mean(results , axis=0) 
error = np.std(results,axis=0) / np.sqrt(M) 

theory = np.array([2 * np.sqrt(2 / np.pi),(3*np.pi - 8) / np.pi,2*np.sqrt(2)*(16 - 5*np.pi) / (3*np.pi - 8)**1.5])

names = ["Mean" , "Variance" , "Skewness"] 

for i , name in enumerate(names): 
    print(f"{name}: {means[i]:.6f} ± {error[i]:.6f}"f" | Theory: {theory[i]:.6f}")

plt.hist(x , density=True , color = "green" , edgecolor = "black",bins=100,label = "random values") 
plt.plot(x_values , maxwell(x_values) , color = "red" , label = "theory") 
plt.legend(fontsize = 15) 
plt.xlabel("x" , fontsize = 15) 
plt.ylabel("y" , fontsize = 15) 
plt.tick_params("both" , labelsize = 15)
plt.show() 
