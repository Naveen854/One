import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
f=input('Enter the frquency ;')
p=input('Enter the Order of Moving Average System')
t=np.linspace(0,0.01,300)
x1=np.sin(2*np.pi*f*t)								
N=np.random.rand(x1.shape[0])
m=x1+N
y=[];
for i in range(300):
	c=0
	d=p
	if(i<p):
		d=i
	for k in range(0,d+1):
			c=c+m[i-k]
	y.append((c)/p)
print y
plt.subplot(411)
plt.plot(t,x1)
plt.title('Sine Wave')
plt.subplot(412)
plt.plot(t,N)
plt.title('Noise ')
plt.subplot(413)
plt.plot(t,m)
plt.title('Noise Added Signal ')
plt.subplot(414)
plt.plot(t,y)
plt.title('Output Response of Moving Average System ')
plt.show()
