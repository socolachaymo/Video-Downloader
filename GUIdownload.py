import pytube
from tkinter import *

def download():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()
        video.download('Downloads')
        notif.config(fg='green', text='Download complete!')
    except Exception as e:
        print(e)
        notif.config(fg='red', text='Video could not be downloaded')

master = Tk()
master.title('Youtube Video Downloader')

Label(master, text='Youtube Video Converter', fg='red', font=('Arial',15)).grid(sticky=N,padx=100,row=0)
Label(master, text='Please enter the link to your video below : ', font=('Arial',12),).grid(sticky=N,pady=5,row=1)

url = StringVar()
Entry(master, width=50, textvariable=url).grid(sticky=N,row=2)

Button(master,width=20, text='Download', font=('Arial',12), command=download).grid(sticky=N,row=3,pady=15)
notif = Label(master, font=('Arial',12))
notif.grid(sticky=N,pady=1,row=4)


master.mainloop()


