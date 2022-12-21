from pytube import YouTube

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
    d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1]
    try:
        # downloading the video
        d_video.download(SAVE_PATH)
        # result of success
        print(yt.title + " has been successfully downloaded.")
    except:
        print("Some Error!")
print('Task Completed!')
