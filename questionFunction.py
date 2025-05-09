import pygame
import csv
import time
import sys

# ---------------------------- Pygame Setup ----------------------------
pygame.init()
WIDTH, HEIGHT = 1650, 1275
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Survey")
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    current_image = update_image("up1")
                elif event.key == pygame.K_a:
                    current_image = update_image("left1")
                elif event.key == pygame.K_s:
                    current_image = update_image("down1")
                elif event.key == pygame.K_d:
                    current_image = update_image("right1")
                elif event.key == pygame.K_q:
                    status = False

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
def question_teller(photo_num):
    score = 0
    total_score = 0

    show_message("Welcome to the survey.", photo_num)
    time.sleep(1)

    with open('questions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            id = row[0]
            question_text = f"Question {id}: {row[1]}"
            question = get_user_input(question_text, photo_num)

            if id == '9':
                show_message("Let's play a little game, shall we?", photo_num)
            if id == '13' and question == '10':
                break
            if id == '1' and question == 'yes':
                show_message("You can't play this game.", photo_num)
                break

            if id == '1':
                while True:
                    if question == 'yes':
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
            elif id == '7':
                while True:
                    try:
                        int(question)
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
pygame.quit()
