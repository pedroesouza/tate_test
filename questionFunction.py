import pygame
import csv
import os
import time
import getpass
import sys

# ---------------------------- Pygame Setup ----------------------------
pygame.init()
WIDTH, HEIGHT = 1650, 1275
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Survey")
font = pygame.font.SysFont(None, 48)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

photo_num = "mainComputer"  # initial image

# ---------------------------- Image Loading ----------------------------
def load_image(image_name):
    path = f"Images/{image_name}.png"
    try:
        image = pygame.image.load(path).convert()
        return image
    except:
        return None

# ---------------------------- Rendering ----------------------------
def draw_screen(question, user_input='', image_name='mainComputer'):
    screen.fill(WHITE)

    # Draw background image
    image = load_image(image_name)
    if image:
        screen.blit(image, (0, 0))

    # Render text
    question_surface = font.render(question, True, BLACK)
    input_surface = font.render(user_input, True, BLACK)

    question_rect = question_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
    input_rect = input_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10))

    screen.blit(question_surface, question_rect)
    screen.blit(input_surface, input_rect)
    pygame.display.flip()

def show_message(message, wait_time=2):
    draw_screen(message, '', photo_num)
    time.sleep(wait_time)

def get_user_input(question_text):
    user_input = ''
    while True:
        draw_screen(question_text, user_input, photo_num)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return user_input.strip().lower()
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode
                    
# ---------------------------- Survey Logic ----------------------------
def question_teller():
    global photo_num
    score = 0
    total_score = 0

    show_message("Welcome to the survey.")
    time.sleep(1)

    with open('questions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            id = row[0]
            question_text = f"Question {id}: {row[1]}"
            question = get_user_input(question_text)

            if id == '9':
                show_message("Let's play a little game, shall we?")
            if id == '13' and question == '10':
                break
            if id == '1' and question == 'yes':
                show_message("You can't play this game.")
                break

            if id == '1':
                while True:
                    if question == 'yes':
                        show_message("You can't play this game then. Bye.")
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
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (yes/no)")
            elif id == '5':
                photo_num = 'up1'  # Update background image
                show_message("Actually based off my IP grabber, you are at 31.255.56.229")
            elif id == '6':
                while True:
                    if question == 'yes':
                        photo_num = 'right1'
                        show_message("Ok cool, our team is ready to move in...")
                        break
                    elif question == 'no':
                        photo_num = 'left1'
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
            elif id == '9a':
                if question == '19':
                    show_message("Correct!")
                    score += 1
                else:
                    show_message("Incorrect...")
                total_score += 1
            elif id == '9b':
                if question == '2':
                    show_message("Correct!")
                    score += 1
                else:
                    show_message("Incorrect...")
                total_score += 1
            elif id == '9c':
                if question == '110':
                    show_message("Correct!")
                    score += 1
                else:
                    show_message("Incorrect...")
                total_score += 1
            elif id == '9d':
                if question == '63':
                    show_message("Correct!")
                    score += 1
                else:
                    show_message("Incorrect...")
                total_score += 1
            elif id == '9e':
                if question == '5':
                    show_message("Correct!")
                    score += 1
                else:
                    show_message("Incorrect...")
                total_score += 1
            elif total_score == 5:
                if score >= 3:
                    show_message("You failed...")
                else:
                    show_message("You passed.")
            elif id == '10':
                photo_num = 'down1'
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
                        time.sleep(2)
                        break
                    elif question == 'no':
                        show_message("Think again...")
                        time.sleep(2)
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (yes/no)")
            elif id == '13':
                while True:
                    if question in [str(i) for i in range(1, 10)]:
                        show_message("Give me a ten.")
                    elif question == '10':
                        show_message("Good boy.")
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (1–10)")

# ---------------------------- Run ----------------------------
question_teller()
pygame.quit()
