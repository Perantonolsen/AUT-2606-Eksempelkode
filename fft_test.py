#from scipy.fft import fft#,fftfreq
import nympy as np
import matplotlib.pyplot as plt
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N, endpoint=False)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = np.fft.fft(y)[0:int(N/2)]/N
yf[1:] = 2*yf[1:]
Pxx = np.abs(yf)
f = 

fig,ax = plt.subplots()
plt.plot(
plt.grid()
plt.show()
