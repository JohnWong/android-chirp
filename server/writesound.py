import wave
import numpy as np
import scipy.signal as signal

framerate = 8000
time = 30
#[1750, 1875, 2000, 2125, 2250, 2375, 2500, 3635]
hz = 1750

# 产生10秒44.1kHz的100Hz - 1kHz的频率扫描波
t = np.arange(0, time, 1.0/framerate)

#wave_data = signal.chirp(t, 100, time, 1000, method='linear') * 10000
wave_data = signal.chirp(t, hz, time, hz, method='linear') * 10000
wave_data = wave_data.astype(np.short)

# 打开WAV文档
f = wave.open(r"sweep_%d.wav" % hz, "wb")

# 配置声道数、量化位数和取样频率
f.setnchannels(1)
f.setsampwidth(2)
f.setframerate(framerate)
# 将wav_data转换为二进制数据写入文件
f.writeframes(wave_data.tostring())
f.close()

file = open(r"clip_%d.h" % hz, "wb")
count = 0
for wave_byte in wave_data:
    if count == 0:
        file.write("\t\"")
    temp_string = "%04x" % (wave_byte & 0xffff)
    #小端转置
    file.write(r"\x%s\x%s" % (temp_string[2:], temp_string[:2]))
    if count == 7:
        file.write("\"\n")
        count = 0
    else:
        count += 1

if count != 0:
    file.write("\"\n")
file.close()
