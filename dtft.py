import numpy as np
from matplotlib import pyplot as plt
import cmath as cm
w=np.linspace(-np.pi,np.pi,1000)
x=input('Enter the Sequence')
l=len(x)
n=0
j=cm.sqrt(-1)
X_w=0
for n in range(l):
    X_w+=(x[n]*np.exp(-j*w*n))
X_mgtd=np.abs(X_w)
X_phase=np.angle(X_w)
plt.subplot(311)
plt.plot(w,X_w)
plt.title('DTFT of given signal')
plt.subplot(312)
plt.plot(w,X_mgtd)
plt.title('Magnitude Spectrum')
plt.subplot(313)
plt.plot(w,X_phase)
plt.title('Phase Spectrum')
plt.show()
