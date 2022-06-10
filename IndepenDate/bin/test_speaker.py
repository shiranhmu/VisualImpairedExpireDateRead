import pygame
#play audio
while True:
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Downloads/start_scan.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue