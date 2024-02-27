from tkinter import *
from customtkinter import *
from PIL import Image
import hover as ho


def action1(num):
    arabic_page.destroy()  # Hide the root window
    if num == 1:
        import EncryptionPageAR
        EncryptionPageAR.main5()
    elif num == 2:
        import DecryptionPageAR
        DecryptionPageAR.main5()
    elif num == 3:
        import MediaAR
        MediaAR.main_2()
    else:
        import MediaAnalysisAR
        MediaAnalysisAR.main_2()


def action2(num):
    english_page.destroy()  # Hide the root window
    if num == 1:
        import EncryptionPage
        EncryptionPage.main5()
    elif num == 2:
        import DEcryptionPage
        DEcryptionPage.main5()
    elif num == 3:
        import Media
        Media.main_1()
    else:
        import MediaST
        MediaST.main_9()


def main():
    global pro
    pro = CTk()
    pro.geometry('900x600+400+100')
    pro.title('Steganography')
    pro.resizable(FALSE, FALSE)
    pro.iconbitmap('icons/ico.ico')

    My_img = CTkImage(dark_image=Image.open("img2.png"), size=(900, 600))
    lab9 = CTkLabel(pro, image=My_img, text="", font=('Helvetica', 30, 'bold'))
    lab9.place(x=0, y=0)
    image1 = CTkImage(dark_image=Image.open("icons/arabic.ico"), size=(20, 20))
    image2 = CTkImage(dark_image=Image.open("icons/english.ico"), size=(20, 20))

    button1 = CTkButton(pro, text='العربية', font=('Helvetica', 25, 'bold'),
                        command=open_home_Arabic, width=160, height=40, corner_radius=20, bg_color='#001526',
                        fg_color='#0d326e',image=image1)
    button1.place(x=230, y=300)
    ho.CreateToolTip(button1, 'Go To Arabic Page')



    button2 = CTkButton(pro, text='English', font=('Helvetica', 25, 'bold'),
                        command=open_home_English, width=160, height=40, corner_radius=20, bg_color='#001321',
                        fg_color='#0d326e',image=image2)
    button2.place(x=230, y=200)
    ho.CreateToolTip(button2, 'Go To English Page')
    pro.mainloop()


def open_home_Arabic():
    pro.destroy()
    page_Arabic()


def open_home_English():
    pro.destroy()
    page_English()


def page_Arabic():
    # Arabic page code
    global arabic_page
    arabic_page = CTk()
    arabic_page.geometry('900x600+400+100')
    arabic_page.title('الصفحة الرئيسية')
    arabic_page.resizable(FALSE, FALSE)
    arabic_page.iconbitmap('icons/hider.ico')


    My_img1 = CTkImage(dark_image=Image.open("img2.png"), size=(900, 600))
    lab0 = CTkLabel(arabic_page, image=My_img1, text="", font=('Helvetica', 30, 'bold'))
    lab0.place(x=0, y=0)


    image2 = CTkImage(dark_image=Image.open("icons/back.ico"), size=(15, 15))
    image3 = CTkImage(dark_image=Image.open("icons/encryption.ico"), size=(20, 20))
    image4 = CTkImage(dark_image=Image.open("icons/decryption.ico"), size=(20, 20))
    image5 = CTkImage(dark_image=Image.open("icons/stegno.ico"), size=(20, 20))
    image6 = CTkImage(dark_image=Image.open("icons/steganal.ico"), size=(20, 20))

    btt5 = CTkButton(arabic_page, text='التشفير', width=190, height=40, font=('Helvetica', 20, 'bold'),
                     bg_color='#011321', fg_color='#0d326e',
                     corner_radius=15, command=lambda: action1(1),image=image3)
    btt5.place(x=195, y=230)
    ho.CreateToolTip(btt5, 'can encryption data with 4 techniques')


    btt6 = CTkButton(arabic_page, text='تحليل المعلومات', width=190, height=40, font=('Helvetica', 20, 'bold'),
                     bg_color='#01162b', fg_color='#0d326e',
                     corner_radius=15, command=lambda: action1(4),image=image6)
    btt6.place(x=490, y=360)
    ho.CreateToolTip(btt6, 'can decode any stego media type without enter stego technique')

    btt7 = CTkButton(arabic_page, text='فك التشفير', width=190, height=40, font=('Helvetica', 20, 'bold'),
                     bg_color='#000c15', fg_color='#0d326e',
                     corner_radius=15, command=lambda: action1(2),image=image4)
    btt7.place(x=490, y=230)
    ho.CreateToolTip(btt7, 'can decryption data with 4 techniques ')

    btt8 = CTkButton(arabic_page, text='اخفاء المعلومات', width=190, height=40, font=('Helvetica', 20, 'bold'),
                     bg_color='#00182a', fg_color='#0d326e',
                     corner_radius=15, command=lambda: action1(3),image=image5)
    btt8.place(x=195, y=360)
    ho.CreateToolTip(btt8, 'can make steganography with any media type')


    bt5 = CTkButton(arabic_page, text='رجوع', command=open_welcome_page1
                    ,width=150, height=30, font=('Helvetica', 15, 'bold'), corner_radius=15,bg_color='#051021',
                    fg_color='#0d326e',image=image2)
    bt5.place(x=10, y=15)

    arabic_page.mainloop()


def open_welcome_page1():
    arabic_page.destroy()
    main()


def page_English():
    # English page code
    global english_page
    english_page = CTk()
    english_page.geometry('900x600+400+100')
    english_page.title('Home')
    english_page.resizable(FALSE, FALSE)
    english_page.iconbitmap('icons/hider.ico')

    My_imge = CTkImage(dark_image=Image.open("img2.png"), size=(900, 600))
    lab11 = CTkLabel(english_page, image=My_imge, text="", font=('Helvetica', 30, 'bold'))
    lab11.place(x=0, y=0)

    image2 = CTkImage(dark_image=Image.open("icons/back.ico"), size=(15, 15))
    image3 = CTkImage(dark_image=Image.open("icons/encryption.ico"), size=(20, 20))
    image4 = CTkImage(dark_image=Image.open("icons/decryption.ico"), size=(20,20))
    image5 = CTkImage(dark_image=Image.open("icons/stegno.ico"), size=(20, 20))
    image6 = CTkImage(dark_image=Image.open("icons/steganal.ico"), size=(20, 20))

    btt1 = CTkButton(english_page, text='Encryption', width=190, height=45, font=('Helvetica', 20, 'bold'),
                     bg_color='#011321', fg_color='#0d326e',
                     corner_radius=15, command=lambda: action2(1),image=image3)
    btt1.place(x=195, y=230)
    ho.CreateToolTip(btt1, 'can encryption data with 4 techniques')

    btt2 = CTkButton(english_page, text='Steganalysis', width=190, height=45, font=('Helvetica', 20, 'bold'),
                     bg_color='#01162b', fg_color='#0d326e',
                     corner_radius=15, command=lambda: action2(3),image=image6)
    btt2.place(x=490, y=360)
    ho.CreateToolTip(btt2, 'can decode any stego media type without enter stego technique')

    btt3 = CTkButton(english_page, text='Decryption', width=190, height=45, font=('Helvetica', 20, 'bold'),
                     bg_color='#000c15', fg_color='#0d326e',
                     corner_radius=15, command=lambda: action2(2),image=image4)
    btt3.place(x=490, y=230)
    ho.CreateToolTip(btt3, 'can decryption data with 4 techniques ')

    btt4 = CTkButton(english_page, text='Steganography', width=190, height=45, font=('Helvetica', 20, 'bold'),
                     bg_color='#00182a', fg_color='#0d326e',
                     corner_radius=15, command=lambda: action2(4),image=image5)
    btt4.place(x=195, y=360)
    ho.CreateToolTip(btt4, 'can make steganography with any media type')

    bt5 = CTkButton(english_page, text='Back', command=open_welcome_page,
                    width=150, height=30, font=('Helvetica', 15, 'bold'), corner_radius=25, bg_color='#051021',
                    fg_color='#0d326e',image=image2)
    bt5.place(x=10, y=15)

    english_page.mainloop()


def open_welcome_page():
    english_page.destroy()
    main()


if __name__ == "__main__":
    main()
