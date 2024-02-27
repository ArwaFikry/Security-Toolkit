import customtkinter
from tkinter import *
from tkinter import filedialog,messagebox
from lsb import encode, decode
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import hover as ho


def info():
    messagebox.showinfo('Steganography', 'Successful Process')

def gohome():
    root.destroy()
    from MediaST import main_9
    main_9()


def action(pointer):
    if pointer == 'Encode':
        lb3.configure(text="Enter secret message or browse file:")
        lb3.place(x=315)
        text_box.configure(state="normal")
    elif pointer == 'Decode':
        lb3.configure(text="Output secret message:")
        lb3.place(x=360)
        text_box.delete(0.0, 'end')
        update_countdown()
        text_box.configure(state="disabled")

    elif pointer == "browse_file":
        global file_path2
        file_path2 = filedialog.askopenfilename(title="Choose a Text file",
                                                filetypes=(("Text Files", "*.txt"),))
        if file_path2:
            text_box.delete(0.0, 'end')
            fhand= open(file_path2, "r", encoding="utf-8")
            data=fhand.read()
            global width, hight,remaining_chars,max_chars
            remaining_chars = max_chars - len(text_box.get("0.0", "end"))
            for ch in data:
                if remaining_chars>0:
                    text_box.insert('end', ch)
                    update_countdown()

    else:
        global image_path
        image_path = filedialog.askopenfilename(title="Choose an Image",
                                               filetypes=(("Image Files", "*.png;*.bmp;*.jpg;*.jpeg"),))
        image = Image.open(image_path)
        width, height = image.size
        max_chars=(width*height)/3
        max_chars=int(max_chars)
        update_countdown()
        selected_image = CTkImage(dark_image=Image.open(image_path), size=(250, 250))
        lb2.configure(image=selected_image, height=255, width=255, text="")
        data=text_box.get(0.0, "end")
        data=data.strip()
        if data =="choose browse image first":
            text_box.delete(0.0,"end")
            text_box.configure(text_color="black")



def Reset():
    root.destroy()
    display()

def Apply(radvalue):
    secret = text_box.get(0.0, "end")
    if len(image_path) == 0:
        lb2.configure(text_color="red", text="choose image first")
    elif radvalue == "Decode":
        inp_dialog = CTkInputDialog(text="Enter encryption key")
        key=inp_dialog.get_input()
        secret = ""
        text_box.configure(state="normal")
        if key is None:
            pass
        elif len(key)>0:
            secret = decode(image_path,key)
            text_box.delete(0.0, "end")
            text_box.insert(0.0, secret)
            info()
    elif len(secret)<=1 or secret=="enter secret message to hide OR browse text file":
        text_box.insert('end', "enter secret message to hide OR browse text file")
    elif radvalue == "Encode":
        inp_dialog = CTkInputDialog(text="Enter encryption key \n default value 100")
        key = inp_dialog.get_input()
        if key is None:
            pass
        elif len(key)>0:
            stego_img = encode(image_path, secret, key)
        else:
            stego_img = encode(image_path, secret, 100)
        if stego_img:
            selected_image = CTkImage(dark_image=Image.open(stego_img), size=(250, 250))
            lb5.configure(image=selected_image, text="")
            lb6 = CTkLabel(root, text="Image after stegano", font=('Helvetica', 16, 'bold'), bg_color="#000e17",
                           text_color="white")
            lb6.place(x=660, y=320)
            but4 = CTkButton(root, text="Reset", command=Reset, width=150, height=30,
                             font=('Helvetica', 15, 'bold'),
                             corner_radius=25, bg_color='#011828', fg_color='#0d326e', )
            but4.place(x=660, y=500)
            info()


global max_chars
max_chars=0
def update_countdown(event=None):
    global remaining_chars
    remaining_chars = max_chars - len(text_box.get("0.0", "end"))
    if max_chars==0:
        text_box.insert('end',"choose browse image first")
        text_box.configure(state="disabled")
    elif max_chars>0:
        text_box.configure(state="normal")
    if remaining_chars<0:
        text_box.configure(text_color="red")
    countdown_label.configure(text=f"Characters remaining: {remaining_chars}")

def handle_button_click():
    selected_item = combo_box.get()
    print(f"Button clicked! Selected item: {selected_item}")

def display():
    global image_path, file_path2
    image_path = ""
    file_path2 = ""
    global root
    root = CTk()
    root.title('Image Steganography')
    root.geometry("900x600+400+100")
    root.resizable(False, False)
    root.iconbitmap('icons/hider.ico')

    My_img2 = CTkImage(dark_image=Image.open("img2.png"), size=(950, 600))
    lab1 = CTkLabel(root, image=My_img2, text="", font=('Helvetica', 30, 'bold'))
    lab1.place(x=0, y=0)

    image = CTkImage(dark_image=Image.open("icons/ico.ico"), size=(19, 19))
    image1 = CTkImage(dark_image=Image.open("icons/apply1.ico"), size=(20, 20))
    image2 = CTkImage(dark_image=Image.open("icons/back.ico"), size=(16, 16))

    but1 = CTkButton(root, text="Back", command=gohome, width=150, height=30, font=('Helvetica', 15, 'bold'),
                     corner_radius=25, bg_color='#011828', fg_color='#0d326e',image=image2)
    but1.place(x=10, y=10)

    global lb2
    lb2 = CTkLabel(root, text="select image file :", height=255, width=255, font=('Helvetica', 20), bg_color='#ADC7E5'
                   , text_color="black")
    lb2.place(x=40, y=60)

    but2 = CTkButton(root, text="Browse", command=lambda: action("browse"), width=160, height=25,
                     font=('Helvetica', 15, 'bold'), corner_radius=250, bg_color='#021524', fg_color='#0d326e',image=image)
    but2.place(x=82, y=340)

    global lb3
    lb3 = CTkLabel(root, text="Enter secret message or browse file:", font=('Helvetica', 16, 'bold'),
                   bg_color="#000e17", text_color="white")
    lb3.place(x=315, y=60)

    global text_box
    text_box = CTkTextbox(root, width=270, height=200, corner_radius=25, border_width=3, wrap="word",
                          bg_color="#010f1a", border_color="#03002e", fg_color="white",text_color="black")
    text_box.place(x=315, y=90)

    global countdown_label
    countdown_label = CTkLabel(root, text=f"Characters remaining: {max_chars}", font=('Helvetica', 13, 'bold'),
                               bg_color="#00101d", text_color="white")
    countdown_label.place(x=335, y=290)
    update_countdown()
    text_box.bind("<KeyRelease>", update_countdown)

    but3 = CTkButton(root, text="Browse", command=lambda: action("browse_file"), width=160, height=25,
                     font=('Helvetica', 15, 'bold'), corner_radius=25, bg_color='#00182a', fg_color='#0d326e',image=image)
    but3.place(x=375, y=340)

    global lb5
    lb5 = CTkLabel(root, text="output stego image :", height=255, width=255, font=('Helvetica', 20),
                   bg_color='#ADC7E5', text_color="black")
    lb5.place(x=605, y=60)

    options = ["LSB", "DCT"]
    global combo_box
    combo_box = CTkOptionMenu(root, values=options, width=140, height=30, bg_color='#011828')
    combo_box.place(x=380, y=415)


    global but4
    but4 = CTkButton(root, text="Apply", command=lambda:Apply(radvar.get()), width=175, height=45, font=('Helvetica', 20, 'bold'),
                     bg_color='#011121', fg_color='#0d326e',image=image1,corner_radius=15)
    but4.place(x=360, y=510)
    ho.CreateToolTip(but4, 'processed image stegno')

    radvar=customtkinter.StringVar(value="other")
    rad = CTkRadioButton(root, text="Encode", value="Encode", width=100, height=20,
                         corner_radius=25, bg_color='#01192a', font=('Helvetica', 15, 'bold'),
                         text_color='white',variable=radvar,fg_color="blue",command=lambda:action("Encode"))
    rad.place(x=250, y=420)

    rad1 = CTkRadioButton(root, text="Decode", value="Decode", width=100, height=20,
                          corner_radius=25, bg_color='#011423', font=('Helvetica', 15, 'bold'),
                          text_color='white',variable=radvar,fg_color="blue",command=lambda:action("Decode"))
    rad1.place(x=580, y=420)

    root.mainloop()
