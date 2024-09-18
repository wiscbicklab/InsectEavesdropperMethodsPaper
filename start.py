import sounddevice as sd
import threading
import soundfile as sf
from datetime import datetime
from signal import pause
import SH1106
import time
import config
import traceback
import textwrap  # Import the textwrap module
import time
import subprocess
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  #
import argparse
import tempfile
import queue
import sys
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import shutil




from gpiozero import *

# 240x240 display with hardware SPI:
disp = SH1106.SH1106()
disp.Init()

# Clear display.
disp.clear()
# time.sleep(1)
#font = ImageFont.truetype('Font.ttf', 16)
font = ImageFont.load_default()

# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (disp.width, disp.height), "WHITE")

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
wrapped_text =  textwrap.fill("Insect Eavesdropper", width=16)
draw.text((0, 0),wrapped_text, font=font, fill=0)
disp.ShowImage(disp.getbuffer(image))

# pendrive_mount_point = "/mnt/usb0/WAV"
# 
# def is_pendrive_connected(mount_point):
#     return os.path.isdir(mount_point)
# 
# if (is_pendrive_connected(pendrive_mount_point) == False):
#     disp.clear()
#     image = Image.new('1', (disp.width, disp.height), "WHITE")
#     draw = ImageDraw.Draw(image)
#     wrapped_text =  textwrap.fill("Pendrive not found", width=16)
#     draw.text((0, 0),wrapped_text, font=font, fill=0)
#     disp.ShowImage(disp.getbuffer(image))
    
    








def start(actualtime):
    hours = 1
    duration = actualtime
    if(actualtime>3600):
        duration= 60*55
        hours = int(actualtime/3600)

    now = datetime.now()
    date_time = now.strftime("_%m_%d_%Y_%H_%M_%S")

    filename = "Pi1"+date_time
#setduration of each rec in seconds, each file will be this duration
    

##SAve

    
    ##SAve




    # define the number of channels and sample rate for the audio recording


    num_channels = 1
    sample_rate = 44100
    devices = sd.query_devices()
    mic_ids = []
    for i in devices:
        if i['name'].startswith("USB"):
            mic_ids.append(i['index'])
            
    print(mic_ids)
    
    def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        q.put(indata.copy())
        
        
        # start recording audio from the selected microphones
    def record(id,rectime):
 #   sd.wait()
    #setfilename

        file_name = f"{filename}mic{id}hour{rectime}.wav"  # name the file based on the microphone number
 #   sf.write(file_name, recording, sample_rate)
#    gc.collect()
        with sf.SoundFile(file_name, mode='x', samplerate=sample_rate,
                      channels=num_channels, subtype='PCM_24') as file:
            with sd.InputStream(samplerate=sample_rate, device=id,
                            channels=num_channels, callback=callback):
                start_time = time.time()
                while time.time() - start_time < duration:
                    file.write(q.get())
            
        
        print("Done" + date_time)
        
        
        
        
        

    for j in range(hours):
        
        q = queue.Queue()

        threads = []
        for i in range(len(mic_ids)):
            t = threading.Thread(target=record,args=[mic_ids[i],j])
            threads.append(t)
        # wait for the recording to finish
        print(len(threads))
        for i in threads:
            i.start()
            
        for i in threads:
            i.join()
            
       
        
    
            
        
selected_duration_options = [60, 600, 3600, 86400]  # 1 min, 10 min, 1 hour, 24 hours
selected_duration_index = 0  # Default index pointing to 1 minute
selected_duration = selected_duration_options[selected_duration_index]
        
try:
    while True:
        # with canvas(device) as draw:
         if disp.RPI.digital_read(disp.RPI.GPIO_KEY1_PIN) == 1:
        # Increase the duration when UP button is pressed
            disp.clear()
            # Make sure to create image with mode '1' for 1-bit color.
            image = Image.new('1', (disp.width, disp.height), "WHITE")

# Get drawing object to draw on image.
            draw = ImageDraw.Draw(image)
            print("UP")
            selected_duration_index = (selected_duration_index + 1) % len(selected_duration_options)
            selected_duration = selected_duration_options[selected_duration_index]
            wrapped_text = textwrap.fill(f"Duration: {selected_duration // 60} min", width=16)
            draw.text((0, 0), wrapped_text, font=font, fill=0)

       

         elif disp.RPI.digital_read(disp.RPI.GPIO_KEY2_PIN) == 1:
            # Decrease the duration when DOWN button is pressed
            print("UP")
            disp.clear()
            image = Image.new('1', (disp.width, disp.height), "WHITE")

# Get drawing object to draw on image.
            draw = ImageDraw.Draw(image)
            selected_duration_index = (selected_duration_index - 1) % len(selected_duration_options)
            selected_duration = selected_duration_options[selected_duration_index]
            wrapped_text = textwrap.fill(f"Duration: {selected_duration // 60} min", width=15)
            draw.text((0, 0), wrapped_text, font=font, fill=0)

         elif disp.RPI.digital_read(disp.RPI.GPIO_KEY3_PIN) == 1:
            # Start recording when CENTER button is pressed
            print("start")
            image = Image.new('1', (disp.width, disp.height), "WHITE")

# Get drawing object to draw on image.
            draw = ImageDraw.Draw(image)
            disp.clear()
            wrapped_text = textwrap.fill(f" Started for {selected_duration}s",width=15)
            draw.text((0, 0), wrapped_text, font=font, fill=0)
            disp.ShowImage(disp.getbuffer(image))
            start(selected_duration)
            disp.clear()
            image = Image.new('1', (disp.width, disp.height), "WHITE")
            draw = ImageDraw.Draw(image)
            draw.text((0, 0), f"Transferring files", font=font, fill=0)
            disp.clear()
            
            image = Image.new('1', (disp.width, disp.height), "WHITE")
            draw = ImageDraw.Draw(image)
            draw.text((0, 0), f"Done and files transferred", font=font, fill=0)
            
            
            

            
         disp.ShowImage(disp.getbuffer(image))
    
except IOError as e:
    print(e)
    
except KeyboardInterrupt:    
    print("ctrl + c:")
    disp.RPI.module_exit()
    exit()
    
    
