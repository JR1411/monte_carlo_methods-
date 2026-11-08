import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("phi4_results.csv")

h = df["h"]
L = df["L"]
beta = df["beta"] 
M = df["M"] 
abs_M = df["abs_M"] 
chi_M = df["chi_M"] 
chi_A = df["chi_A"] 
binder = df["binder"] 
action_density = df["action_density"] 
acceptance = df["acceptance"] 


plt.plot(beta[0:14] , abs_M[0:14] ,"o-" ,label = "L=8") 
plt.plot(beta[15:29],abs_M[15:29],"o-",label = "L=12") 
plt.plot(beta[30:44] ,abs_M[30:44],"o-",label = "L=16") 
plt.legend(fontsize=15) 
plt.title("Magnetization at h=0 ",fontsize = 15) 
plt.xlabel(r"$\beta$" ,fontsize = 15) 
plt.ylabel("M",fontsize = 15) 
plt.tick_params("both",labelsize = 15) 
plt.show() 


plt.plot(beta[45:59] , abs_M[45:59] ,"o-" ,label = "L=8") 
plt.plot(beta[60:74],abs_M[60:74],"o-",label = "L=12") 
plt.plot(beta[75:89] ,abs_M[75:89],"o-",label = "L=16") 
plt.legend(fontsize=15) 
plt.title("Magnetization at h=0.1 ",fontsize = 15) 
plt.xlabel(r"$\beta$" ,fontsize = 15) 
plt.ylabel("M",fontsize = 15) 
plt.tick_params("both",labelsize = 15)
plt.show() 



plt.plot(beta[90:105] , abs_M[90:105] ,"o-" ,label = "L=8") 
plt.plot(beta[106:120],abs_M[106:120],"o-",label = "L=12") 
plt.plot(beta[121:136] ,abs_M[121:136],"o-",label = "L=16") 
plt.legend(fontsize=15) 
plt.title("Magnetization at h=0.2",fontsize = 15) 
plt.xlabel(r"$\beta$" ,fontsize = 15) 
plt.ylabel("M",fontsize = 15) 
plt.tick_params("both",labelsize = 15) 
plt.show() 
