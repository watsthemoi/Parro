'''Using github project for reference: https://gist.github.com/sloria/5693955
Provides WAV recording functionality via non-blocking approach: 

Non-blocking mode (start and stop recording):
>>> rec = Recorder(channels=2)
>>> with rec.open('nonblocking.wav', 'wb') as recfile:
...     recfile.start_recording()
...     recfile.stop_recording()'''

import sounddevice as sd
import numpy as np
import wave


class Recorder(object):
    '''A method to call the RecordingFile method to start and stop recording audio
    '''

    def __init__(self, channels=1, rate=48000, frames_per_buffer=1024):
        self.channels = channels
        self.rate = rate
        self.frames_per_buffer = frames_per_buffer

    def open(self, fname, mode='wb'):
        return RecordingFile(fname, mode, self.channels, self.rate,
                             self.frames_per_buffer)


class RecordingFile(object):
    '''A recorder class for recording audio to a WAV file.
    Records in mono by default.
    '''

    def __init__(self, fname, mode, channels, rate, frames_per_buffer):
        self.fname = fname
        self.mode = mode
        self.channels = channels
        self.rate = rate
        self.frames_per_buffer = frames_per_buffer
        self.wavefile = self._prepare_file(self.fname, self.mode)
        self._stream = None
        self.frames = []

    def __enter__(self):
        return self

    def __exit__(self, exception, value, traceback):
        self.close()

    def start_recording(self, device=None):
        '''Start non-blocking recording'''
        self.frames = []  # Reset frames
        self._stream = sd.InputStream(samplerate=self.rate, channels=self.channels, callback=self.callback, device=device)
        self._stream.start()

    def stop_recording(self):
        '''Stop non-blocking recording'''
        self._stream.stop()
        self._stream.close()
        # Convert float32 data to int16 and write it to WAV
        audio_data = np.concatenate(self.frames)  # Concatenate all frames
        int16_audio = np.int16(audio_data * 32767)  # Convert float32 to int16
        self.wavefile.writeframes(int16_audio.tobytes())  # Save to WAV

    def get_audio_data(self):
        # Return a numpy array of the recorded frames
        if len(self.frames) > 0:
            return np.concatenate(self.frames, axis=0)
        else:
            return np.array([])

    def callback(self, indata, frames, time, status):
        '''Callback to process incoming audio data'''
        if status:
            print(status)
        self.frames.append(indata.copy())  # Save frames to write to WAV later

    def close(self):
        if self._stream:
            self._stream.close()
        self.wavefile.close()

    def _prepare_file(self, fname, mode='wb'):
        wavefile = wave.open(fname, mode)
        wavefile.setnchannels(self.channels)
        wavefile.setsampwidth(2)  
        wavefile.setframerate(self.rate)
        return wavefile