from cryptography.fernet import Fernet # fernet library for encryption
from hashlib import sha256 # for turn master key into special 32 bytes hash
from base64 import urlsafe_b64encode # for reqire fernet URL-safe base64 coded requirement
from tkinter import messagebox
def save(message,mkey,title):
    if message.get("1.0", "end-1c")=="" or mkey.get()=="":
        messagebox.showerror("Hata","Mesaj veya masterkey boş olamaz!")
    else:
        # turning message text input into bytes
        messageb = message.get("1.0", "end-1c").encode('utf-8')
        mkeyb = mkey.get().encode("utf-8")
        
        # creating special 32 bytes hash and encoding it with b64encode to requirement of fernet
        mkeyhash = sha256(mkeyb).digest()
        mkeybase64 = urlsafe_b64encode(mkeyhash)
        fernet = Fernet(mkeybase64)
        #encryption
        ciphered_text = fernet.encrypt(messageb)
        #writing crypted message into .txt file according to title
        
        with open(f'{title.get()}.txt', "wb") as dosya:
            dosya.write(ciphered_text)
    

def decrypt(mkey,message):
    mkeyb = mkey.get().encode("utf-8")
    messageb_decrypt = message.get("1.0", "end-1c").encode('utf-8')
    mkeyhash = sha256(mkeyb).digest()
    mkeybase64 = urlsafe_b64encode(mkeyhash)
    fernet = Fernet(mkeybase64)
    
    if message.get("1.0", "end-1c")=="" or mkey.get()=="":
        messagebox.showerror("Hata","Çözme işlemi için mesaj ve masterkey girilmelidir!")
    else:
        decrypted = fernet.decrypt(messageb_decrypt)
        print(decrypted.decode("utf-8"))
    