import matplotlib.pyplot as plt 
import pandas as pd 


df = pd.read_csv("./phi4_results.csv") 

beta = df["beta"] 
binder = df["binder"] 


plt.plot(beta[0:14] , binder[0:14] , "o-" , label = "L=8") 
plt.plot(beta[15:29] , binder[15:29],"o-",label = "L=12") 
plt.plot(beta[30:44] , binder[30:44],"o-" ,label = "L=16") 
plt.legend(fontsize = 15) 
plt.xlabel(r"$\beta$" , fontsize = 15)
plt.ylabel("binder",fontsize = 15) 
plt.title("binder at h=0",fontsize=15) 
plt.tick_params("both",labelsize = 15) 
plt.show() 

plt.plot(beta[45:59] , binder[45:59] , "o-" , label = "L=8") 
plt.plot(beta[60:74] , binder[60:74],"o-",label = "L=12") 
plt.plot(beta[75:89] , binder[75:89],"o-" ,label = "L=16") 
plt.legend(fontsize = 15) 
plt.xlabel(r"$\beta$" , fontsize = 15)
plt.ylabel("binder",fontsize = 15) 
plt.title("binder at h=0.1",fontsize=15) 
plt.tick_params("both",labelsize = 15) 
plt.show() 

plt.plot(beta[90:104] , binder[90:104] , "o-" , label = "L=8") 
plt.plot(beta[105:119] , binder[105:119],"o-",label = "L=12") 
plt.plot(beta[120:136] , binder[120:136],"o-" ,label = "L=16") 
plt.legend(fontsize = 15) 
plt.xlabel(r"$\beta$" , fontsize = 15)
plt.ylabel("binder",fontsize = 15) 
plt.title("binder at h=0.2",fontsize=15) 
plt.tick_params("both",labelsize = 15) 
plt.show() 

