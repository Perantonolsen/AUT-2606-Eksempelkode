import numpy as np
from matplotlib import pyplot as plt
#from scipy.stats import gamma
from math import gamma



def RiemannLiouvilleIntegral(order,time_arr,funct_arr):
	s = 0
	arr = np.zeros(len(time_arr))
	dt= time_arr[1]
	print(gamma(order))
	for i in range(len(time_arr)):
		s += (time_arr[-1]-time_arr[i])**(order-1)*funct_arr[i]*dt
		arr[i] = s*1/gamma(order) 
	s*= 1/gamma(order)
	return s, arr




if __name__ == '__main__':
	t = np.linspace(0,2*np.pi,1000)
	f = np.sin(t)
	s1, arr1 = RiemannLiouvilleIntegral(2,t,f)
	s2, arr2 = RiemannLiouvilleIntegral(0.9,t,f)
	s3, arr3 = RiemannLiouvilleIntegral(1.5,t,f)
	plt.plot(t,f,"b-",t,arr1,"r-.",t,arr2,"g-",t,arr3,"r-")
	plt.show()
	input()
