import numpy as np 
import random 
import matplotlib.pyplot as plt 

N_samples = np.arange(100000)
n_steps = 20 

def random_walk(n): 
    x , y = 0 , 0 
    for i in range(n): 
        (dx,dy) = random.choice([(0,1) , (0,-1) , (1,0) , (-1,0)]) 
        x += dx 
        y += dy 

    return (x,y)


lengths = [] 

for i in N_samples: 
    walk = random_walk(n_steps) 
    distance = abs(walk[0]) + abs(walk[1]) 
    lengths.append(distance) 



print("backtracking possible")
print(f"average length : {np.average(lengths)}") 
print(f"maximum length : {np.max(lengths)}") 

def random_walk_no_back(n): 
    x , y = 0 , 0 
    steps_x = [] 
    steps_y = [] 

    choices = [0,1,-1] 

    for i in range(n): 
        dx = random.choice(choices) 
        steps_x.append(dx) 

        dy = random.choice(choices) 
        steps_y.append(dy) 

    for i in range(n): 
        if steps_x[i] == -steps_x[i-1]: 
            steps_x[i] = 0 
        elif steps_y[i] == -steps_y[i-1]: 
            steps_y[i] = 0

    x = x + np.sum(steps_x) 
    y = y + np.sum(steps_y) 

    return (x,y) 


lengths_no = [] 

for i in N_samples: 
    walk = random_walk_no_back(n_steps) 
    space = abs(walk[0]) + abs(walk[1]) 
    lengths_no.append(space) 

print("no back-tracking")
print(f"average distance : {np.average(lengths_no)}")
print(f"maximum distance : {np.max(lengths_no)}") 

plt.hist(lengths_no  , density=True , bins = n_steps , label = "backtracking")
plt.hist(lengths ,density=True ,alpha = 0.6 , bins=n_steps , label = "no-backtracking") 
plt.legend(fontsize = 15 , ncol = 2) 
plt.xlabel("lengths" , fontsize = 15) 
plt.ylabel("probability" , fontsize = 15) 
plt.tick_params("both" , labelsize = 15)
plt.show() 
