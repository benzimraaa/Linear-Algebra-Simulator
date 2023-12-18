from functools import partial
import pygame
import sys
from CoordinatesTransform import *
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
grid = Grid(2*width, 2*height, cell_length=100, color=blue)
grid_fix = Grid(width, height, cell_length=100, color=colors.light_gray)
vec_i = Vector(100, 0)
vec_j = Vector(0, 100)
vec1 = Vector(300, 100)
vec2 = Vector(200, -350, start=vec1.end)
vec2_o = Vector(200, -350)
circle = Circle(100,(-50, 100))



# trans_mat = Rotation(np.pi/2)
# trans_mat = Scaling(-1.2, 1.1)
trans_mat = Shear(-0.5, 0.5)*Scaling(0.6, 1.1)*Translation(-50, -100)
# print("-"*20,'\n'*3)
# print_colored_matrix(trans_mat.get_eigenvectors())
# print("-"*20,'\n'*3)

# eigen_vec = trans_mat.get_eigenvectors()[0].real

# print(eigen_vec)

# assert np.linalg.norm(eigen_vec) != 0

# eigen_vec = eigen_vec / np.linalg.norm(eigen_vec) * 150

# e_vec = Vector(eigen_vec[0], eigen_vec[1])

objects = [origin, grid, 
           vec_i, vec_j, vec1, vec2, vec2_o, circle,
            #  e_vec
             ]

# Main game loop
running = True
i = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                i = 0

    # Clear the screen
    screen.fill(black)

    # Draw a rectangle
    # draw_line(screen, red, (0, 0), (600, 600))

    origin.draw(screen, white)

    # rotate vectors
    for obj in objects:
        trans_mat(obj, i)


    
    # draw axes
    grid.draw(screen, width=1)
    grid_fix.draw(screen, width=1)

    


    # draw vector
    vec1.draw(screen, yellow, width=2)
    vec1.draw(screen, yellow, width=1)
    
    vec2.draw(screen, colors.cyan, width=2)
    vec2.draw(screen, colors.cyan, width=1)

    vec2_o.draw(screen, colors.coral, width=2)

    vec_i.draw(screen, colors.green, width=3)
    vec_i.draw_fixed(screen, colors.green, width=1)

    vec_j.draw(screen, colors.green, width=3)
    vec_j.draw_fixed(screen, colors.green, width=1)
    # circle.draw(screen, colors.green, width=1)

    # e_vec.draw(screen, colors.gold, width=5)
    # e_vec.draw_fixed(screen, colors.gold, width=1)

    # (vec1 + vec2_o).draw(screen, colors.green, width=2)

    # Update the display
    pygame.display.flip()
    i += 0.005
    i = min(i, 1)

# Quit Pygame
pygame.quit()
sys.exit()


