from tkinter import filedialog
file = filedialog.askopenfilename()
with open('_file_saver.mbnhwfjg', 'w+') as f:
	f.write(file)
input()