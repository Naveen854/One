# it's a python program to plot voice
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

[fs,data]=wav.read("/home/rgukt/me1.wav")
fs=np.float(fs)
t=np.arange(0,len(data)/fs,1/fs)
print(fs,len(data),data)
plt.plot(t,data)
plt.show()
wav.write("compressed.wav",0.5*fs,data)
wav.write("expanded.wav",2*fs,data)

