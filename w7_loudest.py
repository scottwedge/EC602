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
#import PyQt4.QtGui as qt
import time
import numpy as np
#import matplotlib.pyplot as pyplot
#import math

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
"""
def wavplay(fname):
    "play a sound, and sleep until it is finished"
    qt.QSound.play(fname)
    music,frame_rate,nframes,nchannels = read_wave(fname)
    time.sleep(nframes/frame_rate)
"""

def loudest_band(music,frame_rate,bandwidth):
    
    #scale bandwidth
    band = int(bandwidth/(frame_rate/len(music)))
    
    #calc fft
    firstfft = np.fft.fft(music)
    w = np.fft.fftshift(firstfft)    
    zer = np.arange(-frame_rate/2,frame_rate,frame_rate/len(music))
    zero = abs(zer).argmin()
    
    musicfft = w[zero:]    
    
    #get signal power
    sigpwr = abs(musicfft)**2
    
    lo = []
    hi = []
    pwr = []    
    
    for i in range(len(musicfft)-band):
        pwr += [sum(sigpwr[i:i+band-1])]
        lo += [i]
        hi += [i+band]
    
    #get max
    maxi = np.argmax(pwr)
    if(maxi!= 0):
        bp1 = np.append(np.ones(bandwidth+1),np.zeros(maxi-1))
        bpneg = np.append(np.zeros(zero - bandwidth - maxi), bp1)

        bp2 = np.append(np.zeros(maxi-1),np.ones(bandwidth+1))
        bppos = np.append(bp2,np.zeros(zero-bandwidth-maxi))
    else:
        bpneg = np.append(np.zeros(zero - bandwidth - maxi),np.ones(bandwidth))
        bppos = np.append(np.ones(bandwidth),np.zeros(zero - bandwidth - maxi))
    
    final = np.append(bpneg,bppos)
    print(final)
    
    filtered = w*final
    time = np.fft.ifft(np.fft.ifftshift(filtered))
    
    result = (lo[maxi]*(frame_rate/len(music)),hi[maxi]*(frame_rate/len(music)),time.real)      
    
    return result


    
