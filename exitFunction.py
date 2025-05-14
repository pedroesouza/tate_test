import cv2
import pygame
from pygame import mixer 
import time

def exitFunction():

    time.sleep(1)

    # Starting the mixer 
    mixer.init() 
    
    # Loading the song 
    mixer.music.load("Bye Bye Bye Audio.mp3") 
    
    # Setting the volume 
    mixer.music.set_volume(0.7) 
    
    # Start playing the song 
    mixer.music.play() 


    cap = cv2.VideoCapture("Bye Bye Bye x2 Speed.mp4")
    success, img = cap.read()
    shape = img.shape[1::-1]
    wn = pygame.display.set_mode(shape)
    clock = pygame.time.Clock()

    while success:
        clock.tick(60)
        success, img = cap.read()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                success = False
        wn.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))
        pygame.display.update()

    pygame.quit()
    
exitFunction()