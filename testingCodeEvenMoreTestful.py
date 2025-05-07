# importing required library
import pygame
 
# activate the pygame library .
pygame.init()
X = 1650
Y = 1275


# create the display surface object
# of specific dimension..e(X, Y).
scrn = pygame.display.set_mode((X, Y))
 
# set the pygame window name
pygame.display.set_caption('image')
 
# create a surface object, image is drawn on it.
imp = pygame.image.load("Images\mainComputer.png").convert()
 
# Using blit to copy content from one surface to other
scrn.blit(imp, (0, 0))
 
# paint screen one time
pygame.display.flip()
status = True
while (status):
 
  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    for i in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False
 
# deactivates the pygame library
pygame.quit()

def cntrls():
    look = input("(W)up, (A)left, (S)down, (D)right, (Q)uit: ")
    if look == "W":
         # Replace the image dynamically (example)
      new_image = pygame.image.load("Images/up1.png").convert()
      scrn.blit(new_image, (0, 0))
      pygame.display.flip()
    elif look == "A":
         # Replace the image dynamically (example)
      new_image = pygame.image.load("Images/left1.png").convert()
      scrn.blit(new_image, (0, 0))
      pygame.display.flip()
    elif look == "S":
           # Replace the image dynamically (example)
      new_image = pygame.image.load("Images/down1.png").convert()
      scrn.blit(new_image, (0, 0))
      pygame.display.flip()
    elif look == "D":
   # Replace the image dynamically (example)
      new_image = pygame.image.load("Images/right1.png").convert()
      scrn.blit(new_image, (0, 0))
      pygame.display.flip()
    elif look == "Q":
      pygame.quit()
    else:
        print("Invalid input, please try again.")

cntrls()