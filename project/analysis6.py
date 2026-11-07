import matplotlib.pyplot as plt 
import pandas as pd 


df = pd.read_csv("./phi4_results.csv") 

beta = df.beta 
acceptance = df["acceptance"]


beta_l8_h0 = beta[0:14] 
acceptance_l8_h0 = acceptance[0:14] 

beta_l8_h1 = beta[15:29] 
acceptance_l8_h1 = acceptance[15:29] 

beta_l8_h2 = beta[30:44] 
acceptance_l8_h2 = acceptance[30:44] 

beta_l12_h0 = beta[45:59] 
acceptance_l12_h0 = acceptance[45:59] 

beta_l12_h1 = beta[60:74] 
acceptance_l12_h1 = acceptance[60:74] 

beta_l12_h2 = beta[75:89]
acceptance_l12_h2 = acceptance[75:89]

beta_l16_h0 = beta[90:104] 
acceptance_l16_h0 = acceptance[90:104] 

beta_l16_h1 = beta[105:119] 
acceptance_l16_h1 = acceptance[105:119] 

beta_l16_h2 = beta[120:136] 
acceptance_l16_h2 = acceptance[120:136] 

plt.plot(beta_l8_h0 , acceptance_l8_h0 , "o-" , label = "h=0") 
plt.plot(beta_l8_h1 , acceptance_l8_h1 , "o-" , label = "h=0.1") 
plt.plot(beta_l8_h2 , acceptance_l8_h2 , "o-" , label = "h=0.2") 
plt.legend(fontsize = 15) 
plt.ylabel("acceptance",fontsize = 15) 
plt.xlabel("beta" , fontsize = 15) 
plt.tick_params("both" ,labelsize = 15) 
plt.title("acceptance at h=0" , fontsize = 15)
plt.show() 


plt.plot(beta_l12_h0 , acceptance_l12_h0 , "o-" , label = "h=0") 
plt.plot(beta_l12_h1 , acceptance_l12_h1 , "o-" , label = "h=0.1") 
plt.plot(beta_l12_h2 , acceptance_l12_h2 , "o-" , label = "h=0.2") 
plt.legend(fontsize = 15) 
plt.ylabel("acceptance",fontsize = 15) 
plt.xlabel("beta" , fontsize = 15) 
plt.tick_params("both" ,labelsize = 15) 
plt.title("acceptance at h=0.1",fontsize = 15)
plt.show() 


plt.plot(beta_l16_h0 , acceptance_l16_h0 , "o-" , label = "h=0") 
plt.plot(beta_l16_h1 , acceptance_l16_h1 , "o-" , label = "h=0.1") 
plt.plot(beta_l16_h2 , acceptance_l16_h2 , "o-" , label = "h=0.2") 
plt.legend(fontsize = 15) 
plt.ylabel("acceptance",fontsize = 15) 
plt.xlabel("beta" , fontsize = 15) 
plt.tick_params("both" ,labelsize = 15) 
plt.title("acceptance at h=0.2" ,fontsize = 15)
plt.show() 
