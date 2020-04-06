import pytesseract as tess
tess.pytesseract.tesseract_cmd =r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open('C:\Users\PIYUSH\Desktop\judges.jpg')
text = tess.image_to_string(img)

print(text)