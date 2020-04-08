import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(0, 8*np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)
plt.xlabel("Values from 0 to 8pi")
plt.ylabel("sin(x) & cos(x)")
plt.title("Plot of sin(x) & cos(x)")
plt.plot(x,y,x,z)
plt.show()


