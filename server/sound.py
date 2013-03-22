import wave
import pylab as pl
import numpy as np

# 打开WAV文档
f = wave.open(r"D:\py\sound\sweep_1760.wav", "rb")
#f = wave.open(r"D:\py\sound\ding.wav", "rb")

# 读取格式信息
# (nchannels, sampwidth, framerate, nframes, comptype, compname)
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]

# 读取波形数据
str_data = f.readframes(nframes)
f.close()

print(params)

#将波形数据转换为数组
wave_data = np.fromstring(str_data, dtype=np.short)
wave_data.shape = -1, nchannels
wave_data = wave_data.T
time = np.arange(0, nframes) * (1.0 / framerate)

#wave_data = wave_data / 10000

count = 0
for wave_byte in wave_data[0]:
    print(wave_byte)
    count += 1
    if count == 200:
        break
showGraph = False;
if showGraph:
    # 绘制波形
    pl.subplot(211) 
    pl.plot(time, wave_data[0])
    if nchannels > 1:
        pl.subplot(212)
        pl.plot(time, wave_data[1], c="g")
    pl.xlabel("time (seconds)")
    pl.show()

print("end")
