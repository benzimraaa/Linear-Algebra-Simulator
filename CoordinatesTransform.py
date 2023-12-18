import pygame
from config import *



def math_to_pixel(vec, scale=1, window_width=WIDTH, window_height=HEIGHT):
    """Converts a coordinate from math coordinates to pixel coordinates."""
    if isinstance(vec, tuple):
        vec = list(vec)
        if len(vec) == 4:
            vec[0] = scale * vec[0] + window_width / 2
            vec[1] = window_height / 2 - scale * vec[1]
            return tuple(vec)
            
    vec = vec.copy()
    vec[0] = scale * vec[0] + window_width / 2
    vec[1] = window_height / 2 - scale * vec[1]
    return vec


def draw_line(screen, color, p1, p2, 
              xmin = -WIDTH/2, xmax = WIDTH/2,
              ymin = -HEIGHT/2, ymax = HEIGHT/2,
              width=1,scale=1,
              window_width=WIDTH, window_height=HEIGHT):
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    
    # Initialize t values for the boundaries
    tmin, tmax = 0, 1

    # Check against x boundaries
    if dx != 0:
        tx1 = (xmin - p1[0]) / dx
        tx2 = (xmax - p1[0]) / dx
        tmin = max(tmin, min(tx1, tx2))
        tmax = min(tmax, max(tx1, tx2))

    # Check against y boundaries
    if dy != 0:
        ty1 = (ymin - p1[1]) / dy
        ty2 = (ymax - p1[1]) / dy
        tmin = max(tmin, min(ty1, ty2))
        tmax = min(tmax, max(ty1, ty2))

    # Check if the line is outside the window
    if tmax < tmin:
        return None, None

    # Calculate the clipped points
    x1 = int(p1[0] + tmin * dx)
    y1 = int(p1[1] + tmin * dy)
    x2 = int(p1[0] + tmax * dx)
    y2 = int(p1[1] + tmax * dy)

    p1 = math_to_pixel([x1, y1], window_width=window_width, window_height=window_height, scale=scale)
    p2 = math_to_pixel([x2, y2], window_width=window_width, window_height=window_height, scale=scale)
    if p1 is not None and p2 is not None:
        pygame.draw.line(screen, color, p1, p2, width)

def check_boundaries(p):
    """Check if a point is inside the boundaries of pygame window."""
    x, y = p
    return 0 <= x <= WIDTH and 0 <= y <= HEIGHT


def draw_text(screen, text, start_pos, end_pos):
    # Calculate the position for the text
    start_pos = math_to_pixel(start_pos)
    end_pos = math_to_pixel(end_pos)
    font = pygame.font.SysFont('Times New Roman', 25)
    text_width, text_height = font.size(text)
    text_x = start_pos[0] + (end_pos[0] - start_pos[0]) // 0.9 - text_width // 2
    text_y = start_pos[1] + (end_pos[1] - start_pos[1]) // 0.9 - text_height // 2

    # Draw the text on the line
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (text_x, text_y))