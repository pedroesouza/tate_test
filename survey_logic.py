# CONNOR

# Import needed libraries
import csv
import time
import pygame

# Get other program's variables and functions
from constants import WIDTH, HEIGHT
from input_handler import get_user_input
from screen_draw import draw_screen
from jumpscare import jumpscare_manager as jumpscare  # Make sure this exists and is correctly implemented

# Display a temporary message on screen for a given time
def show_message(screen, font, held_keys, base_x, base_y, msg, wait=2):
    draw_screen(screen, font, held_keys, base_x, base_y, msg, '')
    start = time.time()
    while time.time() - start < wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

# Get a yes/no response from the user, keep asking until valid
def get_yes_no_input(screen, font, held_keys, base_x, base_y, question):
    first_attempt = True
    while True:
        prompt = question if first_attempt else f"{question} (type yes or no)"
        answer = get_user_input(screen, font, held_keys, base_x, base_y, prompt)
        if answer is None:
            return None
        if answer.lower() in ['yes', 'no']:
            return answer.lower()
        else:
            first_attempt = False

# Get an integer input from the user, retry if not valid
def get_integer_input(screen, font, held_keys, base_x, base_y, question):
    first_attempt = True
    while True:
        prompt = question if first_attempt else f"{question} (type a number)"
        answer = get_user_input(screen, font, held_keys, base_x, base_y, prompt)
        if answer is None:
            return None
        if answer.isdigit():
            return answer
        else:
            first_attempt = False

# Main question flow
def question_teller(screen):
    # Setup font and input state
    font = pygame.font.SysFont(None, 36)
    held_keys = {"up": False, "down": False, "left": False, "right": False}
    base_x, base_y = WIDTH // 2, HEIGHT // 2 - 100

    # Greet the user
    show_message(screen, font, held_keys, base_x, base_y, "Welcome to the survey.")

    # Define correct answers for quiz-style questions
    quiz_answers = {
        '9a': '19',
        '9b': '2',
        '9c': '100',
        '9d': '63',
        '9e': '5',
    }

    quiz_mode = False
    score = 0
    total_quiz_questions = len(quiz_answers)

    # Load all questions from CSV file
    with open('questions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        questions = []
        for row in reader:
            if len(row) < 2:
                continue
            qid = row[0].strip()
            question_text = row[1].strip()
            questions.append((qid, question_text))

        # Loop through each question and handle logic
        for qid, question_text in questions:
            display_question = f"Question {qid}: {question_text}"

            # If it's a quiz question, switch mode and handle grading
            if qid in quiz_answers:
                if not quiz_mode:
                    quiz_mode = True
                    show_message(screen, font, held_keys, base_x, base_y, "Let's play a little game, shall we?")
                answer = get_integer_input(screen, font, held_keys, base_x, base_y, display_question)
                if answer is None:
                    return
                if answer == quiz_answers[qid]:
                    score += 1
                    show_message(screen, font, held_keys, base_x, base_y, "Correct.")
                else:
                    show_message(screen, font, held_keys, base_x, base_y, "Wrong.")
                continue

            # Handle different input types based on question ID
            if qid in ['1', '4', '6', '8']:
                answer = get_yes_no_input(screen, font, held_keys, base_x, base_y, display_question)
                if answer is None:
                    return
            elif qid in ['7', '13']:
                answer = get_integer_input(screen, font, held_keys, base_x, base_y, display_question)
                if answer is None:
                    return
            else:
                answer = get_user_input(screen, font, held_keys, base_x, base_y, display_question)
                if answer is None:
                    return

            # Custom response logic for certain questions
            if qid == '2':
                show_message(screen, font, held_keys, base_x, base_y, "Ok.")
            elif qid == '3':
                show_message(screen, font, held_keys, base_x, base_y, "Cool.")
            elif qid == '5':
                show_message(screen, font, held_keys, base_x, base_y, "Actually you live at 187.61.9.140")
            elif qid == '6':
                if answer == 'yes':
                    show_message(screen, font, held_keys, base_x, base_y, "I knew that")
                elif answer == 'no':
                    show_message(screen, font, held_keys, base_x, base_y, "Nuh uh...")
            elif qid == '7':
                show_message(screen, font, held_keys, base_x, base_y, "Thanks.")
            elif qid == '8':
                if answer == 'yes':
                    show_message(screen, font, held_keys, base_x, base_y, "Good boy.")
                # No response if 'no'
            elif qid == '10':
                show_message(screen, font, held_keys, base_x, base_y, "Alright.")
            elif qid == '11':
                show_message(screen, font, held_keys, base_x, base_y, "Ok.")

            # Conditional jumpscare triggers based on specific answers
            if qid == '1' and answer == 'yes':
                jumpscare('heart', screen)

            elif qid == '4' and answer in ['yes', 'no']:
                jumpscare('normal', screen)

            elif qid == '8' and answer == 'no':
                show_message(screen, font, held_keys, base_x, base_y, "Bad boy.")
                jumpscare('normal', screen)

            elif qid == '8' and answer == 'yes':
                jumpscare('normal', screen)

            elif qid == '13':
                if answer == '10':
                    jumpscare('won', screen)
                    pygame.quit()
                    return

    # Final quiz result and optional scare if user failed
    if quiz_mode:
        if score >= 3:
            show_message(screen, font, held_keys, base_x, base_y, f"You passed with score {score} / {total_quiz_questions}.")
        else:
            show_message(screen, font, held_keys, base_x, base_y, f"You failed with score {score} / {total_quiz_questions}.")
            jumpscare('normal', screen)
