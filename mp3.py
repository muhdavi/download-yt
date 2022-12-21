# importing packages
from pytube import YouTube
import os

# where to save
SAVE_PATH = "."  # to_do

# link of the video to be downloaded
link = [
    "https://www.youtube.com/watch?v=xsrCSpkPLs0",
    "https://www.youtube.com/watch?v=Zd-5wFaCEag",
    "https://www.youtube.com/watch?v=OLApxa8v8cc",
    "https://www.youtube.com/watch?v=VirjOuqM9v0"
]

#link="https://www.youtube.com/watch?v=xWOoBJUqlbI"

for i in link:
    try:
        # object creation using YouTube
        # which was imported in the beginning
        yt = YouTube(i)
    except:
        # to handle exception
        print("Connection Error")
    # get the video with the extension and
    # resolution passed in the get() function
    d_video = yt.streams.filter(only_audio=True).first()
    try:
        # downloading the video
        out_file = d_video.download(SAVE_PATH)
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        # result of success
        print(yt.title + " has been successfully downloaded.")
    except:
        print("Some Error!")
print('Task Completed!')

