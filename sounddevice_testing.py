import argparse
import math
import numpy as np
import shutil
import numpy as np
import sounddevice as sd
import matplotlib as mpl
mpl.use('tkagg')
from matplotlib import pyplot as plt
from collections import deque


input_deque = deque()
default_microphone = sd.default.device[0]
microphone_sample_rate = sd.query_devices(
    default_microphone
)['default_samplerate']


def microphone_callback(in_data, frames, time, status):
    deque.append(in_data)


def set_defaults():
    sd.default.channels = [1,2]


if __name__ == '__main__':
    set_defaults()

    seconds_to_record = 1
    frames = int(seconds_to_record * microphone_sample_rate)
    recording = sd.rec(
        frames=frames,
        samplerate=microphone_sample_rate,
        channels=1,
    )
    sd.wait()

    spectrum = np.fft.rfft(recording, axis=0)
    frequencies = np.fft.rfftfreq(len(recording), 1/microphone_sample_rate)
    plt.plot(recording)
    plt.show()
    plt.close()
    plt.plot(frequencies, abs(spectrum))
    plt.show()
    plt.close()


#    with sd.InputStream(channels=2, callback=microphone_callback):
#        while True:
#            if any(input_deque):
