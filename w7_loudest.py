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

def dialer(file_name,frame_rate,phone,tone_time):
    #generate two tone signal

    output=[]    
    
    for n in phone:
        if(n=="0"):
            f1 = 941
            f2 = 1336
        elif(n=="1"):
            f1 = 697
            f2 = 1209
        elif(n=="2"):
            f1 = 697
            f2 = 1336
        elif(n=="3"):
            f1 = 697
            f2 = 1477
        elif(n=="4"):
            f1 = 770
            f2 = 1209
        elif(n=="5"):
            f1 = 770
            f2 = 1336
        elif(n=="6"):
            f1 = 770
            f2 = 1477
        elif(n=="7"):
            f1 = 852
            f2 = 1209
        elif(n=="8"):
            f1 = 852
            f2 = 1336
        elif(n=="9"):
            f1 = 852
            f2 = 1477
        elif(n=="A"):
            f1 = 697
            f2 = 1633
        elif(n=="B"):
            f1 = 770
            f2 = 1633
        elif(n=="C"):
            f1 = 852
            f2 = 1633
        elif(n=="D"):
            f1 = 941
            f2 = 1633
        elif(n=="*"):
            f1 = 941
            f2 = 1209
        elif(n=="#"):
            f1 = 941
            f2 = 1477
        else:
            f1 = 0
            f2 = 0
            
        fs = frame_rate
        duration = tone_time
        x1 = (np.sin(2*np.pi*np.arange(fs*duration)*f1/fs)).astype(np.float32)
        x2 = (np.sin(2*np.pi*np.arange(fs*duration)*f2/fs)).astype(np.float32)
        x = x1 + x2
        output = np.concatenate([output,x])
        
    #output = np.array(output)
    wavfile.write(file_name, frame_rate, output)  
    wavplay(file_name)

dialer("test1",8000,"123456789",0.5)
      
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