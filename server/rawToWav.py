import wave
import numpy as np
import scipy.signal as signal

framerate = 16000

raw_file = open("record.txt", "rb")
wave_data = ""
while True:
    line = raw_file.readline()
    if not line:
        break
    wave_data += line

# ��WAV�ĵ�
f = wave.open(r"record-real.wav", "wb")

# ����������������λ����ȡ��Ƶ��
f.setnchannels(1)
f.setsampwidth(2)
f.setframerate(framerate)
# ��wav_dataת��Ϊ����������д���ļ�
f.writeframes(wave_data)
f.close()
