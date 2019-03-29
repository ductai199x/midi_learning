#!/usr/bin/env python3

import mido
from music21 import *

from matplotlib import pyplot as plt
import numpy as np

infile = mido.MidiFile("./midi/test.mid")

track_v_note = {}
for i, track in enumerate(infile.tracks):
    print("Track {}: {}".format(i, track))
    track_v_note[i] = []
    for msg in track:
        if msg.type == "note_on" and msg.time > 0 and msg.velocity > 0:
            track_v_note[i].append(msg)

# Extract one major track
outfile = mido.MidiFile()
t = mido.MidiTrack()
outfile.tracks.append(t)

track_len = 0
freq_arr = []
veloc_arr = []

# (a / 32) * (2 ** ((note - 9) / 12))
g = 2**(1/12)
f = lambda note: 440*g**(note-69)
tempo = 500000  # micro sec/beat (120 bpm)
ticks_per_beat = 480
for n in track_v_note[2]:
    track_len += n.time
    freq_arr.extend([f(n.note)]*n.time)
    veloc_arr.extend([n.velocity]*n.time)
    t.append(n)

# Save the extracted file
outfile.save("./midi/extract.mid")

# Get the time axes
tick_arr = [i for i in range(0, track_len) ]

# Doing some fft
from scipy.fftpack import fft
# Normalize data:
norm_freq = [ (e/f(127))*2-1 for e in freq_arr ] # Midi is 8 bit track, normalizing between -1 and 1
fft_freq = fft(norm_freq)

# Plotting
fig1, ax1 = plt.subplots(nrows=2, ncols=2, constrained_layout=True)
ax1[0, 0].plot(tick_arr, freq_arr)
ax1[0, 1].plot(tick_arr, veloc_arr)
#ax1[1, 0].plot(fft_freq[1:len(fft_freq)//2-1])
ax1[1, 0].plot(fft_freq[1:])




plt.show()
