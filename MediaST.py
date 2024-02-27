from tkinter import *
from customtkinter import *
from PIL import Image
import hover as ho
import tkinter as tk


def back():
    pro.destroy()
    main_9()

def about():
    root.destroy()
    about_page()

def gohome():
    root.destroy()
    from HomePage import page_English
    page_English()


def action(num):
    root.destroy()  # Hide the root window
    if num == 1:
        import ImagePage
        ImagePage.display()
    elif num == 2:
        import VideoPage
        VideoPage.display()
    elif num == 3:
        import AudioPage
        AudioPage.display()
    else:
        import TextPage
        TextPage.display()


def main_9():
    global root
    root = CTk()
    root.title('Steganography of media')
    root.geometry("900x600+400+100")
    root.resizable(False, False)
    root.iconbitmap('icons/hider.ico')

    image = CTkImage(dark_image=Image.open("img2.png"), size=(900, 600))
    lab9 = CTkLabel(root, image=image, text="", font=('Helvetica', 30, 'bold'))
    lab9.place(x=0, y=0)

    image2 = CTkImage(dark_image=Image.open("icons/back.ico"), size=(15, 15))
    image1 = CTkImage(dark_image=Image.open("icons/text.ico"), size=(20, 20))
    image3 = CTkImage(dark_image=Image.open("icons/audio.ico"), size=(20, 20))
    image4 = CTkImage(dark_image=Image.open("icons/video.ico"), size=(20, 20))
    image5 = CTkImage(dark_image=Image.open("icons/img.ico"), size=(20, 20))
    image6 = CTkImage(dark_image=Image.open("icons/about.ico"), size=(20, 20))

    lab1 = CTkLabel(root, text="Select Media Type", font=('Helvetica', 25, 'bold'), bg_color='#000e17')
    lab1.place(x=320, y=115)

    but1 = CTkButton(root, text="Image", command=lambda: action(1),image=image5,
                     width=180, height=45, font=('Helvetica', 21, 'bold'), corner_radius=15, bg_color='#021422',
                     fg_color='#0d326e')
    but1.place(x=195, y=230)
    ho.CreateToolTip(but1, 'hide data into image with 2 techniques')

    but2 = CTkButton(root, text="Video", command=lambda: action(2),image=image4,
                     width=180, height=45, font=('Helvetica', 21, 'bold'), corner_radius=15, bg_color='#011423',
                     fg_color='#0d326e')
    but2.place(x=490, y=360)
    ho.CreateToolTip(but2, 'hide data into video')

    but3 = CTkButton(root, text="Audio", command=lambda: action(3),image=image3,
                     width=180, height=45, font=('Helvetica', 21, 'bold'), corner_radius=15, bg_color='#000d16',
                     fg_color='#0d326e')
    but3.place(x=490, y=230)
    ho.CreateToolTip(but3, 'hide data into audio with 2 techniques')

    but4 = CTkButton(root, text="Text", command=lambda: action(4),image=image1,
                     width=180, height=45, font=('Helvetica', 21, 'bold'), corner_radius=15, bg_color='#01182a',
                     fg_color='#0d326e')
    but4.place(x=195, y=360)
    ho.CreateToolTip(but4, 'hide data into text with 3 techniques')

    bt5 = CTkButton(root, text='Back', command=gohome
                    , width=150, height=30, font=('Helvetica', 15, 'bold'), corner_radius=10, bg_color='#021826',
                    fg_color='#0d326e', image=image2)
    bt5.place(x=10, y=15)

    bt6 = CTkButton(root, text='Info'
                    , width=150, height=30, font=('Helvetica', 15, 'bold'), corner_radius=10, bg_color='#011c2f',
                    fg_color='#0d326e', command=about,image=image6)
    bt6.place(x=170, y=15)
    ho.CreateToolTip(bt6, 'advantage and disadvantage about all algorithm techniques used  ')
    root.mainloop()


def about_page():
    global pro
    pro = CTk()  # Assuming CTk is a custom tkinter class
    pro.geometry('900x600+400+100')
    pro.title('About')
    pro.resizable(FALSE, FALSE)
    pro.iconbitmap('icons/hider.ico')

    # Assuming you have defined CTkImage class for displaying images
    My_image = CTkImage(dark_image=Image.open("img2.png"), size=(900, 600))
    lab11 = CTkLabel(pro, image=My_image, text="", font=('Helvetica', 30, 'bold'))
    lab11.place(x=0, y=0)

    # Assuming you have defined CTkButton class
    bt9 = CTkButton(pro, text='Back', width=150, height=30, font=('Helvetica', 15, 'bold'), corner_radius=50,
                    bg_color='#051021', fg_color='#0d326e', command=back)
    bt9.place(x=10, y=15)

    # Add text widget for steganography techniques
    steganography_text = """
    LSB (Least Significant Bit) Steganography:
    Advantages:
    High Payload Capacity: Can modify multiple bits per pixel, allowing for a higher payload.
    Low Visibility: When done carefully, changes may not significantly alter the visual appearance.
    Robustness: Can be robust against common image processing operations.
    Disadvantages:
    Low Robustness Against Attacks: Vulnerable to various attacks, such as histogram and statistical analysis.
    Susceptibility to Lossy Compression: May not withstand lossy compression well.
    Limited Embedding Capacity: Might not be sufficient for applications requiring very high data capacity.
    Sensitivity to Noise: Can be sensitive to noise in the image.

    DCT (Discrete Cosine Transform) Steganography:
    Advantages:
    Robustness Against Compression: More robust against lossy compression compared to LSB.
    Higher Security: Operates in the frequency domain, making it less susceptible to simple analyses.
    Improved Payload Capacity: Can hide more data with a lower likelihood of visual detection.
    Less Susceptible to Visual Inspection: Changes may be less noticeable to the human eye.
    Disadvantages:
    Complexity: More complex implementation compared to LSB methods.
    Susceptibility to Advanced Attacks: Still susceptible to advanced steganalysis techniques.
    Limited Robustness: May not be robust against certain image processing operations or attacks.
    Dependency on Compression Settings: Effectiveness can be influenced by compression settings.

    Phase-Based Audio Steganography:
    Advantages:
    Robustness Against Compression: More robust against compression compared to amplitude-based techniques.
    Increased Security: Less susceptible to traditional audio steganalysis methods.
    Potential for High Payload: Can offer a higher payload capacity.
    Disadvantages:
    Complexity: More complex implementation compared to basic amplitude-based techniques.
    Sensitivity to Signal Processing: Embedded information may be sensitive to certain signal processing operations.
    Limited Robustness: Not immune to all types of signal processing and attacks.
    Auditory Perception Considerations: Potential for audible artifacts or degradation in audio quality.

    LSB Audio Steganography:
    Advantages:
    Low Visibility: When done carefully, modifications may not be easily perceptible.
    Ease of Implementation: Does not require advanced signal processing knowledge.
    Potential for High Payload: Can provide a relatively high payload capacity.
    Disadvantages:
    Susceptibility to Attacks: Vulnerable to statistical analysis and changes in amplitude.
    Low Robustness: May not be robust against common audio processing operations.
    Risk of Auditory Artifacts: Modifying least significant bits may introduce audible artifacts.
    Limited Embedding Capacity: May not be sufficient for applications requiring very high data capacity.
    Dependence on Audio Format: Effectiveness may depend on the audio file format used.

    ZWC (Zero-Width Characters) Steganography:
    Advantages:
    Invisibility: Designed to be invisible to the human eye, providing stealth.
    Camouflage: Hides information within non-visible characters, making detection difficult.
    Variety of Characters: Multiple zero-width characters available for embedding data.
    Applicability to Various Textual Content: Can be applied to various types of text, including code, prose, and social media posts.
    Disadvantages:
    Vulnerability to Detection: Specialized tools or algorithms may detect the presence of hidden information.
    Limited Payload Capacity: Limited by the number and arrangement of zero-width characters.
    Potential for Misuse: Potential for misuse for hiding malicious or unauthorized information.
    Encoding Challenges: Requires careful encoding and decoding for accurate extraction.
    Compatibility and Display Issues: Display of zero-width characters may not be consistent, leading to compatibility and display issues.
    Risk of Collisions: Limited set of zero-width characters may result in collisions, causing potential data corruption.

    Letter Case Steganography:
    Advantages:
    Invisibility: Changes are often less noticeable than other modifications to text.
    Ease of Implementation: Straightforward implementation without specialized tools.
    Applicability to Natural Language: Seamless application to natural language text.
    Disadvantages:
    Limited Payload Capacity: Limited by the number of letters and chosen encoding
    Whitespace in Text:
    Advantages:
    Readability: Enhances readability by visually separating different parts of text.
    Aesthetics: Contributes to the overall aesthetics of a document or user interface.
    Separation of Elements: Used to separate elements in a document for better organization.
    Preventing Line Wrap Issues: Helps prevent undesirable line wrap issues.
    Responsive Design: Aids in responsive layouts in web design.
    Disadvantages:
    Overuse: Excessive use can lead to wasted space and longer documents.
    Inconsistent Use: Inconsistency in usage can create confusion.
    Potential for Ambiguity: Careless use may alter the meaning of sentences or code.
    Increased File Size: Excessive use in web development may contribute to larger file sizes.
    Challenges in Data Processing: Extraneous whitespace can pose challenges in data processing.
    Accessibility Concerns: Excessive whitespace may affect accessibility for some users.
    """
    steganography_text_widget = CTkTextbox(pro, wrap="word", width=800, height=530, font=('Helvetica', 12,"bold"),fg_color="white",text_color="black")
    steganography_text_widget.insert(tk.END, steganography_text)
    steganography_text_widget.place(x=50, y=50)


    pro.mainloop()  # Run the tkinter event loop for this window



if __name__ == "__main__":
    main_9()
