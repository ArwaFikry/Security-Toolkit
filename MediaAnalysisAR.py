from tkinter import *
from customtkinter import *
from PIL import Image
import hover as ho


def gohome1():
    root.destroy()
    from HomePage import page_Arabic
    page_Arabic()


def action(num):
    root.destroy()  # Hide the root window
    if num == 1:
        import steganalysisImageAR
        steganalysisImageAR.display1()
    elif num == 2:
        import steganalysisVideoAR
        steganalysisVideoAR.display1()
    elif num == 3:
        import steganalysisAudioAR
        steganalysisAudioAR.display1()
    else:
        import SteganalysisTextAR
        SteganalysisTextAR.display1()


def main_2():
    global root
    root = CTk()
    root.title('تحليل الوسائط')
    root.geometry("900x600+400+100")
    root.resizable(False, False)
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

    lab1 = CTkLabel(root, text="اختر نوع الوسائط", font=('Helvetica', 30, 'bold'), bg_color='#000e19')
    lab1.place(x=335, y=115)

    but1 = CTkButton(root, text="صورة", command=lambda: action(1), image=image5,
                     width=180, height=45, font=('Helvetica', 21, 'bold'), corner_radius=15,
                     bg_color='#011422', fg_color='#0d326e')
    but1.place(x=195, y=230)
    ho.CreateToolTip(but1, 'الصورة من البيانات تحليل')

    but2 = CTkButton(root, text="مقطع مرئي", command=lambda: action(2), image=image4,
                     width=180, height=45, font=('Helvetica', 21, 'bold'), corner_radius=15,
                     bg_color='#001027', fg_color='#0d326e')
    but2.place(x=490, y=360)
    ho.CreateToolTip(but2, 'المرئي المقطع من البيانات تحليل')

    but3 = CTkButton(root, text="مقطع صوتي", command=lambda: action(3), image=image3,
                     width=180, height=45, font=('Helvetica', 21, 'bold'), corner_radius=15,
                     bg_color='#000d16', fg_color='#0d326e')
    but3.place(x=490, y=230)
    ho.CreateToolTip(but3, 'الصوتي المقطع من البيانات تحليل')

    but4 = CTkButton(root, text="نص", command=lambda: action(4), image=image1,
                     width=180, height=45, font=('Helvetica', 21, 'bold'), corner_radius=15,
                     bg_color='#001528', fg_color='#0d326e')
    but4.place(x=195, y=360)
    ho.CreateToolTip(but4, 'النص من البيانات تحليل')

    bt5 = CTkButton(root, text='رجوع', command=gohome1
                    , width=150, height=30, font=('Helvetica', 15, 'bold'), corner_radius=50, bg_color='#011826',
                    fg_color='#0d326e', image=image2)
    bt5.place(x=10, y=15)

    root.mainloop()


if __name__ == "__main__":
    main_2()
