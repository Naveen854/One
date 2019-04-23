import math
import cmath as cm
import numpy as np
import matplotlib.pyplot as plt
def dft(x,n):
    j=cm.sqrt(-1)
    for i in range(n):
    		sum=0;
    		for l in range(n):
        		sum=sum+x[l]*np.exp(-1*1j*2*np.pi*i*l/np.float(N))
    			Xk=np.append(Xk,sum)
    return 
def zeroadd(x,n):
	l=len(x)
	if(l == n):
		return x
	j=n-l
	for i in range(j+1):
	    x.append(0)
	return x

def add(x,y):
	l=len(x)
	s=np.zeros(l)
        for i in range(l):
        	s[i]=x[i]+y[i]	
        return s
      	  
                        
mx=input('Enter the First Sequence ;')
my=input('Enter the Second Sequence ;')
N=input('Enter the N-point to find DFT ;')
x1=zeroadd(mx,N)
print x1
x2=zeroadd(my,N)
print x2	
X1_k=dft(x1,N)
print X1_k
X2_k=dft(x2,N)
print X2_k
x3=add(x1,x2)
print x3
X3_k=dft(x3,N)
print X3_k

x6=add(X1_k,X2_k)
print x6

plt.subplot(331)
plt.stem(x1)
plt.subplot(332)
plt.stem(x2)
plt.subplot(333)
plt.stem(x3)
plt.subplot(334)
plt.stem(X1_k)
plt.subplot(335)
plt.stem(X2_k)
plt.subplot(336)
plt.stem(X3_k)
plt.show()
