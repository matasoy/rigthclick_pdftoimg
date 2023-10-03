from pdf2image import convert_from_path
import sys #to get parameter from bat file
from io import BytesIO
import win32clipboard
from PIL import Image

yol = sys.argv[1]
print(yol)

pdf_images = convert_from_path(yol)
say=0
for idx in range(len(pdf_images)):
    say=say+1
    pdf_images[idx].save('pdf_page_'+ str(idx+1) +'.png', 'PNG')
    if say==1:
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