import tkinter as tk
from tkinter import *
import os, webbrowser

root = tk.Tk()
root.title('Social Media Keyword Search')
socials = []



def searchMedias():
    print(facebook.get())
    if facebook.get():
        keyword = e.get()
        webbrowser.open('https://www.facebook.com/page/124299671596193/search/?q=' + keyword)

    print(andiBlog.get())
    if andiBlog.get():
        keyword = e.get()
        webbrowser.open('https://harbourcitydoulas.com/?s=' + keyword)

    print(instaHash.get())    
    if instaHash.get():
        keyword = e.get()
        webbrowser.open('https://www.instagram.com/explore/tags/' + keyword)
    
        
     
        
    






canvas = tk.Canvas(root, height = 700, width = 700, bg = '#263D42')
canvas.pack()

frame = tk.Frame(root, bg = 'white')
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)



facebook = tk.BooleanVar()
tk.Checkbutton(frame, text = 'Facebook', height= 5, width = 20, var = facebook).pack()


andiBlog = tk.BooleanVar()
tk.Checkbutton(frame, text = 'Blog', height = 5, width = 20, var = andiBlog).pack()

instaHash = tk.BooleanVar()
insta = tk.Checkbutton(frame, text = 'Instagram', height = 5, width = 20, var = instaHash).pack()

e = Entry(frame, justify = LEFT)
e.pack()

launch = tk.Button(root, text = 'Search', padx = 10, pady = 5, fg = 'white', bg = '#263D42', command = searchMedias)
launch.pack()


for app in socials:
    label = tk.Label(frame, text = app)
    label.pack()



root.mainloop()
