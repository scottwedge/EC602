# -*- coding: utf-8 -*-
"""
# AUTHOR John Keisling jfkeis@bu.edu
# AUTHOR Sigurdur Egill Thorvaldsson sigurdur@bu.edu

w7_dialer.py
10/20/16
Siggi&John
"""

# WAV file support
import scipy.io.wavfile as wavfile

# sound playing
import PyQt4.QtGui as qt

# sleep while sound is playing
import time

# arrays
import numpy

# plotting facilities
import matplotlib.pyplot as pyplot

def dialer(file_name,frame_rate,phone,tone_time):
    
    phone = [8, 5, 7, 5, 5, 9, 3, 6, 8, 9]
    
    for i in phone:
        if i == 0:
            #blabla
        else