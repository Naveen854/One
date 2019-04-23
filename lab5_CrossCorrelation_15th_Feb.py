#it is a program to implement convolution of Two signals

import numpy as np
import matplotlib.pyplot as plt
x=input('Enter the samples of signal1 in array format ;')
z=input('Enter the samples of signal2 in array format ;')
l=len(x)
m=len(z)
h=z[::-1]
y=np.zeros(m+l-1)
for i in range(l):
		for j in range(m):
			y[i+j]=y[i+j]+x[i]*h[j]
print y

plt.subplot('311')
plt.stem(x)
plt.title('Signal 1')
plt.subplot('312')
plt.stem(h)
plt.title('Signal 1')
plt.subplot('313')
plt.stem(y)
plt.title('Convoluton of signals 1 & 2')
plt.show()
