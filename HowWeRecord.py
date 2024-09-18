import sounddevice as sd
import threading
import soundfile as sf
from datetime import datetime
import time

now = datetime.now()
date_time = now.strftime("_%m_%d_%Y_%H_%M_%S")
start = time.time()

#setduration in seconds
duration = 60*60


filename = "RW39_25_5_3" + date_time
print(filename)
##SAve




# define the number of channels and sample rate for the audio recording


num_channels = 1
sample_rate = 44100


# select which microphones to record from
mic_ids = [1,2,3,4]  # replace with the device IDs of the microphones you want to use

# start recording audio from the selected microphones
def record(id,j):
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=num_channels, device=id)
    sd.wait()
    #setfilename
    file_name = f"{filename}mic{id}hour{j}.wav"  # name the file based on the microphone number
    sf.write(file_name, recording, sample_rate)
    
#hours
for j in range(1):
    threads = []
    for i in range(len(mic_ids)):
        t = threading.Thread(target=record,args=(mic_ids[i],j))
        threads.append(t)
    # wait for the recording to finish
    print(len(threads))
    for i in threads:
        i.start()
        
    for i in threads:
        i.join()
    
    
    
end = time.time()
print(end-start)