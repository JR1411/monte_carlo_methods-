import numpy as np 
import matplotlib.pyplot as plt 


height_sample = np.random.normal(170 , 25 , 100_000_000) 
sub_sample = np.random.choice(height_sample , 100_000) 

height_list = [] 

for i in range(1,10000): 
    sample = np.random.choice(sub_sample , 10000) 
    sample_average = np.average(sample) 
    height_list.append(sample_average) 

average_height = np.average(height_list) 

print(f"({average_height:.2f} $\pm$ {np.std(height_list):.2f}) [cm]") 


plt.hist(height_list , edgecolor = "black" , bins = 50 ,color = "green") 
plt.tick_params("both" , labelsize = 15) 
plt.xlabel("height [cm]",fontsize = 15) 
plt.ylabel("values [1]" , fontsize = 15)
plt.show() 
