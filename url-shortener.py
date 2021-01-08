from tkinter import *
root = Tk()
root.geometry("500x200")
def printtext():
    import pyshorteners as py
    print("done1")
    global link
    link = e.get()
    s=py.Shortener()
    sh = (s.tinyurl.short(link))

    Label(root,text=sh).pack()

root.title('URL shortener')

a='Enter Your URL : '
Label(root,text=a).pack()

e=Entry(root)
e.pack()
e.focus_set()

print("done2")
b=Button(root,text='short the URL',command=printtext)

b.pack(side='bottom')
root.mainloop()
