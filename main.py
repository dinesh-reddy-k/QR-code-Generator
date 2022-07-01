from tkinter import *
from pyqrcode import create as c
import png
from PIL import Image as i
from PIL import ImageTk as it
def f():
    a=e.get()
    b=c(a)
    b.png('myqr.png',scale=6)
    img=i.open('myqr.png').resize((200,200),i.Resampling.NEAREST)
    img1=img.convert(mode='RGBA')
    img1.save('myqr.png',format='PNG')
    img=i.open('myqr.png')
    img1=it.PhotoImage(img)
    Label(r,text='qr code',bg='red',image=img1).place(x=100,y=400)
#tkinter file start
from tkinter import *
r=Tk()
r.geometry('400x600')
r.configure(bg='orange')
r.title('QR code Generator')
Label(r,text='Hi! welcome\nThis is Dinesh Reddy',font=('Italic',30,'bold'),bg='black',fg='blue').place(x=0,y=50)
Label(r,text='Please enter the text or link\nto create the QR code',font=('italic',20),fg='red',bg='blue').place(x=30,y=200)
e=Entry(r,font=10,width=25)
e.place(x=50,y=300)
Button(text='Generate',bg='black',fg='red',font=15,command=f).place(x=100,y=350)
Button(text='END',bg='black',fg='red',font=15,command=r.quit).place(x=250,y=350)
r.mainloop()
#tkinter file end