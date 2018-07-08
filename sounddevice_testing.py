import argparse
import math
import numpy as np
import shutil
import numpy as np
import sounddevice as sd
from collections import deque


input_deque = deque()
default_microphone = sd.default.devices[0]
microphone_sample_rate = sd.query_devices(
    default_microphone
)['default_samplerate']


def microphone_callback(in_data, frames, time, status):
    deque.append(in_data)


def set_defaults():
    sd.defaults.channels = [1,2]


if __name__ == '__main__':
    audio_data = np.ndarry()
    set_defaults()

    seconds_to_record = 5

    recording = sd.rec(int(seconds_to_record * microphone_sample_rate))


#    with sd.InputStream(channels=2, callback=microphone_callback):
#        while True:
#            if any(input_deque):
