import mysql.connector
import cv2
import numpy as np
import requests
import io
import json
import pyttsx3
from datetime import date
from datetime import time
from datetime import datetime 
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
while True:
    try:
        check, frame = webcam.read()
        print(check) #prints true as long as the webcam is running
        print(frame) #prints matrix values of each framecd 
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 28x28 scale...")
            img_ = cv2.resize(gray,(28,28))
            print("Resized...")
            img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
            print("Image saved!")
        
            break
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
    
img = cv2.imread("saved_img.jpg")
height, width, _ = img.shape

# Cutting image
# roi = img[0: height, 400: width]
roi = img

# Ocr
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpg", roi, [1, 90])
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api,
              files = {"screenshot.jpg": file_bytes},
              data = {"apikey": "helloworld",
                      "language": "eng"})

result = result.content.decode()
result = json.loads(result)

parsed_results = result.get("ParsedResults")[0]
text_detected = parsed_results.get("ParsedText")
print(text_detected)
#this is

cv2.imshow("roi", roi)
cv2.imshow("Img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="")
mycursor=mydb.cursor()
parking=[i for i in range(1,20)]
real_parking=[1,2,3,4]
print(parking)
print(real_parking)
#print(lenght_parking)
#print(length_real_parking)
for i in range(10):
	rel=1
	for j in range(4):
		if parking[i]==real_parking[j]:
				rel=2
	if rel==1:
		parking_no2=parking[i]
		break
parking_no1=str(parking_no2)
#mycursor.execute("CREATE TABLE user_data(user_name VARCHAR(234),plate_no1 VARCHAR(234),this1_time VARCHAR(234),this1_date VARCHAR(234),parking_no VARCHAR(12))")
name=str(input("enter ur name:"))
#plate_no=str(input("enter ur plate:"))
#parking,name,plate_no,date that
this_time=datetime.time(datetime.now())
this_date=datetime.date(datetime.now())
val=(name,text_detected,this_time,this_date,parking_no1)
mycursor.execute("use garage")
sql="INSERT INTO user_data(user_name,plate_no1,this1_time,this1_date,parking_no)VALUES(%s,%s,%s,%s,%s)"
mycursor.execute(sql,val)
mydb.commit()
engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
	engine.say(audio)
	engine.runAndWait()
a1='hello  '
a2='  my  name  is    shilpa'
this123=a1+name+a2
speak(this123)
a3='your    plate    number'
a4='parking  number'
a5=a3+parking_no1+a4
speak(a5)
#speak("you can place ur bike on {}parking number",parking_no1)
speak("thankyou")
#here is the speak function call 
print("this is the someone")
#parking_no
