try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()

mainWindow = tkinter.Tk()
mainWindow.title("Hello World")
mainWindow.geometry("640x480+50+400")

label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side='top')

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
canvas.pack(side='left')

button1 = tkinter.Button(mainWindow, text='button1')
button2 = tkinter.Button(mainWindow, text='button2')
button3 = tkinter.Button(mainWindow, text='button3')
button1.pack(side='left')
button2.pack(side='left')
button3.pack(side='left')

mainWindow.mainloop()
