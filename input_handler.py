#CONNOR and LOCKLIN

#Import needed library
import pygame
import sys

#Import functions from other files
from screen_draw import draw_screen
from exitFunction import exitFunction

# Handle player typing
def get_user_input(screen, font, held_keys, base_x, base_y, question_text):
    user_input = ''
    clock = pygame.time.Clock()

    while True:
        draw_screen(screen, font, held_keys, base_x, base_y, question_text, user_input)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    clean = user_input.strip().lower()
                    if clean == 'quit':
                        pygame.quit()
                        exitFunction()
                    return clean

                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]

                elif event.key == pygame.K_SPACE and len(user_input) < 100:
                    user_input += ' '

                elif event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                    held_keys["up"] = event.key == pygame.K_UP
                    held_keys["down"] = event.key == pygame.K_DOWN
                    held_keys["left"] = event.key == pygame.K_LEFT
                    held_keys["right"] = event.key == pygame.K_RIGHT

                elif len(user_input) < 100:
                    user_input += event.unicode

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP: held_keys["up"] = False
                if event.key == pygame.K_DOWN: held_keys["down"] = False
                if event.key == pygame.K_LEFT: held_keys["left"] = False
                if event.key == pygame.K_RIGHT: held_keys["right"] = False

        clock.tick(60)
