import numpy as np 
import matplotlib.pyplot as plt 


L = 20 
m1 = -1 
LAM = 6 
rng = np.random.default_rng(42)

def potential(phi,h): 
    return h * phi + m1 * 0.5 * phi**2 + LAM/24 * phi**4 


def action(phi , beta , h ): 
    dx = phi - np.roll(phi , -1 ) 
    dy = phi - np.roll(phi , -1 ) 

    kinetic = np.sum(dx**2 + dy**2) / 2 
    interaction = np.sum(potential(phi ,h)) 

    return kinetic + interaction 

def metropolis_sweep(phi , beta , h , step): 
    accepted = 0 

    for _ in range(L**2): 
        i = rng.integers(L) 
        j = rng.integers(L) 

    old = phi[i,j] 
    new = old + rng.uniform(-step , step) 
    
    neighbors = (
        phi[(i+1)%L , j ] + 
        phi[(i-1)%L , j ] + 
        phi[i,(j+1)%L] + 
        phi[i , (j-1)%L] 
    )


    delta_kinetic = (
        2 * (new**2 - old**2 ) - (new -old)*neighbors
    )

    delta_S = beta * (delta_kinetic + potential(new , h ) - potential(old ,h)) 

    if delta_S <= 0 or rng.random() < np.exp(-delta_S) : 
        phi[i,j] = new 
        accepted += 1

    return accepted / L**2 



def simulate(L,beta,h , thermal = 1500 , measurements = 1000 , thin = 5  ): 
    phi = rng.normal(0 , 0.5 , (L,L)) 
    step = 1 

    for sweep in range(thermal): 
        acceptance = metropolis_sweep(phi , beta , h , step) 

        if sweep < thermal//2 : 
            if acceptance > 0.55 : 
                step *= 1.01 
            elif acceptance < 0.45 : 
                step *= 0.99 

    magnetization = [] 
    actions = [] 
    acceptance_rates = [] 

    for _ in range(measurements): 
        rates = [] 

        for _ in range(thin): 
            rates.append(metropolis_sweep(phi , beta , h , step)) 


        magnetization.append(np.mean(phi)) 
        actions.append(action(phi,beta,h)/L**2) 
        acceptance_rates.append(np.mean(rates)) 


    M = np.asarray(magnetization)
    A = np.asarray(actions) 

    mean_m = np.mean(M) 
    mean_abs_m = np.mean(abs(M)) 

    chi_m = L**2 * (np.mean(M**2) - np.mean(M)**2 ) 
    chi_a = L**2 * (np.mean(A**2) - np.mean(A)**2) 

    binder = 1 - np.mean(M**4)/(3 * np.mean(M**2)**2) 
    
    action_density = np.mean(A) 
    acceptance = np.mean(acceptance_rates)

    return M , A , mean_m , mean_abs_m , chi_m , chi_a , binder , acceptance , action_density


def scan(betas ,sizes , fields): 
    results = {} 

    for h in fields: 
        for L in sizes : 
            measurements = [] 

            for beta in betas: 
                results = simulate(L,beta,h) 
                measurements.append(results) 

        results = measurements


    return measurements 


betas = np.arange(0.1 , 1 , 0.1) 
sizes = [20] 
fields = [0 , 0.1 ,0.2] 

results = scan(betas,sizes,fields) 


