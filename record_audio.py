import pyaudio
import wave

# define parameters for recording
chunk = 1024 # number of samples per frame
format = pyaudio.paInt16 # sample format
channels = 1 # number of channels
rate = 44100 # sampling rate in Hz
duration = 10 # recording duration in seconds
filename = "output.wav" # output file name

# create an instance of PyAudio class
p = pyaudio.PyAudio()

# open a stream for recording
stream = p.open(format=format,
                channels=channels,
                rate=rate,
                input=True,
                frames_per_buffer=chunk)

# initialize an empty list to store the frames
frames = []

# loop through the stream and append the frames to the list
for i in range(0, int(rate / chunk * duration)):
    data = stream.read(chunk)
    frames.append(data)

# stop and close the stream
stream.stop_stream()
stream.close()

# terminate the instance of PyAudio class
p.terminate()

# create a wave file object and write the frames to it
wf = wave.open(filename, "wb")
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(format))
wf.setframerate(rate)
wf.writeframes(b"".join(frames))
wf.close()
