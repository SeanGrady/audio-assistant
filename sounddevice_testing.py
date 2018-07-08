import argparse
import math
import numpy as np
import shutil
import numpy as np
import sounddevice as sd
from collections import deque

input_deque = deque()

def microphone_callback(in_data, frames, time, status):
    deque.append(in_data)



if __name__ == '__main__':
    audio_data = np.ndarry()
    with sd.InputStream(channels=2, callback=microphone_callback):
        while True:
            if any(input_deque):


