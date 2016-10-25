# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w7_loudest.py
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
import math

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
    
    #mus,fs,nframes,nchannels = read_wave(music)

    w = np.fft.fft(mus)
    wShift = np.fft.fftshift(w)    
    
    zer = np.arange(-frame_rate/2,frame_rate,frame_rate/len(music))
    zero = abs(zer)    
    
    
    freqs = np.fft.fftfreq(len(mus))  
    fs = frame_rate
    hz = abs(freqs * fs)
    
    #maxi = np.argmax(np.abs(w))
    fftData=abs(freqs)**2
    # find the maximum
    maxi = fftData[1:].argmax() + 1
    loudest = hz[maxi]
    low = hz[maxi - math.floor(bandwidth/2)]
    high = hz[maxi + math.floor(bandwidth/2)]
    output = (low, high, loudest)    
    
    pyplot.plot(fftData)
    pyplot.show()    
    #wavfile.write('bachFiltered.wav',frame_rate, loudest.real/1000)

    return output
      
fname = "bach10sec.wav"

l, h, lds = loudest_band(fname,8000,10)
print(l,h,lds)

# Plot the sound
music,frame_rate,nframes,nchannels = read_wave(fname,debug=True)
if nchannels > 1:
    music = music.sum(axis=1)

pyplot.plot(music)
pyplot.show()



# Listen to the sound
#wavplay('bach10sec.wav')
#wavplay('scary.wav')
