from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter
import os
import subprocess
import threading
import time
def createiso():
    global source_folder_var
    global device_var
    global source_iso_var
    global status
    global progress_bar
    try:
        status.config(text="Creating ISO")
        command = ["mkisofs", "-o", source_iso_var, "-R", "-J", source_folder_var]
        subprocess.run(command, check=True)
        status.config(text="Burning ISO to disc")
        command = ["cdrecord", "-v", source_iso_var, "dev=" + device_var]
        subprocess.run(command, check=True)
        status.config(text="Burned Disc!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error!", f"Error burning ISO: {e}. The disc may no longer be usable!")
    progress_bar.stop()

def pickdir2():
    global source_iso_var
    folder = filedialog.asksaveasfilename(defaultextension=".iso", filetypes=[("ISO files", "*.iso")])
    if folder:
        source_iso_var = (folder)
def pickdir():
    global source_folder_var
    folder = filedialog.askdirectory()
    if folder:
        source_folder_var = (folder)
def stage4():
    global root
    global frm
    global source_folder_var
    global device_var
    global status
    global progress_bar
    root.destroy()
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    status=ttk.Label(frm, text="Burning")
    status.grid(column=0, row=0)
    progress_bar = ttk.Progressbar(root, mode="indeterminate", length=200)
    progress_bar.grid(column=0, row=1)
    progress_bar.start()
    threading.Thread(target=createiso, daemon=True).start()
    root.mainloop()
def stage3():
    global root
    global frm
    global source_folder_var
    global device_var
    global source_iso_var
    print(device_var)
    device_var = device_var.get()
    root.destroy()
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Summary").grid(column=0, row=0)
    ttk.Label(frm, text="Will burn directory: " + source_folder_var).grid(column=0, row=1)
    ttk.Label(frm, text="To device: " + device_var).grid(column=0, row=2)
    ttk.Label(frm, text="And will create an iso at:" + source_iso_var).grid(column=0, row=3)
    ttk.Button(frm, text="Burn", command=stage4).grid(column=0, row=5)
    root.mainloop()
def stage2():
    global root
    global frm
    global device_var
    root.destroy()
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    device_var = tkinter.StringVar()
    ttk.Label(frm, text="Enter device path").grid(column=0, row=0)
    deviceobject = ttk.Entry(root, textvariable=device_var, width=50).grid(column=0, row=1)
    ttk.Button(frm, text="Next", command=stage3).grid(column=0, row=3)
    root.mainloop()
def stage1():
    global root
    global frm
    global device_var
    root.destroy()
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Select files to burn").grid(column=0, row=0)
    ttk.Button(frm, text="Pick directory", command=pickdir).grid(column=0, row=1)
    ttk.Button(frm, text="Pick where to put the ISO", command=pickdir2).grid(column=0, row=2)
    ttk.Button(frm, text="Next", command=stage2).grid(column=0, row=3)
    root.mainloop()
    
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
source_folder_var = ""
source_iso_var = ""
device_var = ""
status = ""
progress_bar = ""
ttk.Label(frm, text="Welcome to the dvdburn wizard!").grid(column=0, row=0)
ttk.Button(frm, text="Next", command=stage1).grid(column=0, row=1)
root.mainloop()