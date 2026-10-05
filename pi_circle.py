import numpy as np 
import matplotlib.pyplot as plt 

N_samples = np.arange(1,100_000) 
pi_array = [] 
pi_counter = 0 

dots_x = [] 
dots_y = [] 
dotcolor = [] 

def plot_struct():
    fig , ax = plt.subplots(1,2,figsize = (10,5)) 
    ax[0].set_aspect("equal") 
    ax[0].set_xlim([0,1]) 
    ax[0].set_ylim([0,1]) 
    phi = np.linspace(0 , np.pi , 200 , endpoint=False) 
    ax[0].plot(np.cos(phi) , np.sin(phi) ,color = "black") 
    ax[0].set_xlabel("x" , fontsize = 15) 
    ax[0].set_ylabel("y" , fontsize = 15) 
    ax[0].tick_params("both" , labelsize = 15)
    
    ax[1].grid() 
    ax[1].set_xlim([0,N_samples.max() ]) 
    ax[1].set_ylim([2,4]) 
    ax[1].axhline(np.pi , 0 , N_samples.max() , color = "red",label = r"$\pi$") 
    ax[1].set_xlabel(r"$N_i$" , fontsize = 15)
    ax[1].set_ylabel("pi approx" , fontsize = 15 ) 
    ax[1].tick_params("both" , labelsize = 15)

    return ax 

ax =  plot_struct() 

for n in N_samples: 
    x = np.random.uniform(0,1) 
    y = np.random.uniform(0,1) 

    dots_x.append(x) 
    dots_y.append(y) 

    if np.sqrt(x**2 + y**2 ) <= 1 : 
        pi_counter += 1 
        dotcolor.append("blue") 

    else : 
        dotcolor.append("red") 

    probability = pi_counter / n 
    pi_approx = 4 * probability 
    pi_array.append(pi_approx) 

print(pi_array[::10000])

ax[1].set_title(f"{pi_array[-1]}") 
ax[0].scatter(dots_x , dots_y , color = dotcolor , marker  ="o" , s = 5 ) 
ax[1].plot(pi_array , color = "black",label = "approx pi")
plt.legend(fontsize = 15 , ncol = 2 ) 
plt.show() 
