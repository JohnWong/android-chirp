from pyaudio import PyAudio, paInt16 
import numpy as np 
import wave
import math
import threading

NUM_SAMPLES = 512      # pyAudio内部缓存的块的大小
DB_THRESHOLD = 40.0
NUM_RESULT = NUM_SAMPLES/2-1
SAMPLING_RATE = 16000    # 取样频率
DATA_SIZE = 8
DATA_INDEX = [56, 60, 64, 68, 72, 76, 80, 84]
DATA_FREQ = [1750, 1875, 2000, 2125, 2250, 2375, 2500, 3635]


class RecordThread(threading.Thread):
    def save_wave_file(self, filename, data): 
        wf = wave.open(filename, 'wb') 
        wf.setnchannels(1) 
        wf.setsampwidth(2) 
        wf.setframerate(SAMPLING_RATE) 
        wf.writeframes("".join(data)) 
        wf.close() 

    def run(self):
        # 开启声音输入
        pa = PyAudio() 
        stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True, 
                frames_per_buffer=NUM_SAMPLES) 

        recognize_temp = [0, 0, 0]
        recognize_index = 0


        while True: 
            # 读入NUM_SAMPLES个取样
            string_audio_data = stream.read(NUM_SAMPLES) 
            # 将读入的数据转换为数组
            audio_data = np.fromstring(string_audio_data, dtype=np.short) 
            fft_data = np.fft.fft(audio_data)
            spec_gain = []
        
            for i in range(DATA_SIZE):
                spec_index = DATA_INDEX[i]
                rex = fft_data[spec_index].real
                imx = fft_data[spec_index].imag
                spec_gain.append(20 * math.log10(2 * math.sqrt(rex * rex + imx * imx) / NUM_SAMPLES))
                if spec_gain[i] > DB_THRESHOLD:
                    last_recognize = recognize_temp[recognize_index]
                    if last_recognize <= 0 or spec_gain[i] > spec_gain[last_recognize - 1]:
                        recognize_temp[recognize_index] = i + 1
                        
            if recognize_index >= 2:
                if recognize_temp[0] != 0 or recognize_temp[1] != 0 or recognize_temp[2] != 0:
                    print(recognize_temp[0], recognize_temp[1], recognize_temp[2])
                recognized = 0
                if recognize_temp[0] == recognize_temp[1]:
                    recognized = recognize_temp[0]
                elif recognize_temp[2] == recognize_temp[0] or recognize_temp[2] == recognize_temp[1]:
                    recognized = recognize_temp[2]
                if recognized > 0:
                    print("识别到%d" % DATA_FREQ[recognized - 1])
                recognize_index = 0
                recognize_temp[0] = 0
                recognize_temp[1] = 0
                recognize_temp[2] = 0
            else:
                recognize_index += 1
            
t = RecordThread()
t.setDaemon(True)
t.start()
