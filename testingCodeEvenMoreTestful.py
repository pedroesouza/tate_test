# importing required library
import pygame

# activate the pygame library
pygame.init()
X = 1650
Y = 1275

# create the display surface object
scrn = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('image')

# load initial image
current_image = pygame.image.load("Images/mainComputer.png").convert()

# function to update the screen with a new image
def update_image(image_path):
    global current_image
    current_image = pygame.image.load(image_path).convert()
    scrn.blit(current_image, (0, 0))
    pygame.display.flip()

# draw the initial image
scrn.blit(current_image, (0, 0))
pygame.display.flip()

status = True
while status:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
        elif event.type == pygame.KEYDOWN:  # Detect key press
            if event.key == pygame.K_w:  # W key
                update_image("Images/up1.png")
            elif event.key == pygame.K_a:  # A key
                update_image("Images/left1.png")
            elif event.key == pygame.K_s:  # S key
                update_image("Images/down1.png")
            elif event.key == pygame.K_d:  # D key
                update_image("Images/right1.png")
            elif event.key == pygame.K_q:  # Q key to quit
                status = False

# deactivates the pygame library
pygame.quit()