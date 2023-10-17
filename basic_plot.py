#import os
import numpy as np
from matplotlib import pyplot as plt

t = np.linspace(0,np.pi,1000)
x = np.cos(t)


plt.plot(t,x)
#plt.savefig('testplot.png')
#Image.open('testplot.png').save('testplot.jpg','JPEG')
plt.show(block=True)
