from pytube import YouTube
from pytube import Playlist
#from pytube.cli import on_progress
from math import ceil
import sys
import os
import threading

links = []
link = []
thrd = []
size = 0

def split_link(links,size):
    for i in range(0,len(links),size):
        yield links[i:i+size]

def playlist_down(yt_link):
    p = Playlist(yt_link)
    #global links
    print("\nPlaylist Name : {}\nChannel Name  : {}".format(p.title,p.owner))
    print("\nTotal Videos  : {}\nTotal Views   : {}".format(p.length,p.views))
    try:
        for url in p.video_urls:
            links.append(url)
    except:
        print('Playlist link is not valid.')
        sys.exit(0)
    if len(links)<4:
        link = [[ele] for ele in links]
        #print(type(link[0]))
    else:
        size = ceil(len(links)/4)
        link = list(split_link(links,size))
    print("\nLength of Links : {len}\nSize : {sz}".format(len=len(links), sz=len(link)))
    print("Downloading Started...\n")    
    for i in range(len(link)):
        tmp = threading.Thread(target=downloader, args=(i, link, ))
        thrd.append(tmp)
    for i in range(len(thrd)):
        thrd[i].start()
    return 'complete'

def downloading(yt_link):
    video = YouTube(yt_link)
    video_type = video.streams.filter(progressive = True, file_extension = "mp4").get_highest_resolution()
    title = video.title
    print ("Fetching: {}...".format(title))
    global file_size
    file_size = video_type.filesize
    print('Total Size: ', str(round(file_size/(1024*1024))) + 'MB\n')
    #Starts the download process
    video_type.download(file_path())
    print('File downloaded!!!')
    return video_type

def downloader(num, link):
    for i in link[num]:
        filename=downloading(i)
        print("threading {}:  ".format(num) + filename.split('/')[-1] + ' Downloaded Successfully')
    again = start()

def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    return download_path

def check_link(yt_link):
    val = None
    try:
        p = Playlist(yt_link)
        val = 'plist'
        print(p)
    except:
        print("\nNot playlist...\n")
        try:
            p = YouTube(yt_link)
            val = 'single'
            print(p)
        except:
            val = 'Invalid Link!!!'
            print(val)
            start()
    return val

def start():
    print("Your video will be saved to: {}".format(file_path()))
    #Input 
    yt_url = input("Copy and paste your YouTube URL here: ")
    if yt_url=='exit':
        sys.exit()
    print ("\nAccessing YouTube URL...")
    val = check_link(yt_url)
    print("val ===== ", val)    
    if val == 'plist':
        playlist_down(yt_url)
    else:
        filename=downloading(yt_url)