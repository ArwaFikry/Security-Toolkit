from tkinter import *

from tkinter import filedialog

from customtkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import hover as ho


def gohome():
    root.destroy()
    from MediaAR import main_2
    main_2()


def action(pointer):
    if pointer == 'encode':
        pass
    if pointer == 'decode':
        pass
    if pointer == "browse_file":
        global file_path2
        file_path2 = filedialog.askopenfilename(title="Choose a Text file",
                                                filetypes=(("Text Files", "*.txt"),))
        if file_path2:
            text_box.delete(0.0, 'end')
            text_box.insert('end', file_path2)


    else:
        global file_path
        file_path = filedialog.askopenfilename(title="Choose an Image",
                                               filetypes=(("Image Files", ".png;.bmp;.jpg;.jpeg"),))
        selected_image = CTkImage(dark_image=Image.open(file_path), size=(250, 250))
        pointer.configure(image=selected_image, height=255, width=255, text="")
        # pointer.image = selected_image

    # updateButton()


def update_countdown(event=None):
    remaining_chars = max_chars - len(text_box.get("1.0", "end-1c"))
    countdown_label.configure(text=f": الحروف المتبقية {remaining_chars}")


max_chars = 200


def Apply():
    pass
    # secret = text_box.get(0.0, "end")
    # if len(file_path) > 0 and len(secret) > 1:
    #
    #     img_path = encode(file_path, text_box.get(0.0, "end"))
    #     if img_path:
    #         selected_image = CTkImage(dark_image=Image.open(img_path), size=(250, 250))
    #         lab5 = CTkLabel(fr, image=selected_image, height=255, width=255, text="")
    #         lab5.pack()
    #         lab6 = CTkLabel(fr, text="image after stegano")
    #         lab6.pack()
    #         # lb5.destroy()
    #         move()
    # elif len(file_path) == 0:
    #     lb2.configure(text_color="red", text="choose image to hide into first")
    # elif len(text_box.get(0.0, "end")) <= 1:
    #     text_box.configure(text_color="red")
    #     text_box.insert('end', "enter secret message to hide OR browse text file")


def move():
    # lab6.
    global my_y, my_y2
    my_y -= 20
    my_y2 += 20
    if my_y >= 50 or my_y2 < 700:
        fr.place(x=635, y=my_y)
        lb5.place(x=635, y=my_y2)
        root.after(50, move)


# def updateButton():
#     if len(file_path) >0 and len(file_path2) >0:
#         but4.configure(state="normal")

def display():
    global file_path, file_path2, my_y, my_y2
    my_y = 650 / 2 + 350
    my_y2 = 70
    file_path = ""
    file_path2 = ""
    global root
    root = CTk()
    root.title('صور الاخفاء')
    root.geometry("900x600+400+100")
    root.resizable(False, False)
    root.iconbitmap('icons/hider.ico')

    def handle_button_click():
        selected_item = combo_box.get()
        print(f"Button clicked! Selected item: {selected_item}")

    My_img2 = CTkImage(dark_image=Image.open("img2.png"), size=(950, 600))
    lab1 = CTkLabel(root, image=My_img2, text="", font=('Helvetica', 30, 'bold'))
    lab1.place(x=0, y=0)

    image = CTkImage(dark_image=Image.open("icons/ico.ico"), size=(19, 19))
    image1 = CTkImage(dark_image=Image.open("icons/apply1.ico"), size=(20, 20))
    image2 = CTkImage(dark_image=Image.open("icons/back.ico"), size=(16, 16))


    but1 = CTkButton(root, text="رجوع", command=gohome, width=150, height=30, font=('Helvetica', 15, 'bold'),
                     corner_radius=15, bg_color='#011828', fg_color='#0d326e',image=image2)
    but1.place(x=10, y=10)

    global lb2
    lb2 = CTkLabel(root, text=": اختر ملف الصورة", height=255, width=255, font=('Helvetica', 20), bg_color='#ADC7E5'
                   , text_color="black")
    lb2.place(x=40, y=70)

    but2 = CTkButton(root, text="تصفح", command=lambda: action(lb2), width=160, height=25,
                     font=('Helvetica', 15, 'bold'), corner_radius=250, bg_color='#021524', fg_color='#0d326e',image=image)
    but2.place(x=82, y=350)

    lb3 = CTkLabel(root, text="اكتب الرسالة المخفية او تصفح الملف", font=('Helvetica', 20, 'bold'),
                   bg_color="#000e17", text_color="white")
    lb3.place(x=330, y=75)

    global text_box
    text_box = CTkTextbox(root, width=270, height=200, corner_radius=25, border_width=3, wrap="word",
                          bg_color="#010f1a", border_color="#03002e", fg_color="white")
    text_box.place(x=315, y=100)
    global countdown_label
    countdown_label = CTkLabel(root, text=f"الحروف المتبقية {max_chars}", font=('Helvetica', 13, 'bold'),
                               bg_color="#000e17", text_color="white")
    countdown_label.place(x=470, y=298)

    text_box.bind("<KeyRelease>", update_countdown)



    but3 = CTkButton(root, text="تصفح", command=lambda: action("browse_file"), width=160, height=25,
                     font=('Helvetica', 15, 'bold'), corner_radius=25, bg_color='#00182a', fg_color='#0d326e',image=image)
    but3.place(x=375, y=350)

    global fr
    fr = CTkFrame(root, width=255, height=255, fg_color='#ADC7E5')
    fr.place(x=635, y=my_y)
    global lb5

    lb5 = CTkLabel(root, text="عرض الصورة بعد الاخفاء", height=255, width=255, font=('Helvetica', 20),
                   bg_color='#ADC7E5', text_color="black")
    lb5.place(x=605, y=my_y2)

    options = ["LSB", "DCT"]
    combo_box = CTkOptionMenu(root, values=options, width=140, height=30, bg_color='#011828')
    combo_box.place(x=380, y=415)

    lb4 = CTkLabel(root, text=": ادخل مفتاح التشفير", font=('Helvetica', 20, 'bold'), bg_color='#02101d')
    lb4.place(x=550, y=460)

    global ent2
    ent2 = CTkEntry(root, width=180, height=25, fg_color="white", text_color='red')
    ent2.place(x=360, y=460)

    global but4
    but4 = CTkButton(root, text="موافق", command=Apply, width=175, height=45, font=('Helvetica', 20, 'bold'),
                     bg_color='#011121', fg_color='#0d326e',image=image1,corner_radius=15)
    but4.place(x=360, y=510)
    ho.CreateToolTip(but4, 'الصورة في الاخفاء تنفيذ')

    rad = CTkRadioButton(root, text="تشفير", value=2, width=100, height=20,
                         corner_radius=25, bg_color='#01192a', font=('Helvetica', 15, 'bold'),
                         command=lambda: action("encode"), text_color='white',fg_color='blue')
    rad.place(x=250, y=420)

    rad1 = CTkRadioButton(root, text="فك التشفير", value=2, width=100, height=20,
                          corner_radius=25, bg_color='#011423', font=('Helvetica', 15, 'bold'),
                          command=lambda: action("decode"), text_color='white')
    rad1.place(x=580, y=420)

    root.mainloop()