#modules
from pytubefix import YouTube
from art import *
from Color_Console import ctext
import os
import re
import datetime


#Behind the scenes😁

##video func

def Download_video(url):
    yt=YouTube(url)
    print("Are you sure to download : ",end="")
    ctext(f"'{yt.title}'","green")
    print("""to confirm press 1 or rentring press 2 : """,end="")
    confirmation =input("")
    while True :
        if confirmation == "1" :
            break
        elif confirmation == "2":
            os.system("cls" if os.name =="nt" else "clear")
            new_input=input("video url :")
            Download_video(new_input)
        else:
            ctext("Invalid Input,please input 1 or 2","red")
            confirmation =input(": ")
    videos=yt.streams.filter(only_video=True,file_extension="mp4",adaptive=True)

    audio=yt.streams.filter(only_audio=True,adaptive=True)[0]

    video_resolutions=list(dict.fromkeys(stream.resolution for stream in videos))

    print(f"""
            video title :{yt.title}
            video duration: {datetime.timedelta(seconds=yt.length)}
            video resolution: {video_resolutions}
            """)


    res=input("enter video's resolution you want : ")

    for i in range(len(videos)):

        if res in str(videos[i]):
            Filename=re.sub(r'[\/:*?"<>|]', '',res+videos[i].title)
            videos[i].download(filename=Filename+".mp4")
            audio.download(filename=Filename+".mp3")
            command_ = f'MP4Box -add "{Filename}.mp4" -add "{Filename}.mp3" -new "{Filename}_final.mp4"'
            os.system(command_)
            os.remove(f"{Filename}.mp4")
            os.remove(f"{Filename}.mp3")
            break
    ctext("Done 😁👌","green")
    return 0

##audio func

def Download_audio(url):
    yt=YouTube(url)
    print("Are you sure to download : ",end="")
    ctext(f"'{yt.title}'","green")
    print("""to confirm press 1 or rentring press 2 : """,end="")
    confirmation =input("")
    while True :
        if confirmation == "1" :
            break
        elif confirmation == "2":
            os.system("cls" if os.name =="nt" else "clear")
            new_input=input("video url :")
            Download_audio(new_input)
        else:
            ctext("Invalid Input,please input 1 or 2","red")
            confirmation =input(": ")
    print(f"""
            audio title :{yt.title}
            audio duration: {datetime.timedelta(seconds=yt.length)}
            """)
    audio=yt.streams.filter(only_audio=True,adaptive=True)[0]
    Filename=re.sub(r'[\/:*?"<>|]', '',yt.title)
    audio.download(filename=Filename+".mp3")

    ctext("Done 😁👌","green")
while True:


#interface

    dragon=text2art("Black Dragon 🐉","random")
    ctext(dragon,"red","black")

    ctext("""
    Facebook :'https://www.facebook.com/profile.php?id=61566183519418'
    Insta :'https://www.instagram.com/blac_kdragon_2006/'
    GitHub :'https://github.com/mostafa-12'
    ""","green","black")

    ctext("Welcome to YOUTUBE DOWNLOADER💫","green","black")

    ctext("""
    To download audio    => 1
            single video => 2
                    exit => 3
    ""","green","black")

    process=input(": ")

    os.system("cls" if os.name =="nt" else "clear")





    if process == "1":
        url=input("audio url: ")
        Download_audio(url)
    elif process == "2":
        url=input("video url: ")
        Download_video(url)

    elif process == "3":
        exit()

    else:
        ctext("""Invalied Input, please enter
              1=> audio
              2=>single video
              3=> exit
              """)
        process=input(" : ")


