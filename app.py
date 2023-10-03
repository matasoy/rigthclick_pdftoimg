from pdf2image import convert_from_path
import sys #to get parameter from bat file
from io import BytesIO
import win32clipboard
from PIL import Image
import tkinter as tk
from tkinter import simpledialog

yol = sys.argv[1]
print(yol)

pdf_images = convert_from_path(yol)
say=0
def winput(title, sentence):    
    tk.Tk().withdraw()
    y = simpledialog.askinteger(title, sentence)
    return y

x = winput("Hangi Sayfa", "Resim olarak kopyalayacağınız sayfa numarasını yazın.")


for idx in range(len(pdf_images)):
    say=say+1    
    if say==x:
        pdf_images[idx].save('pdf_page_'+ str(idx+1) +'.png', 'PNG')
        def send_to_clipboard(clip_type, data):
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(clip_type, data)
            win32clipboard.CloseClipboard()
        filepath = 'pdf_page_'+ str(idx+1) +'.png'
        image = Image.open(filepath)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        send_to_clipboard(win32clipboard.CF_DIB, data)
        print("İlk resim kopyalandı")
print("Successfully converted PDF to images")