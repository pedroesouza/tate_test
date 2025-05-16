import pygame
from constants import WIDTH, HEIGHT, BLACK, MAX_CHARS_PER_LINE

# Text wrap function
def wrap_text(text, font, max_chars=MAX_CHARS_PER_LINE):
    lines = []
    while len(text) > max_chars:
        split_idx = text.rfind(' ', 0, max_chars)
        if split_idx == -1:
            split_idx = max_chars
        lines.append(text[:split_idx])
        text = text[split_idx:].lstrip()
    lines.append(text)
    return [font.render(line, True, BLACK) for line in lines]
