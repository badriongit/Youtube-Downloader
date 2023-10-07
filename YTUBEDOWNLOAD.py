from pytube import YouTube
import ffmpeg
while(True):
    print("\n")
    print("----------------YOUTUBE DOWNLOADER-----------------")
    print("---------------Developed using Pytube--------------")
    link = input("Enter the link: ")
    yt = YouTube(link)
    title = yt.title
    print(title)
    print("\n")
    print(yt.description)
    print("\n")
    print(yt.length)
    print("\n")
    print(yt.fmt_streams)
    print("\n")
    audio = input("Download Audio(a) / Video(v): ")
    dwd = input("Confirm (y/n):")
    if(dwd == "y" and audio == "v"):
        print("Downloading Video. Please wait..")
        stream = yt.streams.first()
        stream.download()
        print("Downloaded!!")
    elif (dwd == "y" and audio == "a"):
        print("Downloading Audio. Please wait..")
        yt.streams.filter(abr="160kbps", progressive=False).first().download(filename="audio.mp3")
        audio = ffmpeg.input("audio.mp3")
        print("Downloaded!!")
    else:
        print("Enter Inputs in proper format")
