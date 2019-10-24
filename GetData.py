# This script get all data coming from STAI Google Forms,
# video source and HR sensor from STM32
# Draft version 0.0.1
# Date: October 22, 2019
# Author: Hector Morales
# Academic Stress Identification Platform v1.0.0

import webbrowser
import requests
import numpy as np
import cv2
import time

def videorecorder(filename):
    timeout = time.time() + 10   # In seconds 60*2 minutes from now
    start_time = time.time()
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # Define the codec and create VideoWriter object
    videofile =str(filename) + '-001' + '.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(videofile,fourcc, 30.0, (640,480))

    #while(cap.isOpened()):

    while True:
        if time.time() > timeout:
            break
        ret, frame = cap.read(cv2.CAP_DSHOW)
        if ret==True:
            #frame = cv2.flip(frame,0)

            # write the flipped frame
            out.write(frame)

            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()

error =1
while (error==1):
    matricula = input("Ingresa tu numero de matrícula (7 dígitos): ")
    try:
        val = int(matricula)
        error = 0
    except ValueError:
        print("ERROR!!")
        print("La matrícula debe ser numérica")

print ("Tu matrícula es: ",matricula)
print ("Un momento por favor a que el browser se abra...")

res = requests.get("https://forms.gle/JY2kvZF53axPzYTs8")
code = res.status_code
if (code==200):
    webbrowser.open_new("https://forms.gle/JY2kvZF53axPzYTs8")
    print("Sleep  - 30 segundos")
    #time.sleep(30)
    print("Start video recording of ",str(matricula)+'-001'+'.mp4')
    videorecorder(matricula)
    print("Recording is good!")
else:
    print("Existió un error al abrir la página, por favor pide ayuda")
