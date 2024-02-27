from tkinter import *
from customtkinter import *
from PIL import Image





def Dencrypt(num):
    pro.destroy()
    if num == 1:
        import decrytionCeaser
        decrytionCeaser.display()
    elif num == 2:
        import decryptionRSA
        decryptionRSA.display()
    elif num == 3:
        import decryptionAffine
        decryptionAffine.display()
    else:
        import decryptionAES
        decryptionAES.display()

def gohome():
    pro.destroy()
    from HomePage import page_English
    page_English()

def main5():
    global pro
    pro = CTk()
    pro.geometry('900x600+400+100')
    pro.title('Decryption')
    pro.resizable(FALSE, FALSE)
    pro.iconbitmap('icons/hider.ico')

    My_img = CTkImage(dark_image=Image.open("img2.png"), size=(900, 600))
    lab9 = CTkLabel(pro, image=My_img, text="", font=('Helvetica', 30, 'bold'))
    lab9.place(x=0, y=0)

    image2 = CTkImage(dark_image=Image.open("icons/back.ico"), size=(15, 15))
    image3 = CTkImage(dark_image=Image.open("icons/decryption.ico"), size=(15, 15))


    lab1 = CTkLabel(pro, text="Decryption Types", font=('Helvetica', 25, 'bold'), bg_color='#000d16')
    lab1.place(x=330, y=115)

    but1 = CTkButton(pro, text="Col transposition",
                     width=190, height=45, font=('Helvetica', 21, 'bold'), corner_radius=15, bg_color='#001220',
                     fg_color='#0d326e', command=lambda: Dencrypt(1),image=image3)
    but1.place(x=195, y=230)

    but2 = CTkButton(pro, text="RSA",
                     width=190, height=45, font=('Helvetica', 21, 'bold'), corner_radius=15, bg_color='#01193b',
                     fg_color='#0d326e', command=lambda: Dencrypt(2),image=image3)
    but2.place(x=490, y=360)

    but3 = CTkButton(pro, text="Affine Cipher",
                     width=190, height=45, font=('Helvetica', 21, 'bold'), corner_radius=15, bg_color='#000c18',
                     fg_color='#0d326e', command=lambda: Dencrypt(3),image=image3)
    but3.place(x=490, y=230)

    but4 = CTkButton(pro, text="AES",
                     width=190, height=45, font=('Helvetica', 21, 'bold'), corner_radius=15, bg_color='#02192b',
                     fg_color='#0d326e', command=lambda: Dencrypt(4),image=image3)
    but4.place(x=195, y=360)



    bt5 = CTkButton(pro, text='Back', command=gohome
                    ,width=150, height=30,
                     font=('Helvetica', 15, 'bold'),corner_radius=15,bg_color='#03002e',fg_color='#0d326e',image=image2 )
    bt5.place(x=10, y=15)

    pro.mainloop()


if __name__ == "__main__":
    main5()
