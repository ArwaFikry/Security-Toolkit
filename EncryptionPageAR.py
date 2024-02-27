from tkinter import *
from customtkinter import *
from PIL import Image
import hover as ho

def back():
    root.destroy()
    main5()


def about():
    pro.destroy()
    about_page()

def Encrypt(num):
    pro.destroy()
    if num == 1:
        import encryptionAR
        encryptionAR.display(num)
    elif num == 2:
        import encryptionAR
        encryptionAR.display(num)
    elif num == 3:
        import encryptionAR
        encryptionAR.display(num)
    else:
        import encryptionAR
        encryptionAR.display(num)

def gohome():
    pro.destroy()
    from HomePage import page_Arabic
    page_Arabic()

def main5():
    global pro
    pro = CTk()
    pro.geometry('900x600+400+100')
    pro.title('التشفير')
    pro.resizable(FALSE, FALSE)
    pro.iconbitmap('icons/hider.ico')

    My_img = CTkImage(dark_image=Image.open("img2.png"), size=(900, 600))
    lab9 = CTkLabel(pro, image=My_img, text="", font=('Helvetica', 30, 'bold'))
    lab9.place(x=0, y=0)

    image = CTkImage(dark_image=Image.open("icons/encryption.ico"), size=(16, 16))
    image2 = CTkImage(dark_image=Image.open("icons/back.ico"), size=(15, 15))
    image3 = CTkImage(dark_image=Image.open("icons/about.ico"), size=(20, 20))

    lab1 = CTkLabel(pro, text="أنواع التشفير", font=('Helvetica', 30, 'bold'), bg_color='#000d16')
    lab1.place(x=370, y=115)

    but1 = CTkButton(pro, text="Col transposition",
                     width=190, height=50, font=('Helvetica', 21, 'bold'), corner_radius=15, bg_color='#001220',
                     fg_color='#0d326e',command=lambda: Encrypt(1),image=image)
    but1.place(x=195, y=230)
    ho.CreateToolTip(but1, 'شهرة اكثرها و التشفير تقنيات ابسط من واحده هي ')

    but2 = CTkButton(pro, text="RSA",
                     width=190, height=50, font=('Helvetica', 21, 'bold'), corner_radius=15, bg_color='#01193b',
                     fg_color='#0d326e',command=lambda: Encrypt(2),image=image)
    but2.place(x=490, y=360)
    ho.CreateToolTip(but2, 'الرقمي التوقيع و الامن البيانات لتشفير واسع نطاق على مستخدمه طريقة')

    but3 = CTkButton(pro, text="Affine Cipher",
                     width=190, height=50, font=('Helvetica', 21, 'bold'), corner_radius=15, bg_color='#000c18',
                     fg_color='#0d326e',command=lambda: Encrypt(3),image=image)
    but3.place(x=490, y=230)
    ho.CreateToolTip(but3, 'الاخري التشفير طرق كل في كفاءة اقل')

    but4 = CTkButton(pro, text="AES",
                     width=190, height=50, font=('Helvetica', 21, 'bold'), corner_radius=15, bg_color='#02192b',
                     fg_color='#0d326e',command=lambda: Encrypt(4),image=image)
    but4.place(x=195, y=360)
    ho.CreateToolTip(but4, 'السرية المعلومات لحماية المتحدة الولايات حكومة اختارته الذي واحد مفتاح باستخدام التشفير')



    bt5 = CTkButton(pro, text='رجوع', command=gohome
                    , width=150, height=30,
                     font=('Helvetica', 15, 'bold'),corner_radius=25,bg_color='#001020',fg_color='#0d326e',image=image2)
    bt5.place(x=10, y=15)

    bt6 = CTkButton(pro, text='معلومات'
                    , width=150, height=30, font=('Helvetica', 15, 'bold'), corner_radius=15, bg_color='#001020',
                    fg_color='#0d326e', command=about,image=image3)
    bt6.place(x=170, y=15)
    ho.CreateToolTip(bt6, 'المستخدمة الخوارزمية تقنيات جميع في العيوب و المزايا')


    pro.mainloop()

def about_page():
    global root
    root = CTk()
    root.geometry('900x600+400+100')
    root.title('About')
    root.resizable(FALSE, FALSE)
    root.iconbitmap('hider.ico')

    My_imge = CTkImage(dark_image=Image.open("img2.png"), size=(900, 600))
    lab11 = CTkLabel(root, image=My_imge, text="", font=('Helvetica', 30, 'bold'))
    lab11.place(x=0, y=0)

    image = CTkImage(dark_image=Image.open("but.ico"), size=(16, 16))
    image2 = CTkImage(dark_image=Image.open("back.ico"), size=(15, 15))

    bt5 = CTkButton(root, text='Back',
                        width=150, height=30, font=('Helvetica', 15, 'bold'), corner_radius=25, bg_color='#051021',
                        fg_color='#0d326e', command=back, image=image2)
    bt5.place(x=10, y=15)

    root.mainloop()




if __name__ == "__main__":
    main5()


