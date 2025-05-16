import pygame
from constants import WIDTH, HEIGHT, WHITE
from graphics import wrap_text

# Load images once
images = {
    "center": pygame.transform.scale(pygame.image.load("Images/mainComputer.png"), (WIDTH, HEIGHT)),
    "up": pygame.transform.scale(pygame.image.load("Images/up1.png"), (WIDTH, HEIGHT)),
    "down": pygame.transform.scale(pygame.image.load("Images/down1.png"), (WIDTH, HEIGHT)),
    "left": pygame.transform.scale(pygame.image.load("Images/left1.png"), (WIDTH, HEIGHT)),
    "right": pygame.transform.scale(pygame.image.load("Images/right1.png"), (WIDTH, HEIGHT)),
}

# Draw everything
def draw_screen(screen, font, held_keys, base_x, base_y, question, user_input, speed=20):
    # Start with center
    text_x, text_y = 0, 0
    current_bg = images["center"]

    # Adjust based on direction
    if held_keys["up"]:
        text_y += speed + 475
        current_bg = images["up"]
    if held_keys["down"]:
        text_y -= speed + 475
        current_bg = images["down"]
    if held_keys["left"]:
        text_x += speed + 720
        text_y -= speed + 170
        current_bg = images["left"]
    if held_keys["right"]:
        text_x -= speed + 470
        text_y -= speed + 160
        current_bg = images["right"]

    screen.blit(current_bg, (0, 0))

    # Render text
    question_lines = wrap_text(question, font)
    for i, surf in enumerate(question_lines):
        rect = surf.get_rect(center=(base_x + text_x, base_y - 80 + i * 40 + text_y))
        screen.blit(surf, rect)

    input_lines = wrap_text(user_input, font)
    for i, surf in enumerate(input_lines):
        rect = surf.get_rect(center=(base_x + text_x, base_y + 40 + i * 40 + text_y))
        screen.blit(surf, rect)

    # Quit tip
    quit_text = font.render("Enter 'quit' to quit", True, WHITE)
    screen.blit(quit_text, quit_text.get_rect(topright=(WIDTH - 20, 20)))

    pygame.display.flip()
