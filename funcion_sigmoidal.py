import matplotlib.pyplot as plt
import numpy as np
import math

x=np.linspace(-10,10,100)
z=1/(1+np.exp(-x))

plt.plot(x,z)
plt.title('Funcion sigmoidal')
plt.xlabel("x")
plt.ylabel("Sigmoidal(x)")
plt.legend()
plt.grid()

plt.show()