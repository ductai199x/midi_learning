#!/usr/bin/env python3

from scipy.io import wavfile
import numpy as np
from matplotlib import pyplot as plt

sample_rate, data = wavfile.read("ALREADY.wav")

# Get pulse:
pulse = []
a = 100
abs_data = np.abs(data)
for i in range (a, len(data)-a):
    pulse.append(np.mean(abs_data[i-a:i+a]))

pulse2 = []
for i in range (a, len(pulse)-a):
    pulse2.append(np.mean(pulse[i-a:i+a]))



fig1, ax1 = plt.subplots(3, 1)

ax1[0].plot(data, linestyle="", marker=".")
ax1[1].plot(pulse)
ax1[2].plot(pulse2)

plt.show()
