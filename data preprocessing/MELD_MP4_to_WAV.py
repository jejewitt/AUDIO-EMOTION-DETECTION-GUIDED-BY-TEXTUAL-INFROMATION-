# 48000
# convert meld video data into audio data
# expects folders extracting data from in _wav format 
#note that there are videos with the same if combining data
import subprocess
import os

wav_list = []
# folders = ["TEST","TRAIN","VAL"]
folders = ["TRAIN"]
# folders = ["WAV"]

# durations = []
empty = []
name = []
for i in folders:
    da= os.listdir(f"./{i}")    
    for k in da:
        one_path = f"./{i}/"+ k
        if  '.mp4' in k: # '.mp3' in k or
            if os.path.getsize(one_path)!=0:
                wav_list.append(one_path) 
                name.append(k[:-4])
            else:
                empty.append(one_path) 

for i,val in enumerate(wav_list):
	command = f"ffmpeg -i {val} -ar 48000 -vn ./out/{name[i]}.wav"
	subprocess.call(command, shell=True)