import subprocess
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

firstFileName = filedialog.askopenfilename()
secondFileName = filedialog.askopenfilename()

test = subprocess.Popen(['echo', f"opening {firstFileName} {secondFileName}"], stdout=subprocess.PIPE)
output = test.communicate()[0]
print(output)

test = subprocess.Popen(['mpv', f"{firstFileName}", f'--external-file={secondFileName}', "--lavfi-complex=[vid1] [vid2] hstack [vo]"])
