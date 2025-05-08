import pygame
import csv
import os
import time
import getpass
import sys

# ---------------------------- Pygame Setup ----------------------------
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Survey")
font = pygame.font.SysFont(None, 36)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Variable that tracks which image is active (used for positioning logic)
photo_num = None

# ---------------------------- Utilities ----------------------------
def draw_centered_text(question, user_input=''):
    screen.fill(WHITE)

    question_surface = font.render(question, True, BLACK)
    input_surface = font.render(user_input, True, BLACK)

    question_rect = question_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
    input_rect = input_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10))

    screen.blit(question_surface, question_rect)
    screen.blit(input_surface, input_rect)
    pygame.display.flip()

def show_message(message, wait_time=2):
    draw_centered_text(message)
    time.sleep(wait_time)

def get_user_input(question_text):
    user_input = ''
    while True:
        draw_centered_text(question_text, user_input)
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

# ---------------------------- Name Handling ----------------------------
try:
    name = os.getlogin()
except Exception:
    name = getpass.getuser()

formatted_name = name.replace('.', ' ').split()
if formatted_name:
    formatted_name[0] = formatted_name[0].capitalize()
formatted_name = ' '.join(formatted_name)

# ---------------------------- Main Question Logic ----------------------------
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
                        question = get_user_input(f"Question {id}: {row[1]} (type yes or no)")

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
                        question = get_user_input(f"Question {id}: {row[1]} (type yes or no)")
            elif id == '5':
                photo_num = 'image1'  # Example trigger
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
                        question = get_user_input(f"Question {id}: {row[1]} (type yes or no)")
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
                        question = get_user_input(f"Question {id}: {row[1]} (type yes or no)")
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
                photo_num = 'image2'
                while True:
                    if question == 'yes':
                        show_message("Nuh uh.")
                        break
                    elif question == 'no':
                        show_message("Good.")
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (type yes or no)")
            elif id == '11':
                while True:
                    if question in ['yes', 'no']:
                        show_message("Ok.")
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (type yes or no)")
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
                        question = get_user_input(f"Question {id}: {row[1]} (type yes or no)")
            elif id == '13':
                while True:
                    if question in [str(i) for i in range(1, 10)]:
                        show_message("Give me a ten.")
                    elif question == '10':
                        show_message("Good boy.")
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (Type a number 1-10)")

question_teller()
pygame.quit()
sys.exit()
