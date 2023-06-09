#Thanks for using my code!
#If you receive an error regarding no module 'PIL' please install Pillow into your cmd or shell. 
#pip install Pillow 


import tkinter as tk
import qrcode
from PIL import ImageTk, Image
import time

root = tk.Tk()
root.title('QR Code Generator')
root.geometry("450x420")
root.config(bg="#2c3e50")

# root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


def create_QR(link_input):
    print(link_input.get())
    lnk = link_input.get()
    global qr_img
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=3)
    qr.add_data(lnk)
    qr.make(fit=True)

    time_str = str(int(time.time()))
    img = qr.make_image(fill_color='cyan', back_color='#2c3e50')
    img.save(f'qrcode_{time_str}.png')
    qr_img = f'qrcode_{time_str}.png'
    return qr_img


def show_qr():
    global qr_img
    qr_img = ImageTk.PhotoImage(Image.open(qr_img))

    qr = tk.Label(frame, image=qr_img)
    qr.grid(row=3, columnspan=3, padx=5, pady=5)
    qr.config(image=qr_img)
    return qr_img


l1 = tk.Label(root, text="Welcome to QR Code Generator", font=("Calibre", 16), bg="#2c3e50", fg="white")
l1.grid(row=0, columnspan=2, padx=5, pady=5)

frame = tk.Frame(root)
frame.grid()
frame.config(bg="#2c3e50")

l2 = tk.Label(frame, text="Link you want as a QR Code: ", bg="#2c3e50", fg="white")
l2.grid(row=1, column=1, padx=5, pady=5, sticky="w")

link_name = tk.StringVar(frame, value='https://')
e1 = tk.Entry(frame, textvariable=link_name, width=35)
e1.grid(row=1, column=2, padx=5, pady=5)

b_cre = tk.Button(frame, text='Create QR Code', command=lambda: create_QR(link_name))
b_cre.grid(row=2, column=1, padx=5, pady=5)

b_sav = tk.Button(frame, text='Show QR Code', command=show_qr)
b_sav.grid(row=2, column=2, padx=5, pady=5)

root.mainloop()
