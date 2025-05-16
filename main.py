import pygame
from constants import WIDTH, HEIGHT
from survey_logic import question_teller
from exitFunction import exitFunction

# Initialize Pygame
pygame.init()

# Create display window
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Survey")

# Start survey logic
question_teller(pygame.display.get_surface())

# Exit when done
exitFunction()
