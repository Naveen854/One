import numpy as np
from matplotlib import pyplot as plt
t=np.linspace(0,0.01,100)
n=np.linspace(-10,10,20)
f=input('Enter the input Frequecy(Hz) ;')
f=np.float(f)
fs=input('Enter the Samping Rate(Hz) ;')
fs=np.float(fs)

x=np.sin(2*np.pi*(f/fs)*n)
plt.subplot(244)
plt.stem(n,x)
plt.show()

p=input('Enter the current sample value ;')
s=0
i=0
for i in range(p):
	s=s+x[i]
	print('sum of first %d sample is : %f'%(i,s))
	
print('Accumulator value is : %f'%(s))

