# This script get all data coming from STAI Google Forms,
# video source and HR sensor from STM32
# Draft version 0.0.2
# Date: October 29, 2019
# Author: Hector Morales
# Academic Stress Identification Platform v1.0.0
# SXE END Exam

import webbrowser
import requests
import numpy as np
import cv2
import time

def videorecorder(filename):
    timeout = time.time() + 75   # In seconds 75 seconds from now
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    videofile =str(filename) + '-003' + '.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(videofile,fourcc, 20.0, (1280,720))

    #while(cap.isOpened()):

    while True:
        if time.time() > timeout:
            break
        ret, frame = cap.read()
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

res = requests.get("https://forms.gle/RHSKHRLqmw6YfiDu5")
code = res.status_code
if (code==200):
    webbrowser.open_new("https://forms.gle/RHSKHRLqmw6YfiDu5")
    print("Sleep  - 20 segundos")
    time.sleep(20)
    print("Start video recording of ",str(matricula)+'-003'+'.mp4')
    start_time = time.time()    #start timestamp
    videorecorder(matricula)
    stop_time = time.time()     #stop timestamp
    print("El archivo se generó correctamente")
else:
    print("Existió un error al abrir la página, por favor pide ayuda")
