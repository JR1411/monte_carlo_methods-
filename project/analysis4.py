import matplotlib.pyplot as plt 
import pandas as pd 


df = pd.read_csv("./phi4_results.csv") 

beta = df.beta 
actions_density = df.action_density 

plt.plot(beta[0:14] , actions_density[0:14] , "o-" , label = "L=8") 
plt.plot(beta[15:29],actions_density[15:29] , "o-" ,label = "L=12") 
plt.plot(beta[30:44] , actions_density[30:44] , "o-",label="L=16") 
plt.legend(fontsize = 15) 
plt.xlabel(r"$\beta$",fontsize = 15)
plt.ylabel(r"$\frac{\langle S \rangle}{L^2}$",fontsize = 15) 
plt.tick_params("both" ,labelsize = 15) 
plt.title(r"action density $\frac{\langle S \rangle}{L^2}$ at h=0" , fontsize = 20)
plt.show()



plt.plot(beta[45:59] , actions_density[45:59] , "o-" , label = "L=8") 
plt.plot(beta[60:74],actions_density[60:74] , "o-" ,label = "L=12") 
plt.plot(beta[75:89] , actions_density[75:89] , "o-",label="L=16") 
plt.legend(fontsize = 15) 
plt.xlabel(r"$\beta$",fontsize = 15)
plt.ylabel(r"$\frac{\langle S \rangle}{L^2}$",fontsize = 15) 
plt.tick_params("both" ,labelsize = 15) 
plt.title(r"action density $\frac{\langle S \rangle}{L^2}$ at h=0.1" , fontsize = 20)
plt.show()


plt.plot(beta[90:104] , actions_density[90:104] , "o-" , label = "L=8") 
plt.plot(beta[105:119],actions_density[105:119] , "o-" ,label = "L=12") 
plt.plot(beta[120:136] , actions_density[120:136] , "o-",label="L=16") 
plt.legend(fontsize = 15) 
plt.xlabel(r"$\beta$",fontsize = 15)
plt.ylabel(r"$\frac{\langle S \rangle}{L^2}$",fontsize = 15) 
plt.tick_params("both" ,labelsize = 15) 
plt.title(r"action density $\frac{\langle S \rangle}{L^2}$ at h=0.2" , fontsize = 20)
plt.show()
