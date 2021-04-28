import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time
from gtts import gTTS
import os

custom_config=r'--oem 3 --psm 6'
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('text4.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
text=pytesseract.image_to_string(img)
print(text) 
myobj = gTTS(text=text, lang='en', slow=False)
myobj.save("welcome.mp3")
# Playing the converted file
os.system(" welcome.mp3")
hImg, wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    #print(b)
    b = b.split(' ')
    #print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
    cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
    boxes = pytesseract.image_to_data(img)
cv2.imshow('img', img)
cv2.waitKey(0)
