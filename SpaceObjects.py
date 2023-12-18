from functools import partial
import pygame
import sys
from pygame_draw_utils import *
from Grid import *
from vector import *
from Circle import *
import colors
from Transformation import *
from printer import *

# Initialize Pygame
pygame.init()

# Set up the window
width, height = WIDTH, HEIGHT
math_to_pixel = partial(math_to_pixel, window_width=width, window_height=height)
draw_line = partial(draw_line, xmin=-width/2, xmax=width/2, ymin=-height/2, ymax=height/2,
                    window_width=width, window_height=height)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Graphics with Pygame")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue=(0,0,255)
yellow=(255,255,0)


origin = Circle(5)
grid = Grid(width, height, cell_length=100, color=blue)
vec1 = Vector(300, 100)
vec2 = Vector(200, -350, start=vec1.end)
vec2_o = Vector(200, -350)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(black)


    origin.draw(screen, white)
    # draw axes
    grid.draw(screen, width=1)
    vec1.draw(screen, yellow, width=2)
    vec2.draw(screen, colors.cyan, width=2)
    vec2_o.draw(screen, colors.coral, width=2)
    (vec1 + vec2_o).draw(screen, colors.green, width=2)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()


