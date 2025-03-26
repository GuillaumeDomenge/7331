import wave
import numpy as np
import pyaudio

# Parameters
rate = 44100  # Samples per second
duration = 10 # seconds
mult = 2
frequency = 440  # Hz (A4 note)

# Generate samples
t = np.linspace(0, duration, int(rate * duration), endpoint=False)
freq2 = np.linspace(frequency, duration/mult*frequency, int(rate * duration), endpoint=False)
freq3 = frequency + np.sin(freq2/5)
print(t)
samples = np.sin(2 * np.pi * freq3 * t) * 32767
print(samples/32767)
samples = samples.astype(np.int16)

# Open a wave file
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=rate,
                output=True)

# Play the sound
stream.write(samples.tobytes())
stream.stop_stream()
stream.close()
p.terminate()

