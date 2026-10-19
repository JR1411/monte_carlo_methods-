import numpy as np 
import matplotlib.pyplot as plt 


N = 100_000 
n = 100_00 
I_array = [] 

x_sample = np.random.uniform(0,1,N) 
y_sample = np.random.uniform(0,1,N) 
z_sample = np.random.uniform(0,1,N) 


for i in range(1 , 1000): 
    x = np.random.choice(x_sample , n) 
    y= np.random.choice(y_sample , n) 
    z = np.random.choice(z_sample , n) 


    func = (1-0)**3 * 1/(np.exp(3 * x**2 + 2 * y - z)) 
    func_average = np.average(func) 
    I_array.append(func_average) 


solution = np.average(I_array) 

error = np.std(I_array) 

print(f"integral = {solution:.4f} $\pm$ {error:.4f}") 

plt.hist(I_array , density=True , color = "green" , edgecolor = "black",bins=25) 
plt.tick_params("both",labelsize=15)
plt.show() 
