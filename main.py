# Выражаю огромную благодарность автору канала PythonToday
# https://www.youtube.com/watch?v=UPjTYorn59g&list=PLqGS6O1-DZLoAADhgzzkvc8ifKsKG4G-T&index=4
# import pytesseract
# from PIL import Image
#
# img = Image.open('phone_1.png')
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#
# # точность  распознования, параметры config
# custom_config = r'--oem 3 --psm 13'
#
# text = pytesseract.image_to_string(img,  config=custom_config)
# print(text)
#
# with open('phone_1.txt', 'w') as text_file:
#     text_file.write(text)

# --------------------------------------------

import pytesseract
from PIL import Image

img = Image.open('i.png')

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

file_name = img.filename
file_name = file_name.split('.')[0]

custom_config = r'--oem 3 --psm 36'

text = pytesseract.image_to_string(img)
print(text)

with open(f'{file_name}.txt', 'w') as text_file:
    text_file.write(text)