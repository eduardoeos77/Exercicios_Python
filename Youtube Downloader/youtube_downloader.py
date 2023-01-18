import threading
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil, time, threading

#funções
# def select_path():
#     path = filedialog.askdirectory(initialdir='~\\videos')
#     path_label.config(text=path)

def download_file():
    get_link = link_field.get()
    user_path = filedialog.askdirectory(initialdir='~\\videos')
    #user_path = path_label.cget('text')
    download_label.config(text="Aguarde...")
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    #mp4_video = YouTube(get_link).streams.get_by_resolution(1080).download()
    shutil.move(mp4_video, user_path)
    download_label.config(text="Download concluído")


window = Tk()

#cosmético
icon = PhotoImage(file='YouTube-Icon-Full-Color-Logo.wine.png')
window.iconphoto(True, icon)

window.title("YouTube Downloader")

canvas = Canvas(window, width=750, height=150)
canvas.config(background='#4a4646')
canvas.pack()

#logo
logo_img = PhotoImage(file='YouTube-White-Full-Color-Logo.wine.png').subsample(10, 10)
canvas.create_image(150, 70, image=logo_img)

#campo para o link
link_label = Label(window, text="Copie o link do vídeo aqui:", font=("Arial", 12), fg="white", bg='#4a4646')
link_field = Entry(window, width=50)
canvas.create_window(500, 60, window=link_label)
canvas.create_window(500, 80, window=link_field)

#caminho
# path_label = Label(window, text="Escolha onde salvar o vídeo", font=("Arial", 15))
#open_btn = Button(window, text='Abrir pasta', command=os.startfile(path))
# canvas.create_window(250, 280, window=path_label)
#canvas.create_window(250, 200, window=open_btn)

download_label = Label(window, text="Download não iniciado", fg="white", bg='#4a4646', font=("Courier", 12))
canvas.create_window(500, 120, window=download_label)

download_btn = Button(window, text='Download', fg="white", bg='#4a4646', command=download_file)
canvas.create_window(700, 80, window=download_btn)

window.mainloop()