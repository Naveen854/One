import numpy as np
import matplotlib.pyplot as plt
n=int(input("Enter the Length of Samples"))
x=[]
for i in range(n):
	z=int(input("Enter a samples"))
	x=np.append(x,z)
print(x)


lnx=n
y=np.zeros(lnx)
for i in range(lnx):
	if lnx-i>=0 and lnx-i<=lnx:
		y[i]=x[lnx-i-1]
print(y)
print("time revesal of x[n] is:",y)
plt.subplot(311)
plt.plot(n,x)
plt.title('Given signal')
plt.subplot(311)
plt.plot()
plt.title('DTFT of given signal')
plt.subplot(312)

