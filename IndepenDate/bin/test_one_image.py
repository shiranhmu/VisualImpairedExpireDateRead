import os
import re
import cv2
import copy
import pytesseract



def run_tesseract_on_image(args, frame):
    '''
    runs the pytesseract on a single frame
    :param args: system arguments, should contain87
        conf_thresh - the algo minimum confidence threshold
        date_pattern - what pattern to find using the tesseract
    :param frame: the image to run on, should be a cv2 image
    :return: a dictionary of results containing the dates, cropped images, and confidence thresholds
    '''
    image = copy.deepcopy(frame)
    if args.debug:
        cv2.imshow('', image)
        print("test2")
        cv2.waitKey(0)
    print("are u out ?")
    d = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
    print('DATA KEYS: \n', d.keys())
    n_boxes = len(d['text'])
    results = {
        'date' : [],
        'images' : [],
        'threshold' : []
    }
    for i in range(n_boxes):
        print("are u in ?")
        if float(d['conf'][i]) > args.conf_thresh:
            # write your function here
            if re.match(args.date_pattern, d['text'][i]):
                if len(d['text'][i].split('/')) >=- 1:
                    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                    # no need for rectangle, just output the date
                    image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    crop_img = image[y:y + h, x:x + w]
                    cropped_image = cv2.imshow("cropped", crop_img)
                    results['date'].append(d['text'][i])
                    results['images'].append(cropped_image)
                    results['threshold'].append(d['conf'][i])
    return results



if __name__ =='__main__':
    import argparse
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    args.debug = False
    args.conf_thresh = 40
    args.date_pattern = '([0-9]+\/[0-9]+)|([0-9]+)|([0-9\,\.]+)'
    # image = cv2.imread('/home/pi/project/IndepanDate/date.jpg')
    results = run_tesseract_on_image(args, image)