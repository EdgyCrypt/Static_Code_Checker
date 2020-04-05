from tkinter import  filedialog

file = filedialog.askdirectory()

with open('_file_saver.mbnhwfjg', 'w+') as f:
    f.write(file)
