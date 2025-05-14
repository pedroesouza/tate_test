import pygame
import csv
import time
import sys

# ---------------------------- Pygame Setup ----------------------------
pygame.init()
WIDTH, HEIGHT = 1650, 1275
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Survey")
<<<<<<< HEAD
font = pygame.font.SysFont(None, 48)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def load_image(image_name, scale=1.0):
    try:
        image = pygame.image.load(f"Images/{image_name}.png").convert()
        if scale != 1.0:
            w = int(image.get_width() * scale)
            h = int(image.get_height() * scale)
            image = pygame.transform.smoothscale(image, (w, h))
        return image
    except Exception as e:
        print(f"Error loading image '{image_name}': {e}")
        return None

def camera(start_image="mainComputer", scale=0.5):
    pygame.init()
    X, Y = WIDTH, HEIGHT
    scrn = pygame.display.set_mode((X, Y))
    pygame.display.set_caption('image')

    def update_image(image_name):
        img = load_image(image_name, scale)
        if img:
            scrn.fill((0, 0, 0))
            x = (X - img.get_width()) // 2
            y = (Y - img.get_height()) // 2
            scrn.blit(img, (x, y))
            pygame.display.flip()
        return image_name

    current_image = update_image(start_image)

    status = True
    while status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
            elif event.type == pygame.KEYDOWN:  # Detect key press
                if event.key == pygame.K_UP:  # Up arrow key
                    update_image("Images/up1.png")
                elif event.key == pygame.K_LEFT:  # Left arrow key
                    update_image("Images/left1.png")
                elif event.key == pygame.K_DOWN:  # Down arrow key
                    update_image("Images/down1.png")
                elif event.key == pygame.K_RIGHT:  # Right arrow key
                    update_image("Images/right1.png")
                elif event.key == pygame.K_q:  # Q key to quit
                    status = False
            elif event.type == pygame.KEYUP:  # Detect key release
                # Reset to the mainComputer image when no key is pressed
                update_image("Images/mainComputer.png")

    pygame.quit()
    return current_image

def draw_screen(question, user_input='', image_name='mainComputer'):
    screen.fill(WHITE)
    image = load_image(image_name)
    if image:
        screen.blit(image, (0, 0))

    question_surface = font.render(question, True, BLACK)
    input_surface = font.render(user_input, True, BLACK)

    question_rect = question_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
    input_rect = input_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10))

    screen.blit(question_surface, question_rect)
    screen.blit(input_surface, input_rect)
    pygame.display.flip()

def show_message(message, photo_num, wait_time=2):
    draw_screen(message, '', photo_num)
    time.sleep(wait_time)

def get_user_input(question_text, photo_num):
    user_input = ''
    while True:
        draw_screen(question_text, user_input, photo_num)
=======
font = pygame.font.SysFont(None, 36)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
images = {
    "center": pygame.transform.scale(pygame.image.load("Images/mainComputer.png"), (WIDTH, HEIGHT)),
    "up": pygame.transform.scale(pygame.image.load("Images/up1.png"), (WIDTH, HEIGHT)),
    "down": pygame.transform.scale(pygame.image.load("Images/down1.png"), (WIDTH, HEIGHT)),
    "left": pygame.transform.scale(pygame.image.load("Images/left1.png"), (WIDTH, HEIGHT)),
    "right": pygame.transform.scale(pygame.image.load("Images/right1.png"), (WIDTH, HEIGHT)),
}

# Track which key is held
held_keys = {
    "up": False,
    "down": False,
    "left": False,
    "right": False
}

# Base text position
base_text_x, base_text_y = WIDTH // 2, HEIGHT // 2 - 100
text_offset_x, text_offset_y = 0, 0
speed = 20

# Start with the center image
current_bg = images["center"]

def wrap_text(text, font, max_chars_per_line=40):
    """Split text into lines based on character count and return rendered surfaces."""
    lines = []
    while len(text) > max_chars_per_line:
        split_index = text.rfind(' ', 0, max_chars_per_line)
        if split_index == -1:
            split_index = max_chars_per_line
        lines.append(text[:split_index])
        text = text[split_index:].lstrip()
    lines.append(text)
    return [font.render(line, True, BLACK) for line in lines]

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

    pygame.display.flip()

def show_message(message, wait_time=2):
    draw_screen(message, '')
    start = time.time()
    while time.time() - start < wait_time:
>>>>>>> 85639fddd532713b8d04722ba490fbe59ad66b26
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
<<<<<<< HEAD
=======

def get_user_input(question_text):
    user_input = ''
    clock = pygame.time.Clock()

    while True:
        draw_screen(question_text, user_input)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

>>>>>>> 85639fddd532713b8d04722ba490fbe59ad66b26
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return user_input.strip().lower()
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
<<<<<<< HEAD
                else:
                    user_input += event.unicode

# ---------------------------- Survey Logic ----------------------------
def question_teller(photo_num):
    score = 0
    total_score = 0

    show_message("Welcome to the survey.", photo_num)
    time.sleep(1)

=======
                elif event.key == pygame.K_SPACE:
                    held_keys["up"] = held_keys["down"] = held_keys["left"] = held_keys["right"] = False
                elif event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                    # --- Only one arrow key at a time ---
                    held_keys["up"] = held_keys["down"] = held_keys["left"] = held_keys["right"] = False
                    if event.key == pygame.K_UP:
                        held_keys["up"] = True
                    elif event.key == pygame.K_DOWN:
                        held_keys["down"] = True
                    elif event.key == pygame.K_LEFT:
                        held_keys["left"] = True
                    elif event.key == pygame.K_RIGHT:
                        held_keys["right"] = True
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

def question_teller():
    score = 0
    total_score = 0
    quiz_mode = False

    show_message("Welcome to the survey.")
    time.sleep(1)

>>>>>>> 85639fddd532713b8d04722ba490fbe59ad66b26
    with open('questions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            id = row[0]
            question_text = f"Question {id}: {row[1]}"
<<<<<<< HEAD
            question = get_user_input(question_text, photo_num)

            if id == '9':
                show_message("Let's play a little game, shall we?", photo_num)
            if id == '13' and question == '10':
                break
            if id == '1' and question == 'yes':
                show_message("You can't play this game.", photo_num)
                break
=======
            question = get_user_input(question_text)

            if id == '9':
                quiz_mode = True
                show_message("Let's play a little game, shall we?")
                continue

            if id == '13' and question == '10':
                break
>>>>>>> 85639fddd532713b8d04722ba490fbe59ad66b26

            if id == '1':
                while True:
                    if question == 'yes':
<<<<<<< HEAD
                        show_message("You can't play this game then. Bye.", photo_num)
                        return
                    elif question == 'no':
                        show_message("Ok good.", photo_num)
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (yes/no)", photo_num)

            elif id == '2':
                show_message("Ok.", photo_num)
            elif id == '3':
                show_message("That's cool.", photo_num)
            elif id == '4':
                while True:
                    if question == 'yes':
                        show_message("Ok, just double checking.", photo_num)
                        break
                    elif question == 'no':
                        show_message("Are you sure?...", photo_num)
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (yes/no)", photo_num)
            elif id == '5':
                photo_num = 'up1'
                show_message("Actually based off my IP grabber, you are at 31.255.56.229", photo_num)
            elif id == '6':
                while True:
                    if question == 'yes':
                        photo_num = 'right1'
                        show_message("Ok cool, our team is ready to move in...", photo_num)
                        break
                    elif question == 'no':
                        photo_num = 'left1'
                        show_message("Not anymore...", photo_num)
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (yes/no)", photo_num)
=======
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
>>>>>>> 85639fddd532713b8d04722ba490fbe59ad66b26
            elif id == '7':
                while True:
                    try:
                        int(question)
<<<<<<< HEAD
                        show_message("Thanks.", photo_num)
                        break
                    except ValueError:
                        question = get_user_input(f"Question {id}: {row[1]} (type a number)", photo_num)
            elif id == '8':
                while True:
                    if question == 'yes':
                        show_message("Good boy.", photo_num)
                        break
                    elif question == 'no':
                        show_message("Bad boy...", photo_num)
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (yes/no)", photo_num)
            elif id == '9a':
                if question == '19':
                    show_message("Correct!", photo_num)
                    score += 1
                else:
                    show_message("Incorrect...", photo_num)
                total_score += 1
            elif id == '9b':
                if question == '2':
                    show_message("Correct!", photo_num)
                    score += 1
                else:
                    show_message("Incorrect...", photo_num)
                total_score += 1
            elif id == '9c':
                if question == '110':
                    show_message("Correct!", photo_num)
                    score += 1
                else:
                    show_message("Incorrect...", photo_num)
                total_score += 1
            elif id == '9d':
                if question == '63':
                    show_message("Correct!", photo_num)
                    score += 1
                else:
                    show_message("Incorrect...", photo_num)
                total_score += 1
            elif id == '9e':
                if question == '5':
                    show_message("Correct!", photo_num)
                    score += 1
                else:
                    show_message("Incorrect...", photo_num)
                total_score += 1
            elif total_score == 5:
                if score >= 3:
                    show_message("You failed...", photo_num)
                else:
                    show_message("You passed.", photo_num)
            elif id == '10':
                photo_num = 'down1'
                while True:
                    if question == 'yes':
                        show_message("Nuh uh.", photo_num)
                        break
                    elif question == 'no':
                        show_message("Good.", photo_num)
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (yes/no)", photo_num)
            elif id == '11':
                while True:
                    if question in ['yes', 'no']:
                        show_message("Ok.", photo_num)
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (yes/no)", photo_num)
            elif id == '12':
                while True:
                    if question == 'yes':
                        show_message("How did you know?", photo_num)
                        time.sleep(2)
                        break
                    elif question == 'no':
                        show_message("Think again...", photo_num)
                        time.sleep(2)
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (yes/no)", photo_num)
            elif id == '13':
                while True:
                    if question in [str(i) for i in range(1, 10)]:
                        show_message("Give me a ten.", photo_num)
                    elif question == '10':
                        show_message("Good boy.", photo_num)
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (1–10)", photo_num)

    return photo_num

# ---------------------------- Run ----------------------------
photo_num = camera()  # returns the last viewed image name
question_teller(photo_num)
=======
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
                        break
                    elif question == 'no':
                        show_message("Think again...")
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
                        break
                    else:
                        question = get_user_input(f"Question {id}: {row[1]} (1–10)")

    if quiz_mode and total_score == 5:
        if score >= 3:
            show_message("You failed...")
        else:
            show_message("You passed.")

# ---------------------------- Run ----------------------------
question_teller()
>>>>>>> 85639fddd532713b8d04722ba490fbe59ad66b26
pygame.quit()
