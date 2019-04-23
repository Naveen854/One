import cmath as cm
import numpy as np
import matplotlib.pyplot as plt
def iexp(n):
    return complex(math.cos(n), math.sin(n))
def dft(x,n):
	j=cm.sqrt(-1)
	n=a
	for i in range(a):
		sum=0;
		for m in range(a):
			sum+=sum+x[m]*exp(-1*2*np.pi*i*m/float(N))
	return sum
def timeshift(l,xs):
	n=len(xs)
	m=l
	x=[]
	for i in range(n+l):
		if (m+i > n):
			for k in range(n-m+i):
				x[k]=x[i]
		x[i+l]=xs[i]
	return x	
				
	            
            
q=0;            
x=input('Enter the First Sequence ;')
N=input('Enter the order to fin N-point DFT')
z=len(x)
if z<N:
	q=N-z
x=np.append(x,np.zeros(q))
n=input("enter number of shift")
c=len(x)
print c
x1=[]
for i in range(c):
	a=x[(c+i-n)%N]
	x1.append(a)
print x1
y1=dft(x,N)
y2=dft(x1,N)
k=np.arange(0,N)
R=[]
for i in  k:
	a=P[i]*np.exp(-1*2*np.pi*1j*i*n/np.float(N))
R.append(a)
y11=(np.abs(y1))
y12=(np.angle(y1))
#print P1
r11=(np.abs(R))
r12=(np.angle(R))
plt.subplot(511)
plt.plot(y11)
plt.subplot(512)
plt.plot(y12)
plt.subplot(513)
plt.plot(r11)
plt.subplot(514)
plt.plot(r12)
plt.show()
