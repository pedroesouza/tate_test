import pandas as pd
import pygame
import math
import os

# Initialize pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("3D-Like Question Game")

# Font setup
font = pygame.font.Font(None, 36)

# Camera angles
camera_angle_x = 0
camera_angle_y = 0

# Rotation speed
rotation_speed = 30

# Function to rotate and project a 3D point onto 2D screen
def rotate_3d(x, y, z, angle_x, angle_y):
    rad_x = math.radians(angle_x)
    rad_y = math.radians(angle_y)

    # Rotate around X-axis
    y_rot = y * math.cos(rad_x) - z * math.sin(rad_x)
    z_rot = y * math.sin(rad_x) + z * math.cos(rad_x)

    # Rotate around Y-axis
    x_rot = x * math.cos(rad_y) + z_rot * math.sin(rad_y)
    z_rot = -x * math.sin(rad_y) + z_rot * math.cos(rad_y)

    fov = 500
    distance = 5
    depth = z_rot + distance

    # 🧼 Don't draw if behind camera
    if depth <= 0.1:
        return None

    try:
        x_projected = int((x_rot * fov) / depth + screen_width // 2)
        y_projected = int((y_rot * fov) / depth + screen_height // 2)

        # Clamp for safety
        x_projected = max(-10000, min(10000, x_projected))
        y_projected = max(-10000, min(10000, y_projected))

    except ZeroDivisionError:
        return None

    return x_projected, y_projected

def jumpscare():
    print("💀 BOO! Jumpscare!")

def exit_game():
    print("Exiting the game...")
    pygame.quit()
    exit()

def question():
    global camera_angle_x, camera_angle_y

    csv_path = 'questions.csv'
    if not os.path.exists(csv_path):
        print(f"CSV file not found at: {csv_path}")
        pygame.time.wait(3000)
        return

    try:
        question_csv = pd.read_csv(csv_path)
    except Exception as e:
        print(f"Error loading CSV: {e}")
        pygame.time.wait(3000)
        return

    for index, row in question_csv.iterrows():
        question_text = str(row['question'])
        correct_answer = str(row['answer']).strip().lower()
        user_input = ""
        answered = False

        question_x = 0
        question_y = 0
        question_z = 10

        while not answered:
            screen.fill((0, 0, 0))

            projected = rotate_3d(question_x, question_y, question_z, camera_angle_x, camera_angle_y)

            # 🛑 Skip rendering if behind the camera
            if projected is not None:
                projected_x, projected_y = projected

                question_surface = font.render(question_text, True, (255, 255, 255))
                question_rect = question_surface.get_rect(center=(projected_x, projected_y))
                screen.blit(question_surface, question_rect)

            # Always draw input so user can type
            input_surface = font.render(user_input, True, (255, 255, 255))
            input_rect = input_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
            screen.blit(input_surface, input_rect)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        camera_angle_y += rotation_speed
                    elif event.key == pygame.K_RIGHT:
                        camera_angle_y -= rotation_speed
                    elif event.key == pygame.K_UP:
                        camera_angle_x -= rotation_speed
                    elif event.key == pygame.K_DOWN:
                        camera_angle_x += rotation_speed

                    # Clamp angles
                    camera_angle_y = camera_angle_y % 360
                    camera_angle_x = max(-90, min(90, camera_angle_x))

                    if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        if user_input.strip().lower() == correct_answer:
                            response_surface = font.render("Correct!", True, (0, 255, 0))
                            response_rect = response_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 100))
                            screen.blit(response_surface, response_rect)
                            pygame.display.update()
                            pygame.time.wait(1000)

                            if str(row.get('exit', False)).lower() == 'true':
                                exit_game()
                            elif str(row.get('jumpscare', False)).lower() == 'true':
                                jumpscare()

                            answered = True
                        else:
                            response_surface = font.render("Wrong!", True, (255, 0, 0))
                            response_rect = response_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 100))
                            screen.blit(response_surface, response_rect)
                            pygame.display.update()
                            pygame.time.wait(1000)
                            user_input = ""

                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    elif event.unicode.isprintable():
                        user_input += event.unicode

# Run it
question()
