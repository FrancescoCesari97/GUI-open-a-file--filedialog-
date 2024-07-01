
from tkinter import *

from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    initialdir="D:\\corso web developer\\python\\GUI open a file (filedialog)\\main.py",
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*")
                                    ])
    # filetext = str(text.get(1.0, END))
    filetext = input("Enter some text")
    file.write(filetext)
    file.close()


def openFile():
    filepath = filedialog.askopenfilename(initialdir="D:\\corso web developer\\python",
                                          title="Open file",
                                          filetypes=(("text files", "*.text"),
                                          ("all files", "*.*")))
    print(filepath)
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(text="Open", command=openFile)
button.pack()


# * how to save a file 


buttonSave = Button(text="Save", command=saveFile)
buttonSave.pack()

text = Text(window)
text.pack()

window.mainloop()