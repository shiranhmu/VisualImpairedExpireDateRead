# IndepanDate


Technology development project of reading the expiration date of products for the visually impaired. Performed as part of a final project for a degree in Industrial Engineering and Management at Ben Gurion University of the Negev.     
watch how to use on https://youtube.com/shorts/A0soGtdeD8A?feature=share
## Introduction

Each food package has its expiration date beyond which it is not recommended consuming it. While most visually impaired people can easily check the expiration date before using the product, for the visually impaired it is very difficult to do so independently, if at all. Visually impaired people can use human assistance to know the expiration date of the product but such assistance is not always available.
In this project, a prototype was characterized and developed for a system that reads the expiration date of food products for the visually impaired. The prototype is a handheld device adapted for the visually impaired and contains a Raspberry Pi 4 computer and a camera for scanning the expiration date of the products. The system detects the validity date using image processing technology and Optical Character Recognition (OCR) in the Python code language. The system has a power button on and off of the device and a scan button which is located parallel to the camera viewfinder to make it easier for the visually challenged to aim the camera. Once the date is identified the system will read it aloud using a small speaker component that connects to the Raspberry Pi 4 card. The developed system aims to enable the visually impaired to perform such a routine task in daily life independently.

The code on Github has five major files:

1. Main2 - A Python file which is responsible for the scan. After pressing the scan button, gives an audio indication "start scan". The system then searches for the expiration date on the product using the pytesseract package. A search is performed for a date in the dd / mm or dd / mm / yy or dd / mm / yyyy format, which is known in dairy products in Israel. Once the date is identified, the system will refer to the Python file "Functions" which will read the appropriate expiration date.
2. Functions - A python file containing the functions called from the main program. Functions of image processing, audio playback and date reading.
3. Buttons - A python file which is responsible for running the main program for scanning the expiration date when the scan button is clicked. Turns off the scan program when pressed again.
4. Audio files folder- Contains the audio files of the dates and the start of the scan.



## Main Packages

 

*Pytesseract* -- <br>

Python-tesseract is an optical character recognition (OCR) tool for python. Python-tesseract is an optical character recognition (OCR) tool for Python. It will recognize the date format and perform a transformation from text embedded in images to digital text.

<br>

Python-tesseract is a wrapper for Google’s Tesseract-OCR Engine. It is also useful as a stand-alone invocation script to tesseract, as it can read all image types supported by the Pillow and Leptonica imaging libraries, including jpeg, png, gif, bmp, tiff, and others.

<br>

The experiments show that a lot of numbers and expiration dates are particularly difficult for off-the-shelf OCR engines, such as Tesseract, to read because they are usually written in a dot-matrix font that varies widely from product to product. For example, Tesseract and the Google Text Detection API achieve a 55% and 60% character accuracy, respectively, on dot matrix fonts.

<br>

The time period for implementing the project in machine learning is much larger than what was allocated to us within the time frame of the project. Therefore, OCR technology is used. Technology has helped us identify numbers and dates by format.

*CV2* -- <br>

OpenCV (open source computer vision library) is a library of programming functions aimed primarily at real-time computer vision. Main functions:

1. Ability to perform various manipulations on images (image processing).

2. Identify objects in the image.

3. Traffic tracking.

4. Identify human indications.

<br>

In this project, this library is mainly used with filters like get_grayscale, bitwise_not, thresholding for image processing for better identification of the expiration date.

 *Pygame* -- <br>

The pygame library is an open-source module for the Python programming language specifically intended to help make games and other multimedia applications. Built on top of the portable SDL (Simple DirectMedia Layer) development library.This module contains classes for loading Sound objects and controlling playback.

## HardWare

In order to assemble the 'Independent.Date' device, the hardware required for purchase consists of:

* **Raspberry pi 4** --<br>
Raspberry pi is a low cost, credit-card sized computer that plugs into a computer monitor or TV, and uses a standard keyboard and mouse. Raspberry pi 4 is a completely upgraded and re-engineered dual 4k display computer offered in 2GB, 4GB, or 8GB of RAM. It boasts an updated 64-bit quad-core processor running at 1.4GHz. The Pi 4 B features 2 micro HDMI 
* **Original camera for 8MP card** -- <br>
The camera is capable of taking still images with a resolution of up to 2464x3280 and a film with resolutions up to 1080p.30. It also includes automatic control functions such as exposure control, white balance and brightness detection.
* **Memory Card - SD micro** --<br>
16GB memory, used as storage of the PI. These cards are easy to use thanks to the SPI communication supported by the microcontrollers.
* **Li-ion Battery HAT** -- <br>
integrates the SW6106 power bank management chip, providing 5V regulated power supply to your Pi from a 14500 battery, turning your Pi into a portable device! It will charge the battery and supports bi-directional quick charge.
* **Battery** -- <br>
Applicable battery: 3.7V 14500 lithium battery (4.2V when full charged).
* **Buttons and pins** --<br>
1. power button - PIN GPIO3 - SCL1 - 12C + Ground. size 12 mm.
2. scan button - PIN GPIO17 + Ground. size 20 mm.
![alt text](https://i.ibb.co/McQGrHj/PINS.jpg)
* **Speaker** -- <br>
A small voice amplifier on a module with a connection to the Grove system of the SeeedStudio company.
Provides the module with signals at different frequencies and you can play basic sounds and music.
* **3D model** -- <br> 
The model is ergonomically designed to fit the shape of the palm considering that the hand will not obscure the camera viewfinder. The scan button is located parallel to the camera viewfinder so that it gives the user an indication of where the camera is facing. The model has a side opening for connecting the charger.
1. Sketches: <br>
![alt text](https://i.ibb.co/Gc2XyZC/image.png)

2. SolidWork: <br>
![alt text](https://i.ibb.co/BCc5RRB/PHOTO-2022-06-10-13-45-01.jpg)
![alt text](https://i.ibb.co/smZkF0z/PHOTO-2022-06-10-13-45-02.jpg)
![alt text](https://i.ibb.co/ysH3v08/PHOTO-2022-06-10-13-45-02-1.jpg)
