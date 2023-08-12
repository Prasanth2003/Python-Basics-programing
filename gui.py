from tkinter import *

window = Tk()
window.geometry("500x500")
button=Button(text = "YES",width=30,height=20)
label = Label(window,text="Wellcome")
window.configure(bg="#79D82D")
button.pack()
label.pack()
#to create a window
window.mainloop()
print("Hey")