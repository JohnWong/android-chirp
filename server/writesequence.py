import wave
import numpy as np
import scipy.signal as signal

framerate = 8000
time = 0.096
#1760 1864 ... 10500
hzs = [1750, 1875, 2000, 2125, 2250, 2375, 2500, 2625]

# 产生10秒44.1kHz的100Hz - 1kHz的频率扫描波
t = np.arange(0, time, 1.0/framerate)

i = 0;
while i < len(hzs):
    hz = hzs[i]
    #wave_data = signal.chirp(t, 100, time, 1000, method='linear') * 10000
    single_data =  signal.chirp(t, hz, time, hz, method='linear') * 10000
    if i == 0:
        wave_data = single_data.astype(np.short)
    else:
        wave_data = np.append(wave_data, single_data.astype(np.short))
    i += 1
    
# 打开WAV文档
f = wave.open(r"sweep_sequence.wav", "wb")

# 配置声道数、量化位数和取样频率
f.setnchannels(1)
f.setsampwidth(2)
f.setframerate(framerate)
# 将wav_data转换为二进制数据写入文件
f.writeframes(wave_data.tostring())
f.close()
