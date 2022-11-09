import scipy.io.wavfile
import sounddevice
from scipy.io.wavfile import write, read
from playsound import playsound
fs = 44100
second = int(input("Enter the time duration in seconds: "))
print('Recording... \n')
record_voice = sounddevice.rec(int(second * fs), samplerate = fs, channels = 1)
sounddevice.wait()
write('out.wav', fs, record_voice)
print('Finished...\nPlease check it...')
playsound('/Users/macbookm1-dan/PycharmProjects/voicerecorder/out.wav')
scipy.io.wavfile.read('/Users/macbookm1-dan/PycharmProjects/voicerecorder/out.wav')