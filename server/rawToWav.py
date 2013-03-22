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

# 打开WAV文档
f = wave.open(r"record-real.wav", "wb")

# 配置声道数、量化位数和取样频率
f.setnchannels(1)
f.setsampwidth(2)
f.setframerate(framerate)
# 将wav_data转换为二进制数据写入文件
f.writeframes(wave_data)
f.close()
