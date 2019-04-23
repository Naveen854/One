import numpy as np
import matplotlib.pyplot as plt
x=input('Enter the samples of signal1 in array format ;')
h=x[::-1]
print h
l=len(x)
m=len(h)
y=np.zeros(2*l-1)
for i in range(l):
		for j in range(m):
			y[i+j]=y[i+j]+x[i]*h[j]
print y
plt.subplot('311')
plt.stem(x)
plt.title('Signal 1')
plt.subplot('312')
plt.stem(h)
plt.title('Signal 2')
plt.subplot('313')
plt.stem(y)
plt.title('Auto corelation of signal1')
plt.show()
