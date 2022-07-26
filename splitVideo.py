from moviepy.editor import VideoFileClip
from time import sleep
from datetime import datetime
import os

full_video = str(input("Insert file path of video :\n"))
full_video = full_video.replace("\'","")[:-1]

arrPath = full_video.split("/")
fileName = arrPath[len(arrPath)-1]
save_path = full_video.replace(fileName,"")
arrFile = fileName.split(".")
folderName = fileName.replace("."+(arrFile[len(arrFile)-1]),"")
save_path=save_path+folderName

current_duration = VideoFileClip(full_video).duration
total_duration = current_duration
single_duration=current_duration+1
while (single_duration>current_duration):
    try:
        single_duration = int(input("Enter the limit of seconds that each video must have :\n"))
        if single_duration > current_duration:
            os.system('clear')
            print ("The seconds must be at least less than the total seconds of the video")
    except Exception as e:
        os.system('clear')
        print("Enter an integer")
os.system("mkdir "+save_path)
part=1

initialVideo = total_duration%single_duration
clip = VideoFileClip(full_video).subclip(0, initialVideo)
current_video = folderName+"_part"+str(part)+".mp4"
clip.to_videofile(save_path+"/"+current_video, codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')
print("-----------------###-----------------")

part=int(total_duration/single_duration)+1
while current_duration > single_duration:
    clip = VideoFileClip(full_video).subclip(current_duration-single_duration, current_duration)
    current_duration -= single_duration
    current_video = folderName+"_part"+str(part)+".mp4"
    part-=1
    clip.to_videofile(save_path+"/"+current_video, codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')
    print("-----------------###-----------------")