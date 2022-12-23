import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import tensorflow as tf
# import qrcode
import numpy as np
import re
from tensorflow import keras
from winsound import *
from tensorflow.keras.utils import load_img, img_to_array
new_model = tf.keras.models.load_model("C:\\Users\\mi591\\Downloads\\music\\Nhan_dang.h5")
def load_img():
    global img, image_data
    for img_display in frame.winfo_children():
        img_display.destroy()
    image_data = filedialog.askopenfilename(initialdir="/", title="Vui long chon anh de tim kiem",
                                            filetypes=(("all files", "*.*"), ("png files", "*.png")))
    basewidth =400
    img = Image.open(image_data)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel_image = tk.Label(frame, image=img).pack()
def classify():
    original = Image.open(image_data)
    original = original.resize((150, 150), Image.ANTIALIAS)
    numpy_image = img_to_array(original)
    image_batch = np.expand_dims(numpy_image, axis=0)
    # processed_image = new_model.preprocess_input(image_batch.copy())
    result = new_model.predict(image_batch)
    global prediction
    if round(result[0][0]) == 1:
        prediction = 'Sao truc'
    if round(result[0][1]) == 1:
        prediction = 'Song loan'
    if round(result[0][2]) == 1:
        prediction = "Da T'rung"
    if round(result[0][3]) == 1:
        prediction = 'Dan bau'
    if round(result[0][4]) == 1:
        prediction = 'Dan co'
    if round(result[0][5]) == 1:
        prediction = 'Dan nguyet'
    if round(result[0][6]) == 1:
        prediction = 'Dan sen'
    if round(result[0][7]) == 1:
        prediction = 'Dan tranh'
    if round(result[0][8]) == 1:
        prediction = 'Dan ti ba'
    if round(result[0][9]) == 1:
        prediction = 'Dan day'
    print('Day la:', prediction)
    print("Day la nhac cu :", str(prediction).upper())
    loainhaccu = tk.Label(wd, text=str(prediction).upper(), bg='aqua', fg='sienna', font=("", 24))
    loainhaccu.place(x=250, y=550)
    root = Tk()
    root.geometry('400x200')
    play = lambda: PlaySound("C:\\Users\\mi591\\Downloads\\music\\" + str(prediction) + ".wav", SND_FILENAME)
    button = Button(root,fg='sienna', bg='pink', text='Am thanh nhac cu', width=20,command=play)
    button.pack()
    root.mainloop()
wd = Tk()
wd.title(' NHAC CU VIETNAM  ')
wd.iconbitmap("C:\\Users\\mi591\\Downloads\\music")
wd.geometry('800x700')
wd.resizable(width=False, height=False)
Label01 = tk.Label(wd)
Label01["activebackground"] = "#58a5de"
Label01['font'] = ("Arial", 30)
Label01["fg"] = "#333333"
Label01['bg'] = 'yellow'
Label01["justify"] = "center"
Label01["text"] = "  NHAC CU DAN TOC VIET NAM "
Label01["relief"] = "flat"
Label01.place(x=30, y=0, width=600, height=50)
frame = Frame(wd)
frame['bg'] = 'aqua'
frame['bd'] =10
frame.place(x=200, y=60, width=400, height=400)
Label02 = tk.Label(wd)
Label02['font'] = ("Arial",16)
Label02["fg"] = "green"
Label02["justify"] = "right"
Label02["text"] = "Nhac cu nay la: "
Label02["relief"] = "flat"
Label02.place(x=40, y=500, width=200, height=95)
Button_01 = tk.Button(wd)
Button_01["bg"] = "pink"
Button_01['font'] = ("Arial",16)
Button_01["fg"] = "#000000"
Button_01["justify"] = "center"
Button_01["text"] = "CHON ANH"
Button_01.place(x=55, y=650, width=280,height=30)
Button_01["command"] = load_img
Button_02 = tk.Button(wd)
Button_02["bg"] = "cyan"
Button_01['font'] = ("Arial", 10)
Button_02["fg"] = "#000000"
Button_02["justify"] = "center"
Button_02["text"] = "KET QUA"
Button_02.place(x=30, y=600, width=266,height=30)
Button_02["command"] = classify
wd.mainloop()