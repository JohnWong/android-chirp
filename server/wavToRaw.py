import wave
import pylab as pl
import numpy as np

# 打开WAV文档
f = wave.open(r"D:\py\sound\record.wav", "rb")
#f = wave.open(r"D:\py\sound\ding.wav", "rb")

# 读取格式信息
# (nchannels, sampwidth, framerate, nframes, comptype, compname)
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]

# 读取波形数据
str_data = f.readframes(nframes)
f.close()

#将波形数据转换为数组
wave_data = np.fromstring(str_data, dtype=np.short)
wave_data.shape = -1, nchannels
wave_data = wave_data.T
time = np.arange(0, nframes) * (1.0 / framerate)



# 打开WAV文档
count = 0
file = open(r"clip_record.h", "wb")

for wave_byte in wave_data[0]:
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
        
print("end")
