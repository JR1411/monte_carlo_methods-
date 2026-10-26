import numpy as np 
import matplotlib.pyplot as plt 
from project_code import magnetization , acceptance , L 

acceptance = np.asarray(acceptance)

chi_M = L**2 * (np.mean(magnetization**2) - np.mean(magnetization)**2) 
chi_A = L**2 * (np.mean(acceptance**2) - np.mean(acceptance)**2) 


plt.plot(chi_M)
plt.show() 
