from moviepy.editor import VideoFileClip
import os

full_video = str(input("\nInsert file path of video :\n"))
full_video = full_video.replace("\'","")[:-1]

arrPath = full_video.split("/")
fileName = arrPath[len(arrPath)-1]
save_path = full_video.replace(fileName,"")
arrFile = fileName.split(".")
folderName = fileName.replace("."+(arrFile[len(arrFile)-1]),"")
save_path=save_path+folderName

total_duration = VideoFileClip(full_video).duration
single_duration=total_duration+1
while (single_duration>total_duration):
    try:
        single_duration = int(input("\nEnter the limit of seconds that each video must have :\n"))
        if single_duration > total_duration or total_duration == 0:
            os.system('clear')
            print ("The seconds must be at least less than the total seconds of the video or different from 0")
            single_duration=total_duration+1
    except Exception as e:
        os.system('clear')
        print("Enter an integer")
os.system("mkdir "+save_path)

initialSubClip = 0
finalSubClip = total_duration%single_duration

part=0

while finalSubClip <= total_duration:
    part+=1
    current_video = folderName+"_part"+str(part)+".mp4"
    clip = VideoFileClip(full_video).subclip(initialSubClip,finalSubClip)
    print ("\n"+current_video+" = { \n  initial second : "+str(initialSubClip)+",\n  final second : "+str(finalSubClip)+"\n}\n")
    initialSubClip=finalSubClip
    finalSubClip+=single_duration
    clip.to_videofile(save_path+"/"+current_video, codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')
    print("-----------------###-----------------")