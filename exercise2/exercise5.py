import numpy as np
import  matplotlib.pyplot as plt 

def mean_error(data): 
    N = len(data) 
    
    mean = np.mean(data) 
    error = np.std(data) / np.sqrt(N) 

    return mean , error 


def test_case(numbers): 
    print("uniformity test") 
    for k in range(1,5): 
        values = numbers**k 
        mean , error = mean_error(values) 
        theory = 1 / (k+1) 

        print(f"k = {k}",f"numerical : {mean:.5f} $\pm$ {error:.5f}" ,
              f"theory : {theory:.5f}") 

    print("independence  test") 

    x = numbers[0::2] 
    x_prime = numbers[1::2] 

    for k in range(1,5):  
        for kp in range(1,5): 
            values = x**k * x_prime**kp 
            mean , error = mean_error(values) 
            theory = 1/((k+1)*(kp+1)) 

            print(f"k:{k} , kp:{kp}" , 
                  f"numerical {mean:.5f} $\pm$ {error:.5f}" , 
                  f"theory : {theory:.5f}") 


def LCG(N,seed,a,m): 
    numbers = np.zeros(N) 

    x = seed 

    for i in range(N): 
        x = (a*x) % m 
        numbers[i] = x / m 

    return numbers 

def middle_square(N,seed,n=4): 
    numbers = np.zeros(N) 
    x = seed 
    for i in range(N): 
        squared = str(x*x).zfill(2*n) 
        x = int(squared[n//2 : 2*n-n//2] ) 
        numbers[i] = x / 10**n 
    return numbers 


N = 100000

rng1 = LCG(N, 12345, 1277, 2**17)
rng2 = LCG(N, 12345, 16807, 2**31 - 1)
rng3 = LCG(N, 12345, 48271, 2**31 - 1)
rng4 = middle_square(N,1234) 


generators = {"LCG 1277" : rng1 , 
              "LCG 16807 ": rng2 , 
              "LCG 48271" : rng3 , 
              "middle_square" : rng4 }  



for name , numbers in generators.items(): 
    print(f"\n{"_"*20}")
    print(name)
    print("_"*20)
    test_case(numbers) 


for name , numbers in generators.items(): 
    plt.hist(numbers , bins = 50 , density=True , alpha = 0.7 , edgecolor  = "black" , color = "green") 
    plt.axhline(1,color = "red" , linestyle = "dashed" , label = "uniform distribution") 
    plt.title(name)  
    plt.xlabel("x" , fontsize = 15) 
    plt.ylabel("probability density",fontsize = 15) 
    plt.legend(fontsize = 15)
    plt.tick_params("both" , labelsize = 15)
    plt.show() 
