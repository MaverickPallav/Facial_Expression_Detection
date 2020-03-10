from src.pre import facecrop
import cv2
import csv
import time
from src.cam import takeSnap
from src.cam import DisplayCamera
from keras.models import load_model

from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

import numpy as np
import matplotlib.pyplot as plt

countdown = 10;

DisplayCamera()
file = "snap.jpg"

f = open("mycsv.csv","w")
f.truncate()
f.close()

def emotion_analysis(emotions):
    objects = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
    y_pos = np.arange(len(objects))

    plt.bar(y_pos, emotions, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('percentage')
    plt.title('emotion')
    with open('mycsv.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)

        thewriter.writerow(objects)
        thewriter.writerow(emotions)

    plt.show()


while countdown > 0:
    time.sleep(1)
    print(countdown)
    countdown -= 1
    if countdown == 0:
        takeSnap()
        file = "snap.jpg"
        countdown = 10
        model = load_model('models/model.h5')
        # file = 'photo.jpg'
        # true_image = image.load_img("images/CROPPED"+file)
        img = image.load_img("images/CROPPED" + file, color_mode="grayscale", target_size=(48, 48))

        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)

        x /= 255

        custom = model.predict(x)
        emotion_analysis(custom[0])

    if facecrop(file) != 1:
        print("unable to crop")
        takeSnap()
        file = "snap.jpg"
        model = load_model('models/model.h5')
        # file = 'photo.jpg'
        # true_image = image.load_img("images/CROPPED"+file)
        img = image.load_img("images/CROPPED" + file, color_mode="grayscale", target_size=(48, 48))

        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)

        x /= 255

        custom = model.predict(x)
        emotion_analysis(custom[0])



    # if (cv2.waitKey(100) & 0xff == ord('q')):

    # break

    '''while True:
    print("Enter : \n")
    print("1. Input the name of the file in /image folder to process\n")
    print("2. Take snap from webcam\n")

    i = int(input())
    if (i == 2):
        takeSnap()
        file = "snap.jpg"
    else:
        file = input("Enter the name of file : ")

    # webcam.takeFrame()
    if (facecrop(file) != 1):
        print("Unable to crop image")
        exit()
    model = load_model('models/model.h5')
    # file = 'photo.jpg'
    # true_image = image.load_img("images/CROPPED"+file)
    img = image.load_img("images/CROPPED" + file, color_mode="grayscale", target_size=(48, 48))

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    x /= 255

    custom = model.predict(x)
    emotion_analysis(custom[0])
    print("Enter 1 to try again and 0 to exit : ")
    t = int(input())
    if (t == 0):
        break'''

# x = np.array(x, 'float32')
# x = x.reshape([48, 48]);

# plt.gray()
# plt.imshow(true_image)
# plt.show()
