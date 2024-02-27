from tkinter import *
from customtkinter import *
from PIL import Image
import hover as ho

def back():
    pro.destroy()
    main_2()

def about():
    root.destroy()
    about_page()


def gohome1():
    root.destroy()
    from HomePage import page_Arabic
    page_Arabic()

def action(num):
    root.destroy()  # Hide the root window
    if num == 1:
        import ImageAR
        ImageAR.display()
    elif num == 2:
        import VideoAR
        VideoAR.display()
    elif num == 3:
        import AudioAR
        AudioAR.display()
    else:
        import TextAR
        TextAR.display()


def main_2():
    global root
    root = CTk()
    root.title('Security Tool')
    root.geometry("900x600+400+100")
    # root.resizable(False, False)
    root.config(background='#3E3646')
    root.iconbitmap('icons/hider.ico')

    My_img1 = CTkImage(dark_image=Image.open("img2.png"), size=(900, 700))
    lab9 = CTkLabel(root, image=My_img1, text="", font=('Helvetica', 30, 'bold'))
    lab9.place(x=0, y=0)

    image2 = CTkImage(dark_image=Image.open("icons/back.ico"), size=(15, 15))
    image1 = CTkImage(dark_image=Image.open("icons/text.ico"), size=(20, 20))
    image3 = CTkImage(dark_image=Image.open("icons/audio.ico"), size=(20, 20))
    image4 = CTkImage(dark_image=Image.open("icons/video.ico"), size=(20, 20))
    image5 = CTkImage(dark_image=Image.open("icons/img.ico"), size=(20, 20))
    image6 = CTkImage(dark_image=Image.open("icons/about.ico"), size=(20, 20))

    lab1 = CTkLabel(root, text="اختر نوع الوسائط", font=('Helvetica', 30, 'bold'), bg_color='#000e17')
    lab1.place(x=330, y=115)

    but1 = CTkButton(root, text="صورة", command=lambda: action(1), image=image5,
                     width=180, height=45, font=('Helvetica', 21, 'bold'), corner_radius=15, bg_color='#021422',
                     fg_color='#0d326e')
    but1.place(x=195, y=230)
    ho.CreateToolTip(but1, 'تقنيتين باستخدام الصورة في البيانات اخفاء')

    but2 = CTkButton(root, text="مقطع مرئي", command=lambda: action(2), image=image4,
                     width=180, height=45, font=('Helvetica', 21, 'bold'), corner_radius=15, bg_color='#011423',
                     fg_color='#0d326e')
    but2.place(x=490, y=360)
    ho.CreateToolTip(but2, 'المرئي المقطع في البيانات اخفاء')

    but3 = CTkButton(root, text="مقطع صوتي", command=lambda: action(3), image=image3,
                     width=180, height=45, font=('Helvetica', 21, 'bold'), corner_radius=15, bg_color='#000d16',
                     fg_color='#0d326e')
    but3.place(x=490, y=230)
    ho.CreateToolTip(but3, 'تقنيتين باستخدام الصوتية الملفات في البيانات اخفاء')

    but4 = CTkButton(root, text="نص", command=lambda: action(4), image=image1,
                     width=180, height=45, font=('Helvetica', 21, 'bold'), corner_radius=15, bg_color='#01182a',
                     fg_color='#0d326e')
    but4.place(x=195, y=360)
    ho.CreateToolTip(but4, ' تقنيات 3 باستخدام النص في البيانات اخفاء')

    bt5 = CTkButton(root, text='رجوع', command=gohome1
                    , width=150, height=30, font=('Helvetica', 15, 'bold'), corner_radius=10, bg_color='#021826',
                    fg_color='#0d326e', image=image2)
    bt5.place(x=10, y=15)

    bt6 = CTkButton(root, text='معلومات'
                    , width=150, height=30, font=('Helvetica', 15, 'bold'), corner_radius=10, bg_color='#011c2f',
                    fg_color='#0d326e', command=about, image=image6)
    bt6.place(x=170, y=15)
    ho.CreateToolTip(bt6, 'المستخدمة الخوارزمية تقنيات جميع في العيوب و المزايا')
    root.mainloop()


def about_page():
    global pro
    pro = CTk()
    pro.geometry('900x600+400+100')
    pro.title('About')
    pro.resizable(FALSE, FALSE)
    pro.iconbitmap('hider.ico')

    My_imge = CTkImage(dark_image=Image.open("img2.png"), size=(900, 600))
    lab11 = CTkLabel(pro, image=My_imge, text="", font=('Helvetica', 30, 'bold'))
    lab11.place(x=0, y=0)

    bt9 = CTkButton(pro, text='رجوع'
                    , width=150, height=30, font=('Helvetica', 15, 'bold'), corner_radius=50, bg_color='#051021',
                    fg_color='#0d326e', command=back)
    bt9.place(x=10, y=15)

    pro.mainloop()


if __name__ == "__main__":
    main_2()
