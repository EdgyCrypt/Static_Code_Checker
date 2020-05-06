from tkinter import Tk
from tkinter.filedialog import askopenfilename
root = Tk()
file = askopenfilename()
root.destroy()
with open('_file_saver.mbnhwfjg', 'w+') as f:
	f.write(file)
input()