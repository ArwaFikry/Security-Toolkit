from tkinter import *
from customtkinter import *
from PIL import Image
import hover as ho


def gohome():
    root.destroy()
    from HomePage import page_English
    page_English()

def action(num):
    root.destroy()  # Hide the root window
    if num == 1:
        import steganalysisImage
        steganalysisImage.display1()
    elif num == 2:
        import steganalysisVideo
        steganalysisVideo.display1()
    elif num == 3:
        import steganalysisAudio
        steganalysisAudio.display1()
    else:
        import steganalysisText
        steganalysisText.display1()


def main_1():
    global root
    root = CTk()
    root.title('Steganalysis of media')
    root.geometry("900x600+400+100")
    root.resizable(False, False)
    root.iconbitmap('icons/hider.ico')

    My_img1 = CTkImage(dark_image=Image.open("img2.png"), size=(900, 600))
    lab9 = CTkLabel(root, image=My_img1, text="", font=('Helvetica', 30, 'bold'))
    lab9.place(x=0, y=0)


    image2 = CTkImage(dark_image=Image.open("icons/back.ico"), size=(15, 15))
    image1 = CTkImage(dark_image=Image.open("icons/text.ico"), size=(20, 20))
    image3 = CTkImage(dark_image=Image.open("icons/audio.ico"), size=(20, 20))
    image4 = CTkImage(dark_image=Image.open("icons/video.ico"), size=(20, 20))
    image5 = CTkImage(dark_image=Image.open("icons/img.ico"), size=(20, 20))

    lab1= CTkLabel(root , text="Select Media Type", font=('Helvetica', 25, 'bold'), bg_color='#000e19')
    lab1.place(x=320, y=115)

    but1 = CTkButton(root, text="Image", command=lambda: action(1),image=image5,
                     width=180, height=45,font=('Helvetica', 21, 'bold'),corner_radius=15,
                     bg_color='#011422',fg_color='#0d326e')
    but1.place(x=195, y=230)
    ho.CreateToolTip(but1, 'extract data from image')

    but2 = CTkButton(root, text="Video", command=lambda: action(2),image=image4,
                     width=180, height=45,font=('Helvetica', 21, 'bold'),corner_radius=15,
                     bg_color='#001027',fg_color='#0d326e')
    but2.place(x=490, y=360)
    ho.CreateToolTip(but2, 'extract data from video')

    but3 = CTkButton(root, text="Audio", command=lambda: action(3),image=image3,
                     width=180, height=45,font=('Helvetica', 21, 'bold'),corner_radius=15,
                     bg_color='#000d16',fg_color='#0d326e')
    but3.place(x=490, y=230)
    ho.CreateToolTip(but3, 'extract data from audio')

    but4 = CTkButton(root, text="Text", command=lambda: action(4),image=image1,
                     width=180, height=45,font=('Helvetica', 21, 'bold'),corner_radius = 15,
                     bg_color = '#001528',fg_color='#0d326e')
    but4.place(x=195, y=360)
    ho.CreateToolTip(but4, 'extract data from text')

    bt5 = CTkButton(root, text='Back', command=gohome
                    ,width=150, height=30,font=('Helvetica', 15, 'bold'), corner_radius=50, bg_color='#011826',
                    fg_color='#0d326e', image=image2)
    bt5.place(x=10, y=15)

    root.mainloop()


if __name__ == "__main__":
    main_1()
