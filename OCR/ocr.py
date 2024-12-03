import pytesseract
from PIL import Image

import pytesseract
import os

# تحديد المسار إلى tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# تحديد مسار tessdata
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'


# تحديد المسار إلى tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# تحميل الصورة التي تحتوي على النصوص
image_path = 'Screenshot 2024-05-13 130100.png'
image = Image.open(image_path)

# استخراج النصوص من الصورة
text = pytesseract.image_to_string(image)

# طباعة النص المستخرج
print("النص المستخرج من الصورة:")
print(text)
text = pytesseract.image_to_string(image, lang='ara')
print("النص المستخرج (باللغة العربية):")
print(text)


