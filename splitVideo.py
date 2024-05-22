from moviepy.editor import VideoFileClip
import os
import platform

def clear_console():
    # Clear the console in a cross-platform way
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

full_video = input("\nInsert file path of video :\n").strip()
# Remove surrounding quotes if present
if full_video.startswith('"') and full_video.endswith('"'):
    full_video = full_video[1:-1]

arrPath = full_video.split(os.path.sep)
fileName = arrPath[-1]
save_path = full_video.replace(fileName, "")
arrFile = fileName.split(".")
folderName = fileName.replace("." + arrFile[-1], "")
save_path = os.path.join(save_path, folderName)

try:
    total_duration = VideoFileClip(full_video).duration
except OSError as e:
    print(f"Failed to read the duration of the video file. Error: {e}")
    exit(1)

single_duration = total_duration + 1
while single_duration > total_duration:
    try:
        single_duration = int(input("\nEnter the limit of seconds that each video must have :\n"))
        if single_duration > total_duration or total_duration == 0:
            clear_console()
            print("The seconds must be at least less than the total seconds of the video or different from 0")
            single_duration = total_duration + 1
    except ValueError:
        clear_console()
        print("Enter an integer")

os.makedirs(save_path, exist_ok=True)

initialSubClip = 0
finalSubClip = total_duration % single_duration

part = 0

while finalSubClip <= total_duration:
    part += 1
    current_video = f"{folderName}_part{part}.mp4"
    clip = VideoFileClip(full_video).subclip(initialSubClip, finalSubClip)
    print(f"\n{current_video} = {{ \n  initial second : {initialSubClip},\n  final second : {finalSubClip}\n}}\n")
    initialSubClip = finalSubClip
    finalSubClip += single_duration
    clip.write_videofile(os.path.join(save_path, current_video), codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')
    print("-----------------###-----------------")
