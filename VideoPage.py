from tkinter import *

from tkinter import filedialog, messagebox

from customtkinter import *
from PIL import Image
from tkinter import ttk


def info():
    messagebox.showinfo('Video Steganography', 'Successful Process')


def gohome():
    root.destroy()
    from MediaST import main_9
    main_9()


def action(pointer):
    if pointer == "browse_file":
        global file_path2
        file_path2 = filedialog.askopenfilename(title="Choose a Text file",
                                                filetypes=(("Text Files", "*.txt"),))
        if file_path2:
            text_box.delete(0.0, 'end')
            text_box1.insert('end', file_path2)

    else:
        global file_path
        file_path = filedialog.askopenfilename(title="Choose an Image",
                                               filetypes=(("Image Files", ".png;.bmp;.jpg;.jpeg"),))
        selected_image = CTkImage(dark_image=Image.open(file_path), size=(250, 250))
        pointer.configure(image=selected_image, height=255, width=255, text="")
        pointer.image = selected_image

    # updateButton()


def update_countdown(event=None):
    remaining_chars = max_chars - len(text_box.get("1.0", "end-1c"))
    countdown_label.configure(text=f"Characters remaining: {remaining_chars}", text_color="white")


max_chars = 200


def Apply():
    pass
    # secret = text_box.get(0.0, "end")
    # if len(file_path) > 0 and len(secret) > 1:
    #
    #     img_path = encode(file_path, text_box.get(0.0, "end"))
    #     if img_path:
    #         selected_image = CTkImage(dark_image=Image.open(img_path), size=(250, 250))
    #         # lab5 = CTkLabel(fr, image=selected_image, height=255, width=255, text="")
    #         # lab5.pack()
    #         # lab6 = CTkLabel(fr, text="image after stegano")
    #         # lab6.pack()
    #         # lb5.destroy()
    #         move()
    # # elif len(file_path) == 0:
    # #     lb2.configure(text_color="red", text="choose image to hide into first")
    # elif len(text_box.get(0.0, "end")) <= 1:
    #     text_box.configure(text_color="red")
    #     text_box.insert('end', "")
    # info()

def move():
    # lab6.
    global my_y, my_y2
    my_y -= 20
    my_y2 += 20
    if my_y >= 50 or my_y2 < 700:
        # fr.place(x=635, y=my_y)
        # lb5.place(x=635, y=my_y2)
        root.after(50, move)


def display():
    global file_path, file_path2, my_y, my_y2
    my_y = 650 / 2 + 350
    my_y2 = 70
    file_path = ""
    file_path2 = ""
    global root
    root = CTk()
    root.title('Video Steganography')
    root.geometry("900x600+400+100")
    root.resizable(False, False)
    root.iconbitmap('icons/hider.ico')

    My_img2 = CTkImage(dark_image=Image.open("img2.png"), size=(900, 600))
    lab9 = CTkLabel(root, image=My_img2, text="", font=('Helvetica', 30, 'bold'))
    lab9.place(x=0, y=0)

    image = CTkImage(dark_image=Image.open("icons/ico.ico"), size=(20, 20))
    image1 = CTkImage(dark_image=Image.open("icons/apply1.ico"), size=(15, 15))
    image2 = CTkImage(dark_image=Image.open("icons/back.ico"), size=(15, 15))

    but1 = CTkButton(root, text="Back", command=gohome, width=150, height=30, font=('Helvetica', 15, 'bold'),
                     corner_radius=25, bg_color='#011828', fg_color='#0d326e',image=image2)
    but1.place(x=10, y=10)

    lb3 = CTkLabel(root, text="Enter secret message :", font=('Helvetica', 22,'bold'), bg_color="#000e17", text_color="white")
    lb3.place(x=325, y=65)

    global text_box
    text_box = CTkTextbox(root, width=270, height=200, corner_radius=25, border_width=3, wrap="word",
                          bg_color="#010f1a", border_color="#03002e", fg_color="white", text_color='Red')
    text_box.place(x=305, y=100)

    global countdown_label
    countdown_label = CTkLabel(root, text=f"Max of charachter : {max_chars}", font=('Helvetica', 12,'bold'),
                               bg_color="#01192a")
    countdown_label.place(x=315, y=300)

    text_box.bind("<KeyRelease>", update_countdown)

    lb3 = CTkLabel(root, text="Choose file :", font=('Helvetica', 20,'bold'), bg_color='#01192a')
    lb3.place(x=150, y=340)

    global text_box1
    text_box1 = CTkEntry(root, width=180, height=20,
                         bg_color="#010f1a", fg_color="white", text_color="Red")
    text_box1.place(x=310, y=340)

    but3 = CTkButton(root, text="Browse", command=lambda: action("browse_file"), width=50, height=25,
                     font=('Helvetica', 15, 'bold'), corner_radius=25, bg_color='#03002e', fg_color='#0d326e',image=image)
    but3.place(x=500, y=340)

    lb4 = CTkLabel(root, text="Encryption key :", font=('Helvetica', 20,'bold'), bg_color='#01192a')
    lb4.place(x=150, y=380)

    global ent2
    ent2 = CTkEntry(root, width=180, height=25, fg_color="white", text_color='red')
    ent2.place(x=310, y=380)

    options = ["Encode", "Decode"]
    combo_box = CTkOptionMenu(root, values=options, width=150, bg_color='#011828',font=('Helvetica', 13,'bold'))
    combo_box.place(x=195, y=435)

    options = ["option1", "option2"]
    combo_box1 = CTkOptionMenu(root, values=options, width=140, bg_color='#011828',font=('Helvetica',13,'bold'))
    combo_box1.place(x=475, y=435)

    global but4
    but4 = CTkButton(root, text="Apply", command=Apply, width=120, height=30, font=('Helvetica', 14,'bold'),
                     bg_color='#011828', fg_color='#0d326e', corner_radius=25,image=image1)
    but4.place(x=350, y=435)

    root.mainloop()
