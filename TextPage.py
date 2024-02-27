from tkinter import *
from tkinter import filedialog, messagebox
from customtkinter import *
from PIL import Image
from snow import encode_message,decode_message
import hover as ho
def info():
    messagebox.showinfo('Steganography', 'Successful Process')

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
            ent1.delete(0,"end")
            ent1.insert('end', file_path2)

    elif pointer=="browse_stegotext":
        file_path = filedialog.askopenfilename(title="Choose a Text file",
                                                filetypes=(("Text Files", "*.txt"),))
        text_box.delete(0.0, 'end')
        fhand= open(file_path, "r", encoding="utf-8")
        data=fhand.read()
        global remaining_chars,max_chars
        remaining_chars = max_chars - len(text_box.get("0.0", "end"))
        for ch in data:
            if remaining_chars>0:
                text_box.insert('end', ch)
                update_countdown()

def update_countdown(event=None):
    remaining_chars = max_chars - len(text_box.get("1.0", "end-1c"))
    countdown_label.configure(text=f"Characters remaining: {remaining_chars}", text_color="white")


max_chars = 2000


def Apply():
    secret = text_box.get(0.0, "end")
    secret=secret.strip()
    textfile=ent1.get()
    if len(textfile) > 0 :
        inp_dialog = CTkInputDialog(text="Enter encryption key \n default value 100")
        key = inp_dialog.get_input()
        process=combo_box.get()
        technique=combo_box1.get()
        if process =="Encode" and len(secret) >1:
            if technique == "WhiteSpace":
                encode_message(textfile,secret,key)
                info()
        else:
            if technique == "WhiteSpace":
                secret=decode_message(textfile,key)
                text_box.delete(0.0, "end")
                text_box.insert('end', secret)

def display():
    global root
    root = CTk()
    root.title('Text Steganography')
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
    lb3.place(x=315, y=65)

    global text_box
    text_box = CTkTextbox(root, width=270, height=200, corner_radius=25, border_width=3, wrap="word",
                          bg_color="#010f1a", border_color="#03002e", fg_color="white",text_color="black")
    text_box.place(x=305, y=100)
    global countdown_label
    countdown_label = CTkLabel(root, text=f"Max of charachter : {max_chars}", font=('Helvetica', 12,'bold'),
                               bg_color="#01192a")
    countdown_label.place(x=315, y=300)

    text_box.bind("<KeyRelease>", update_countdown)

    lb3 = CTkLabel(root, text="Choose file :", font=('Helvetica', 20,'bold'), bg_color='#01192a')
    lb3.place(x=150, y=380)

    global ent1
    ent1 = CTkEntry(root, width=180, height=20,
                         bg_color="#010f1a", fg_color="white", text_color="Red")
    ent1.place(x=310, y=380)

    but3 = CTkButton(root, text="Browse", command=lambda: action("browse_file"), width=50, height=25,
                     font=('Helvetica', 15, 'bold'), corner_radius=25, bg_color='#03002e', fg_color='#0d326e',image=image)
    but3.place(x=500, y=380)
    ho.CreateToolTip(but3, 'browse cover text file')

    but2 = CTkButton(root, text="Browse", command=lambda: action("browse_stegotext"), width=50, height=25,
                     font=('Helvetica', 15, 'bold'), corner_radius=25, bg_color='#001a29', fg_color='#0d326e',image=image)
    but2.place(x=350, y=340)
    ho.CreateToolTip(but2, 'browse secret text file')



    options = ["Encode", "Decode"]
    global combo_box
    combo_box = CTkOptionMenu(root, values=options, width=150, bg_color='#011828',font=('Helvetica', 13,'bold'))
    combo_box.place(x=195, y=435)

    options = ["WhiteSpace", "Letter Case"]
    global combo_box1
    combo_box1 = CTkOptionMenu(root, values=options, width=150, bg_color='#011828',font=('Helvetica',13,'bold'))
    combo_box1.place(x=475, y=435)

    global but4
    but4 = CTkButton(root, text="Apply", command=Apply, width=120, height=30, font=('Helvetica', 15,'bold'),
                     bg_color='#011828', fg_color='#0d326e', corner_radius=25,image=image1)
    but4.place(x=350, y=435)
    ho.CreateToolTip(but4, 'processed text stegno')

    root.mainloop()