import pygame
import csv
import time
import sys
from jumpscare import jumpscare_manager as jumpscare

# Pygame initialization setup
pygame.init()
WIDTH, HEIGHT = 1650, 1275
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Survey")
font = pygame.font.SysFont(None, 36)

# Define color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load background images
images = {
    "center": pygame.transform.scale(pygame.image.load("Images/mainComputer.png"), (WIDTH, HEIGHT)),
    "up": pygame.transform.scale(pygame.image.load("Images/up1.png"), (WIDTH, HEIGHT)),
    "down": pygame.transform.scale(pygame.image.load("Images/down1.png"), (WIDTH, HEIGHT)),
    "left": pygame.transform.scale(pygame.image.load("Images/left1.png"), (WIDTH, HEIGHT)),
    "right": pygame.transform.scale(pygame.image.load("Images/right1.png"), (WIDTH, HEIGHT)),
}

# Arrow key tracking
held_keys = {
    "up": False,
    "down": False,
    "left": False,
    "right": False
}

# Text positioning setup
base_text_x, base_text_y = WIDTH // 2, HEIGHT // 2 - 100
text_offset_x, text_offset_y = 0, 0
speed = 20

# Default background image
current_bg = images["center"]

# Text wrapping function
def wrap_text(text, font, max_chars_per_line=35):
    lines = []
    while len(text) > max_chars_per_line:
        # Try to break at the last space before the limit
        split_index = text.rfind(' ', 0, max_chars_per_line)
        if split_index == -1:
            # If no space is found, force split at the limit
            split_index = max_chars_per_line
        lines.append(text[:split_index])
        text = text[split_index:].lstrip()  # Remove leading spaces for the next line
    lines.append(text)  # Add the final line
    return [font.render(line, True, BLACK) for line in lines]


# Draw screen content
def draw_screen(question, user_input=''):
    global text_offset_x, text_offset_y, current_bg

    text_offset_x = 0
    text_offset_y = 0
    current_bg = images["center"]

    if held_keys["up"]:
        text_offset_y += speed + 475
        current_bg = images["up"]
    if held_keys["down"]:
        text_offset_y -= speed + 475
        current_bg = images["down"]
    if held_keys["left"]:
        text_offset_x += speed + 720
        text_offset_y -= speed + 170
        current_bg = images["left"]
    if held_keys["right"]:
        text_offset_x -= speed + 470
        text_offset_y -= speed + 160
        current_bg = images["right"]

    screen.blit(current_bg, (0, 0))

    question_lines = wrap_text(question, font)
    for i, line_surf in enumerate(question_lines):
        rect = line_surf.get_rect(center=(base_text_x + text_offset_x, base_text_y - 80 + i * 40 + text_offset_y))
        screen.blit(line_surf, rect)

    input_lines = wrap_text(user_input, font)
    for i, line_surf in enumerate(input_lines):
        rect = line_surf.get_rect(center=(base_text_x + text_offset_x, base_text_y + 40 + i * 40 + text_offset_y))
        screen.blit(line_surf, rect)
    
    # Display backslash quit instruction in top-right corner
    quit_text = font.render("Press backslash to quit", True, WHITE)
    quit_rect = quit_text.get_rect(topright=(WIDTH - 20, 20))
    screen.blit(quit_text, quit_rect)

    pygame.display.flip()

# Show temporary message
def show_message(message, wait_time=2):
    draw_screen(message, '')
    start = time.time()
    while time.time() - start < wait_time:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Handle user input
def get_user_input(question_text):
    user_input = ''
    clock = pygame.time.Clock()

    while True:
        draw_screen(question_text, user_input)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return user_input.strip().lower()
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key == pygame.K_SPACE:
                    held_keys["up"] = held_keys["down"] = held_keys["left"] = held_keys["right"] = False
                elif event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                    # One arrow key
                    held_keys["up"] = held_keys["down"] = held_keys["left"] = held_keys["right"] = False
                    if event.key == pygame.K_UP:
                        held_keys["up"] = True
                    elif event.key == pygame.K_DOWN:
                        held_keys["down"] = True
                    elif event.key == pygame.K_LEFT:
                        held_keys["left"] = True
                    elif event.key == pygame.K_RIGHT:
                        held_keys["right"] = True
                    elif event.key == pygame.K_F1:
                        pygame.quit()
                        sys.exit()
                else:
                    user_input += event.unicode

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    held_keys["up"] = False
                elif event.key == pygame.K_DOWN:
                    held_keys["down"] = False
                elif event.key == pygame.K_LEFT:
                    held_keys["left"] = False
                elif event.key == pygame.K_RIGHT:
                    held_keys["right"] = False

        clock.tick(60)

# Survey logic function
def question_teller():
    score = 0
    total_score = 0
    quiz_mode = False

    show_message("Welcome to the survey.")
    time.sleep(1)

    with open('questions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            id = row[0]
            question_text = f"Question {id}: {row[1]}"
            question = get_user_input(question_text)

            # Quiz mode trigger
            if id == '9':
                quiz_mode = True
                show_message("Let's play a little game, shall we?")
                continue

            # Exit early condition
            if id == '13' and question == '10':
                break

            # Specific question logic
            if id == '1':
                while True:
                    if question == 'yes':
                        show_message("You can't play this game then. Bye.")
                        jumpscare('heart', screen)
                        return
                    elif question == 'no':
                        show_message("Ok good.")
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (yes/no)")

            elif id == '2':
                show_message("Ok.")
            elif id == '3':
                show_message("That's cool.")
            elif id == '4':
                while True:
                    if question == 'yes':
                        show_message("Ok, just double checking.")
                        break
                    elif question == 'no':
                        show_message("Are you sure?...")
                        jumpscare('normal', screen)
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (yes/no)")
            elif id == '5':
                show_message("Actually based off my IP grabber, you are at 31.255.56.229")
            elif id == '6':
                while True:
                    if question == 'yes':
                        show_message("Ok cool, our team is ready to move in...")
                        break
                    elif question == 'no':
                        show_message("Not anymore...")
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (yes/no)")
            elif id == '7':
                while True:
                    try:
                        int(question)
                        show_message("Thanks.")
                        break
                    except ValueError:
                        question = get_user_input(f"Question {id}: {row[1]} (type a number)")
            elif id == '8':
                while True:
                    if question == 'yes':
                        show_message("Good boy.")
                        break
                    elif question == 'no':
                        show_message("Bad boy...")
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (yes/no)")
            elif id in ['9a', '9b', '9c', '9d', '9e']:
                correct_answers = {'9a': '19', '9b': '2', '9c': '110', '9d': '63', '9e': '5'}
                total_score += 1
                if question == correct_answers[id]:
                    show_message("Correct!")
                    score += 1
                else:
                    show_message("Incorrect...")
            elif id == '10':
                while True:
                    if question == 'yes':
                        show_message("Nuh uh.")
                        break
                    elif question == 'no':
                        show_message("Good.")
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (yes/no)")
            elif id == '11':
                while True:
                    if question in ['yes', 'no']:
                        show_message("Ok.")
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (yes/no)")
            elif id == '12':
                while True:
                    if question == 'yes':
                        show_message("How did you know?")
                        jumpscare('normal', screen)
                        break
                    elif question == 'no':
                        show_message("Think again...")
                        jumpscare('normal', screen)
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (yes/no)")
            elif id == '13':
                while True:
                    if question in [str(i) for i in range(1, 10)]:
                        show_message("Give me a ten.")
                        question = get_user_input(f"Question {id}: {row[1]} (1–10)")
                    elif question == '10':
                        show_message("Good boy.")
                        jumpscare('won', screen)
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (1–10)")

    # Show quiz results
    if quiz_mode and total_score == 5:
        if score >= 3:
            show_message("You failed...")
            jumpscare('normal', screen)
        else:
            show_message("You passed.")

# Run main function
question_teller()
pygame.quit()
