import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
def dft(x,n):
	j=cm.sqrt(-1)
	n=a
	for i in range(a):
		sum=0;
		for m in range(a):
			sum+=sum+x[m]*exp(-1*2*np.pi*i*m/float(N))
			
X=input('Enter the Sequence')
N=len(X)
p=N-1
m=5
l=N+m
Y=[]
while(N<l):
	X.append(0)
	N=N+1
Y.append(X)
print(Y)
j=cm.sqrt(-1)
n=np.arange(0,p,1)
k=np.arange(0,p,1)
c=0
y1=[]
for k in range(p):
	for n in range(p):
		c=c+(X[n]*np.exp((-(j*2*np.pi*k*n/N))))
	y1.append(c)
	c=0
print(y1)
mag=np.abs(y1)
ph=np.angle(y1)
plt.subplot(4,1,1)
plt.stem(mag)
plt.subplot(4,1,2)
plt.stem(ph)
plt.subplot(4,1,3)
plt.stem(y1)
plt.subplot(4,1,4)
plt.stem(X)
plt.show()
