from tkinter import Tk,mainloop,Button,Label,Entry,Text,messagebox #for UI
from PIL import Image, ImageTk # for adding image into Tk window
import commands

t=Tk()
t.minsize(width=200,height=400)
t.title("secret note trial")

img=Image.open("download.png")
imgre=img.resize((100,100))
image=ImageTk.PhotoImage(imgre)
Label(t,image=image).pack()


Label(t,text="Enter your title").pack()
title=Entry(t)
title.pack()


Label(t,text="mesajınız").pack()
message=Text(t,height=10,width=50)
message.pack()



Label(t,text="master keyi girin").pack()
mkey=Entry(t,width=30)
mkey.pack()

save=Button(t,text="kaydet ve şifrele",command=lambda: commands.save(message, mkey, title)) # lambda functions for both save and decrypt parts to fix code synchronization problems due to Tkinter
save.config(width=20,height=1)
save.pack()

decyrpt=Button(t,text="şifre çöz",width=10,height=1,command=lambda: commands.decrypt(mkey, message))
decyrpt.pack()



mainloop()
