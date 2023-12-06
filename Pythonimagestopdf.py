from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

dosya_konumu=""

def dosya_sec():
    global dosya_konumu
    dosya_konumu = filedialog.askdirectory()
    if dosya_konumu:
        label_konum.config(text="Seçilen Klasör Konumu: " + dosya_konumu)
def imagestopdf():
    if(dosya_konumu!=""):
        def find_image_files(directory, extensions):
            image_files = []
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if any(file.endswith(ext) for ext in extensions):
                        image_files.append(os.path.join(root, file))
            return image_files

        image_extensions = (".jpg", ".jpeg", ".png", ".gif")  # Resim dosyası uzantıları
        image_files = find_image_files(dosya_konumu, image_extensions)

        imgclr=[]
        for image_list in image_files:
            img=Image.open(image_list)
            imgclr.append(img.convert('RGB'))
            print(image_list)

        imgclr[0].save(dosya_konumu.split('/')[len(dosya_konumu.split('/'))-1]+".pdf", save_all=True, append_images=imgclr[1:])

        ana_pencere.destroy()


ana_pencere = tk.Tk()
ana_pencere.title("Dosya Seçme Uygulaması")

label_konum = tk.Label(ana_pencere, text="")
label_konum.pack()

buton = tk.Button(ana_pencere, text="Dosya Seç", command=dosya_sec)
buton.pack()

buton1 = tk.Button(ana_pencere, text="Pdf çevir", command=imagestopdf)
buton1.pack()

ana_pencere.mainloop()




    
