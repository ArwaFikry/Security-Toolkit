from tkinter import *

from tkinter import filedialog

from customtkinter import *
from PIL import Image
from tkinter import ttk
import hover as ho


def gohome():
    root.destroy()
    from EncryptionPage import main5
    main5()


def action(pointer):
    if pointer == "path":
        global file_path
        file_path = filedialog.askopenfilename()
    elif pointer == "encode":
        global flag1
        flag1 = "encode"
    elif pointer == "decode":
        ent.delete(0, END)
        flag1 = "decode"
    elif pointer == "append":
        global flag2
        flag2 = "append"
    else:
        flag2 = "lsb"
    updateButton()


def Apply():
    pass

    # if flag2 == "append":  # -->choose Append technique
    #     if flag1 == "encode":  # --->encode +append
    #         data = ent.get()
    #         encode(file_path, data)
    #         ent.delete(0, END)
    #     else:  # --->decode + append
    #         ent.delete(0, END)
    #         ent.insert(0, decode(file_path))
    # elif flag2 == "lsb":  # -->choose LSb tech
    #     if flag1 == "encode":  # --->encode +LSb
    #         data = ent.get()
    #         encode2(file_path, data)
    #         ent.delete(0, END)
    #     else:  # --->decode + LSb
    #         ent.delete(0, END)
    #         ent.insert(0, decode2(file_path))


def updateButton():
    if flag1 != 0 and flag2 != 0 and len(file_path) > 0:
        but4.config(state=NORMAL)


def display():
    global flag1, flag2, file_path
    flag1 = 0
    flag2 = 0
    file_path = ""
    global root
    root = CTk()
    root.title('Encryption Affine Cipher')
    root.geometry("900x600+400+100")
    root.resizable(False, False)
    root.iconbitmap('icons/hider.ico')

    My_img2 = CTkImage(dark_image=Image.open("img2.png"), size=(900, 600))
    lab9 = CTkLabel(root, image=My_img2, text="", font=('Helvetica', 30, 'bold'))
    lab9.place(x=0, y=0)

    image = CTkImage(dark_image=Image.open("icons/ico.ico"), size=(20, 20))
    image1 = CTkImage(dark_image=Image.open("icons/apply1.ico"), size=(20, 20))
    image2 = CTkImage(dark_image=Image.open("icons/back.ico"), size=(15, 15))

    image = CTkImage(dark_image=Image.open("icons/ico.ico"), size=(20, 20))

    but1 = CTkButton(root, text="Back", command=gohome, width=150, height=30, font=('Helvetica', 15, 'bold'),
                     corner_radius=25, bg_color='#001624', fg_color='#0d326e', image=image2)
    but1.place(x=10, y=10)

    lb2 = CTkLabel(root, text="Enter text :", font=('Helvetica', 25), bg_color='#000e17')
    lb2.place(x=370, y=65)

    global ent
    ent = CTkTextbox(root, width=270, height=200, corner_radius=15, border_width=3,
                     wrap="word", bg_color="#000d16", border_color="#000d16", fg_color='white')
    ent.place(x=300, y=100)

    lb3 = CTkLabel(root, text="Choose file :", font=('Helvetica', 25), bg_color='#001729')
    lb3.place(x=200, y=400)

    but3 = CTkButton(root, text="Browse", command=lambda: action("path"), width=180, height=25, image=image,
                     font=('Helvetica', 15, 'bold'), corner_radius=25, bg_color='#001423', fg_color='#0d326e')
    but3.place(x=480, y=400)

    lb4 = CTkLabel(root, text="Enter encryption key :", font=('Helvetica', 25), bg_color='#001727')
    lb4.place(x=200, y=340)

    global ent2
    ent2 = CTkEntry(root, width=180, height=25, fg_color='white')
    ent2.place(x=480, y=342)

    global but4
    but4 = CTkButton(root, text="Apply", command=Apply,  width=175, height=45, font=('Helvetica', 20, 'bold'),
                     corner_radius=15, bg_color='#01182a', fg_color='#0d326e', image=image1)
    but4.place(x=345, y=450)
    ho.CreateToolTip(but4, 'processed encryption data')

    root.mainloop()
