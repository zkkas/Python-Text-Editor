import sys
import tkinter.filedialog as tkFiledialog
v= sys.version 
if sys.version_info[0] < 3:
    from Tkinter import *
else:
    from tkinter import *
root=Tk()
root.title("Text Editor")
Text=Text(root)
Text.grid()

def save():
    t = Text.get("1.0", "end-1c")
    savelocation = tkFiledialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()
    button=Button(root, text="Save", command=save)
    button.grid()
root.mainloop()