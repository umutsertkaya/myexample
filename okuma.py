import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"\Tesseract-OCR\tesseract.exe"

yazi = [pytesseract.image_to_string(Image.open("your photo adress"))]



text =  [] 



k = []
for i in yazi[:]:
    dosya = open("your output .txt file adress and name", "w", encoding="utf-8")
    
    i.strip("\n")
    print(i)
    
    for word in i:
        word.split("\n")
        dosya.writelines(word)
    dosya.close()

ok = open("your output .txt file adress and name", "r", encoding="utf-8")
text2 = []
for i2 in ok:
    text2.append(i2)



while (i2.count(" ")):
    i2.remove(" ")

ok.close()
    



    

