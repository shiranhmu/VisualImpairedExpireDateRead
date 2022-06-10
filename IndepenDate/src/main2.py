import cv2
import pytesseract
import re
from pytesseract import Output
from datetime import datetime
import functions
import imutils




cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
try:
    #start scanning
    first_enter = True
    first_enter = functions.play_audio(first_enter, "/home/pi/Desktop/DateRecords/start_scan.mp3")
    start_time = datetime.now()
    # degree = 0
    index = 0

    while True:
        try:
            # Capture frame-by-frame
            ret, frame = cap.read()

            #Filter frame
            picture = functions.get_grayscale(frame)
            picture = cv2.bitwise_not(picture)
            picture = functions.thresholding(picture)
            #picture = functions.canny(picture)
            # degree += 5
            # if degree >= 360:
            #     degree = 0
            # skewed = imutils.rotate(picture, 14.74)
            # picture = deskew(skewed, degree)



            d = pytesseract.image_to_data(picture, output_type=Output.DICT)
            Description_pattern_yy = '(\d+/\d+/\d+)'
            Description_pattern_mm ='(3[01]|[12][0-9]|0[1-9])(.|-|\/)(1[0-2]|0[1-9])'
            Description_pattern_dm ='(3[01]|[12][0-9]|[1-9])(.|-|\/)(1[0-2]|[1-9])'
            n_boxes = len(d['text'])
            # digit accuracy index
            for j in range(n_boxes):
                if int(d['conf'][j]) > 60 :
                    digit_only = pytesseract.image_to_string(picture, config='outputbase digits')
                    if digit_only != "":
                        file = open('/home/pi/Desktop/digit_file.txt', "a")
                        print(f'digits: {digit_only}')
                        file.write(f'  {start_time} : digits for experiment {digit_only}\n')
                        file.close()

            #out algorithm
            for i in range(n_boxes):
                if int(d['conf'][i]) > 60:
                    if re.match(Description_pattern_yy, d['text'][i]) or re.match(Description_pattern_mm, d['text'][i]):
                        if len(d['text'][i].split('/')) > 1:
                            (text, x, y, w, h) = (d['text'][i], d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                            # don't show empty text
                            if text and text.strip() != "":
                                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                                conf = d["conf"][i]
                                detected_date = d['text'][i]
                                print(f'date is {detected_date} and conf is {conf}')
                                end_time = datetime.now()
                                functions.read_digit_date(detected_date)
                                index =+ 1
                                detect_time = (end_time-start_time).total_seconds()
                                file = open('/home/pi/Desktop/results.txt', "a")
                                file.write(f'{index} {start_time}: date is {detected_date} and conf is {conf} and time is {detect_time}\n')
                                file.close()
                                break

            # Display the resulting frame
            # print("test")
            cv2.imshow('frame', picture)



            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except Exception as e:
            file = open('/home/pi/Desktop/test.txt', "a")
            file.write("e")
            file.close()

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
except Exception as e:
    file = open('/home/pi/Desktop/test.txt', "a")
    file.write("e")
    file.close()


