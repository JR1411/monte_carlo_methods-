import matplotlib.pyplot as plt 
import pandas as pd 


df = pd.read_csv("./phi4_results.csv") 

chi_M = df["chi_M"] 
beta = df["beta"] 

plt.plot(beta[0:14],chi_M[0:14],"o-",label = "L=8") 
plt.plot(beta[15:29],chi_M[15:29],"o-",label = "L=12") 
plt.plot(beta[30:44],chi_M[30:44],"o-",label = "L=16") 
plt.legend(fontsize = 15) 
plt.title(r"Susceptibility $\chi_M$ at h=0",fontsize =15) 
plt.xlabel(r"$\beta$", fontsize = 15) 
plt.ylabel(r"$\chi_M$",fontsize = 15) 
plt.tick_params("both" , labelsize = 15) 
plt.savefig("sus_h0.jpeg")
plt.show() 

plt.plot(beta[45:59],chi_M[45:59],"o-",label = "L=8") 
plt.plot(beta[60:74],chi_M[60:74],"o-",label = "L=12") 
plt.plot(beta[75:89],chi_M[75:89],"o-",label = "L=16") 
plt.legend(fontsize = 15) 
plt.title(r"Susceptibility $\chi_M$ at h=0.1",fontsize =15) 
plt.xlabel(r"$\beta$", fontsize = 15) 
plt.ylabel(r"$\chi_M$",fontsize = 15) 
plt.tick_params("both" , labelsize = 15) 
plt.savefig("sus_h1.jpeg")
plt.show() 

plt.plot(beta[91:105],chi_M[91:105],"o-",label = "L=8") 
plt.plot(beta[106:120],chi_M[106:120],"o-",label = "L=12") 
plt.plot(beta[121:136],chi_M[121:136],"o-",label = "L=16") 
plt.legend(fontsize = 15) 
plt.title(r"Susceptibility $\chi_M$ at h=0.2",fontsize =15) 
plt.xlabel(r"$\beta$", fontsize = 15) 
plt.ylabel(r"$\chi_M$",fontsize = 15) 
plt.tick_params("both" , labelsize = 15) 
plt.savefig("sus_h2.jpeg")
plt.show() 
