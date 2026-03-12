import tkinter as tk
import os
from tkinter import messagebox

os.remove("%appdata%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\ric.pyw")


# Hide the main tkinter window
root = tk.Tk()
root.withdraw()

# Show the message box
messagebox.showinfo("Title", "Are you ready to get rickrolled?")
