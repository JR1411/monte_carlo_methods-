import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_csv("./phi4_results.csv") 


def critical_beta(df , h): 
    data = df[np.isclose(df["h"] ,h)].copy() 

    data["chi_abs"] = (data["chi_M"] - data["L"]**2 * (data["abs_M"]**2 - data["M"]**2)) 

    L_values = [] 
    beta_peaks = [] 

    for L , group in data.groupby("L") : 
        group = group.sort_values("beta") 
        idx = group["chi_abs"].idxmax()  

        if idx in (group.index[0] , group.index[-1]): 
            continue 

    beta_peak = group.loc[idx, "beta"] 

    L_values.append(L) 
    beta_peaks.append(beta_peak) 


    # Finite-size scaling: beta_peak = beta_c + a/L
    x = 1.0 / np.asarray(L_values) 
    a, beta_c = np.polyfit(x, beta_peaks, 1)

    plt.scatter(x, beta_peaks, label="Monte Carlo")

    x_fit = np.linspace(0, x.max(), 100)
    plt.plot(x_fit, beta_c + a*x_fit, label="Scaling fit")

    plt.xlabel(r"$1/L$" , fontsize = 15)
    plt.ylabel(r"$\beta_{\mathrm{peak}}$" , fontsize = 15)
    plt.legend(fontsize = 15)
    plt.grid(alpha=0.3) 
    plt.tick_params("both" , labelsize = 15) 
    plt.title(f"critical_beta = {beta_c:.5f}",fontsize = 15)
    plt.show()


    return beta_c 


h_vals = [0,0.1,0.2] 

critical_betas = np.array([critical_beta(df,h)for h in h_vals]) 

print(critical_betas) 
