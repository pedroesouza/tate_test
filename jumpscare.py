import pygame
import time
import sys

class Jumpscare:
    def __init__(self, image, sound, text, boom):
        self.image = image
        self.sound = sound
        self.text = text
        self.boom = boom

    def jumpscare_run(self, screen):
        pygame.mixer.init()

        image_rect = self.image.get_rect(center=screen.get_rect().center)
        screen.blit(self.image, image_rect)
        pygame.display.update()

        self.sound.play()
        time.sleep(10)

        screen.fill((0, 0, 0))
        pygame.display.update()

        self.boom.play()

        font = pygame.font.Font(None, 64)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=screen.get_rect().center)
        screen.blit(text_surface, text_rect)
        pygame.display.update()

        time.sleep(3)

def jumpscare_manager(type, screen):
    tateImage = pygame.image.load("tate_image.png").convert()
    cartiactImg = pygame.image.load("cartiac.jpg").convert()
    cartiac = pygame.mixer.Sound("carti-scream.wav")
    deadPerson = pygame.image.load("dead.jpg").convert()
    deadJumpscareSound = pygame.mixer.Sound("dead_sound.wav")
    tateJumpscareSound = pygame.mixer.Sound("jumpscare_sound.wav")
    vineBoom = pygame.mixer.Sound("vine_boom.wav")

    if type == "normal":
        scare = Jumpscare(tateImage, tateJumpscareSound, "MUST HAVE BEEN THE WIND", vineBoom)
    elif type == "won":
        scare = Jumpscare(deadPerson, deadJumpscareSound, "YOU DIE :(", vineBoom)
    elif type == "heart":
        scare = Jumpscare(cartiactImg, cartiac, "JK PlAYBOI CARTIAC ARREST", vineBoom)

    scare.jumpscare_run(screen)

# === Main Program ===
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Jumpscare Test")

    screen.fill((0, 0, 0))
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    jumpscare_manager("normal", screen)
                elif event.key == pygame.K_2:
                    jumpscare_manager("won", screen)
                elif event.key == pygame.K_3:
                    jumpscare_manager("heart", screen)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
