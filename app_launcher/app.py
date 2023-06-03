import tkinter as tk
from tkinter import filedialog, Text, ttk
from tkinter import *
import glob
import os

root = tk.Tk()
root.title("Application Launcher")
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename= filedialog.askopenfilename(initialdir="/",title="Select File", filetypes=(("executables","*.exe"), ("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app,bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

def clearList():
    for widget in frame.winfo_children():
        widget.destroy()
    for x in range(len(apps)):
        apps.remove(apps[0])

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()


frame = tk.Frame(canvas, bg="white")
frame.place(relheight=0.8, relwidth=0.8,relx=0.1,rely=0.1)

toolbar = tk.Frame(root,bg='white')
toolbar.pack(expand=1)

openFile = ttk.Button(toolbar, text="Open File", command=addApp)
openFile.pack(expand=True,side=tk.LEFT)

runAppsbtn = ttk.Button(toolbar, text="Run Apps",command=runApps)
runAppsbtn.pack(expand=True,side=tk.LEFT)

clearAppsbtn = ttk.Button(toolbar,text="Clear List",command=clearList)
clearAppsbtn.pack(expand=True,side=tk.LEFT)

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt','w') as f:
    for app in apps:
        f.write(app + ',')