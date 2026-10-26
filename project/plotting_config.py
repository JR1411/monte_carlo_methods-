import matplotlib.pyplot as plt 
from project_code import magnetization , acceptance , phi 



fig, ax = plt.subplots(1, 2, figsize=(10, 5))

im = ax[0].imshow(phi, cmap="plasma")
ax[0].set_title("final field configurations")
plt.colorbar(im, ax=ax[0], label="phi")


ax[1].plot(magnetization)
ax[1].set_xlabel("metropolis sweep", fontsize=15)
ax[1].set_ylabel("mean field", fontsize=15)
ax[1].set_title("Field evolution")

plt.tight_layout()
plt.show() 

