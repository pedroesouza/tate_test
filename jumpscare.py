#PEDRO

#Import needed libraries
import pygame
import time
import sys

#Create the class that creates and runs the jumpscares
class Jumpscare:
    #Creates the variables from what was originally given
    def __init__(self, image, sound, text, boom):
        self.image = image
        self.sound = sound
        self.text = text
        self.boom = boom

    #This puts the image in the screen
    def jumpscare_run(self, screen):
        pygame.mixer.init()

        #Prepare image
        image_rect = self.image.get_rect(center=screen.get_rect().center)
        screen.blit(self.image, image_rect)
        pygame.display.update()

        #Play scary sound
        self.sound.play()
        time.sleep(7) # Wait 7 seconds

        #Make screen black
        screen.fill((0, 0, 0))
        pygame.display.update()

        #Show text
        font = pygame.font.Font(None, 64)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=screen.get_rect().center)
        screen.blit(text_surface, text_rect)
        pygame.display.update()


        self.boom.play() #Play sound 2


        time.sleep(3) #Wait 3 seconds

#This sets up the jumpscare stuff
def jumpscare_manager(type, screen):
    #Load images
    tateImage = pygame.image.load("Images\\tate_image.png").convert()

    cartiactImg = pygame.image.load("Images\cartiac.jpg").convert()
    cartiactImg = pygame.transform.scale(cartiactImg, (
        cartiactImg.get_width() * 6,
        cartiactImg.get_height() * 6
    ))

    deadPerson = pygame.image.load("Images\dead.jpg").convert()
    deadPerson = pygame.transform.scale(deadPerson, (
        deadPerson.get_width() * 4,
        deadPerson.get_height() * 4
    ))

    #Load sounds
    cartiac = pygame.mixer.Sound("Sounds\carti-scream.wav")
    deadJumpscareSound = pygame.mixer.Sound("Sounds\dead_sound.wav")
    tateJumpscareSound = pygame.mixer.Sound("Sounds\jumpscare_sound.wav")
    vineBoom = pygame.mixer.Sound("Sounds\\vine_boom.wav")

    #Choose scare based on type
    if type == "normal":
        scare = Jumpscare(tateImage, tateJumpscareSound, "MUST HAVE BEEN THE WIND", vineBoom)
    elif type == "won":
        scare = Jumpscare(deadPerson, deadJumpscareSound, "YOU DIE :(", vineBoom)
    elif type == "heart":
        scare = Jumpscare(cartiactImg, cartiac, "JK PlAYBOI CARTIAC ARREST", vineBoom)

    scare.jumpscare_run(screen)
