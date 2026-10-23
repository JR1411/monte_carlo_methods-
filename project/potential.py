import numpy as np 
import matplotlib.pyplot as plt 


def potential(x): 
    return - x**2 / 2 + (6/24)* x**4 


x_values = 2 * np.linspace(-1,1,1000) 

potential_curve = potential(x_values) 


plt.plot(x_values , potential_curve ) 
plt.show() 
