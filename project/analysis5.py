import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_csv("./phi4_results.csv") 

beta = df.beta 
chi = df.chi_M 


beta_L8_h0 = beta[0:14] 
chi_L8_h0 = chi[0:14] 

beta_L8_h1 = beta[45:59] 
chi_L8_h1 = chi[45:59] 

beta_L8_h2 = beta[90:104] 
chi_L8_h2 = chi[90:104] 

plt.plot(beta_L8_h0 , chi_L8_h0 , "o-" , label = "h=0") 
plt.plot(beta_L8_h1 , chi_L8_h1 , "o-" , label = "h=0.1") 
plt.plot(beta_L8_h2 , chi_L8_h2 , "o-" , label = "h=0.2") 
plt.legend(fontsize = 15) 
plt.xlabel(r"$\beta$" , fontsize = 15) 
plt.ylabel(r"$\chi$" , fontsize = 15) 
plt.title(r"$\chi_M$ at L=8",fontsize = 15) 
plt.tick_params("both",labelsize = 15) 
plt.show() 


beta_L12_h0 = beta[15:29] 
chi_L12_h0 = chi[15:29] 

beta_L12_h1 = beta[60:74] 
chi_L12_h1 = chi[60:74] 

beta_L12_h2 = beta[105:119] 
chi_L12_h2 = chi[105:119] 

plt.plot(beta_L12_h0 , chi_L12_h0 , "o-" , label = "h=0") 
plt.plot(beta_L12_h1 , chi_L12_h1 , "o-" , label = "h=0.1") 
plt.plot(beta_L12_h2 , chi_L12_h2 , "o-" ,label ="h=0.2")
plt.legend(fontsize = 15) 
plt.xlabel(r"$\beta$" , fontsize = 15) 
plt.ylabel(r"$\chi$" , fontsize = 15) 
plt.title(r"$\chi_M$ at L=12",fontsize = 15) 
plt.tick_params("both",labelsize = 15) 
plt.show() 


beta_L16_h0 = beta[30:45] 
chi_L16_h0 = chi[30:45] 

beta_L16_h1 = beta[75:89] 
chi_L16_h1 = chi[75:89] 

beta_L16_h2 = beta[120:136] 
chi_L16_h2 = chi[120:136] 


plt.plot(beta_L16_h0 , chi_L16_h0 , "o-" , label = "h=0") 
plt.plot(beta_L16_h1 , chi_L16_h1 , "o-" , label = "h=0.1") 
plt.plot(beta_L16_h2 , chi_L16_h2 , "o-" ,label ="h=0.2")
plt.legend(fontsize = 15) 
plt.xlabel(r"$\beta$" , fontsize = 15) 
plt.ylabel(r"$\chi$" , fontsize = 15) 
plt.title(r"$\chi_M$ at L=16",fontsize = 15) 
plt.tick_params("both",labelsize = 15) 
plt.show() 


