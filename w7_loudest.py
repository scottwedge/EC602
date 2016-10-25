# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w7_dialer.py
10/24/16
Siggi&John
"""
# Support for sound is provided 
# in a number of modules. Some
# are part of the standard library,
# but others are not. Everything we 
# use is part of the Anaconda distribution
# of python.

# WAV file support
import scipy.io.wavfile as wavfile
import PyQt4.QtGui as qt
import time
import numpy as np
import matplotlib.pyplot as pyplot

def read_wave(fname,debug=False):
    "return information about and time signal in the WAV file fname"
    frame_rate,music = wavfile.read(fname)
    if debug:
        print(frame_rate,type(music),music.shape,music.ndim)
    if music.ndim>1:
        nframes,nchannels = music.shape
    else:
        nchannels = 1
        nframes = music.shape[0]    
    return music,frame_rate,nframes,nchannels

def wavplay(fname):
    "play a sound, and sleep until it is finished"
    qt.QSound.play(fname)
    music,frame_rate,nframes,nchannels = read_wave(fname)
    time.sleep(nframes/frame_rate)

def loudest_band(music,frame_rate,bandwidth):
    #generate two tone signal

    w = np.fft.fft(music)
    freqs = np.fft.fftfreq(len(music))  
    fs = frame_rate
    hz = abs(freqs * frame_rate)
    
    maxi = np.argmax(np.abs(w))
    loudest = hz[maxi]
    low = hz[maxi - bandwidth/2]
    high = hz[maxi - bandwidth/2]
    output = (low, high, loudest)    
    
    wavfile.write('bachFiltered.wav',frame_rate, loudest.real/1000)
    wavplay(file_name)

    return output
      
"""
fname = "bach10sec.wav"

# Plot the sound
music,frame_rate,nframes,nchannels = read_wave(fname,debug=True)
if nchannels > 1:
    music = music.sum(axis=1)

pyplot.plot(music)
pyplot.show()

# Listen to the sound
wavplay('bach10sec.wav')
wavplay('scary.wav')
"""