import time
import pygame
import cv2
import numpy as np



# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


#Adaptive thresholding
def thresholding(image):
    img = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)


# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)


# skew correction
def deskew(image, angle):
    # coords = np.column_stack(np.where(image > 0))
    # angle = cv2.minAreaRect(coords)[-1]
    # if angle < -45:
    #     angle = -(90 + angle)
    # else:
    #     angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated



day_dict = {
    "01": "./audio/1.mp3",
    "1": "./audio/1.mp3",
    "02": "./audio/2.mp3",
    "2": "./audio/2.mp3",
    "03": "./audio/3.mp3",
    "3": "./audio/3.mp3",
    "04": "./audio/4.mp3",
    "4": "./audio/4.mp3",
    "05": "./audio/5.mp3",
    "5": "./audio/5.mp3",
    "06": "./audio/6.mp3",
    "6": "./audio/6.mp3",
    "07": "./audio/7.mp3",
    "7": "./audio/7.mp3",
    "08": "./audio/8.mp3",
    "8": "./audio/8.mp3",
    "09": "./audio/9.mp3",
    "9": "./audio/9.mp3",
    "10": "./audio/10.mp3",
    "11": "./audio/11.mp3",
    "12": "./audio/12.mp3",
    "13": "./audio/13.mp3",
    "14": "./audio/14.mp3",
    "15": "./audio/15.mp3",
    "16": "./audio/16.mp3",
    "17": "./audio/17.mp3",
    "18": "./audio/18.mp3",
    "19": "./audio/19.mp3",
    "20": "./audio/20.mp3",
    "21": "./audio/21.mp3",
    "22": "./audio/22.mp3",
    "23": "./audio/23.mp3",
    "24": "./audio/24.mp3",
    "25": "./audio/25.mp3",
    "26": "./audio/26.mp3",
    "27": "./audio/27.mp3",
    "28": "./audio/28.mp3",
    "29": "./audio/29.mp3",
    "30": "./audio/30.mp3",
    "31": "./audio/31.mp3"
}

month_dict = {
    "01": "./audio/Jan.mp3",
    "1": "./audio/Jan.mp3",
    "02": "./audio/Feb.mp3",
    "2": "./audio/Feb.mp3",
    "03": "./audio/March.mp3",
    "3": "./audio/March.mp3",
    "04": "./audio/April.mp3",
    "4": "./audio/April.mp3",
    "05": "./audio/May.mp3",
    "5": "./audio/May.mp3",
    "06": "./audio/June.mp3",
    "6": "./audio/June.mp3",
    "07": "./audio/Jul.mp3",
    "7": "./audio/Jul.mp3",
    "08": "./audio/Aug.mp3",
    "8": "./audio/Aug.mp3",
    "09": "./audio/Sep.mp3",
    "9": "./audio/Sep.mp3",
    "10": "./audio/Oct.mp3",
    "11": "./audio/Nov.mp3",
    "12": "./audio/Dec.mp3"
}

year_dict = {
    "2021": "./audio/2021.mp3",
    "2022": "./audio/2022.mp3",
    "2023": "./audio/2023.mp3",
    "2024": "./audio/2024.mp3",
    "21": "./audio/2021.mp3",
    "22": "./audio/2022.mp3",
    "23": "./audio/2023.mp3",
    "24": "./audio/2024.mp3"
}

# play audio
def play_audio(flag, path):
    if flag:
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
         continue

##split by /
def split_date(date):
    date_array = date.split('/')
    return date_array

def voice_indicator(dictionary, index):
    flag = True
    play_audio(flag, dictionary[index])


def read_digit_date(detected_date):
    date_array = split_date(detected_date)
    day = date_array[0]
    month = date_array[1]
    if int(day) < 32 and int(month) < 13:
        voice_indicator(day_dict, day)
        voice_indicator(month_dict, month)
        if len(detected_date.split('/')) > 2:
            year = date_array[2]
            if (int(year) < 25 and int(year) > 20) or (int(year) < 2025 and int(year) > 2020):
                voice_indicator(year_dict, year)