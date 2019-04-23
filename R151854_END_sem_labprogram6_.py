import numpy as np 
import matplotlib.pyplot as plt 
data = np.loadtxt('/home/rgukt/Desktop/DSP_lab_end_sem/radar.txt',skiprows=0)  
print data

x=data
print x
l=len(x)
print l
N=np.random.rand(x.shape[0])
n0=input('Enter the n0 delay ;');
y1=np.roll(x,n0)+N
print y1
m=len(y1)
h=y1[::-1]
y=np.zeros(m+l-1)
for i in range(l):
		for j in range(m):
			y[i+j]=y[i+j]+x[i]*h[j]
print y

plt.subplot('311')
plt.stem(x)
plt.title('Radar Signal')
plt.subplot('312')
plt.stem(h)
plt.title('Reflected Signal')
plt.subplot('313')
plt.stem(y)
plt.title('Convoluton of Radar signals & Reflected Signal')
plt.show()

