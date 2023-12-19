from functools import partial
import random
import pygame
import sys
from Star import Star
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
grid = Grid(8*width, 8*height, cell_length=100, color=blue)
grid_fix = Grid(width, height, cell_length=100, color=colors.light_gray)
vec_i = Vector(100, 0)
vec_j = Vector(0, 100)
vec1 = Vector(300, 100)
vec2 = Vector(200, -350, start=vec1.end)
vec2_o = Vector(200, -350)
circle = Circle(100,(-50, 100))
star = Star(5, 400, 100, (-500, 80))
points = []
# random circles (points)
for i in range(20):
    circle = Circle(random.randint(3,20), (random.randint(-width/2, width/2), random.randint(-height/2, height/2)))
    points.append(circle)


# trans_mat = Rotation(np.pi/3)
# trans_mat = Scaling(2, 1.5) * Rotation(np.pi/3)
trans_mat = Transformation(np.array([[-3,4],
                                     [1,2]])/2)
# trans_mat = Shear(0.5, 0) * Scaling(2, 1)

# *Translation(-50, -100)
print()
print("-"*20,'\n'*3)
print_colored_matrix(trans_mat.get_eigenvectors())
print("-"*20,'\n'*3)

eigen_vec_1 = trans_mat.get_eigenvectors()[:,0]
eigen_vec_2 = trans_mat.get_eigenvectors()[:,1]

# print(eigen_vec_1)

assert np.linalg.norm(eigen_vec_1) != 0

eigen_vec_1 = eigen_vec_1 / np.linalg.norm(eigen_vec_1) * 150
eigen_vec_2 = eigen_vec_2 / np.linalg.norm(eigen_vec_2) * 150

e_vec_1 = Vector(eigen_vec_1[0], eigen_vec_1[1])
e_vec_2 = Vector(eigen_vec_2[0], eigen_vec_2[1])

objects = [origin, grid, 
           vec_i, vec_j, vec1, vec2, vec2_o, circle,star,
             e_vec_1, e_vec_2
             ]+points

# Main game loop
running = True
i = 0
fix = False
show_trans_grid = True
stop = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                i = 0
                fix = True
            if event.key == pygame.K_RIGHT:
                i = 1
            if event.key == pygame.K_UP:
                fix = False
                stop = False
            if event.key == pygame.K_DOWN:
                show_trans_grid = not show_trans_grid
            if event.key == pygame.K_PAGEUP:
                trans_mat *= Rotation(-np.pi/9)
            if event.key == pygame.K_PAGEDOWN:
                trans_mat *= Rotation(np.pi/9)
            if event.key == pygame.K_COMMA:
                trans_mat = Translation(-100, 0)*trans_mat
            if event.key == pygame.K_PERIOD:
                trans_mat = Translation(100, 0)*trans_mat
            if event.key == pygame.K_SPACE:
                stop = not stop

        if event.type == pygame.MOUSEWHEEL:
            # if mouse scroll down scale up
            if event.y < 0:
                trans_mat *= Scaling(1.1, 1.1)
            # if mouse scroll up scale down
            if event.y > 0:
                trans_mat *= Scaling(0.9, 0.9)
            

    # Clear the screen
    screen.fill(black)

    # Draw a rectangle
    # draw_line(screen, red, (0, 0), (600, 600))

    origin.draw(screen, white)

    # rotate vectors
    for obj in objects:
        trans_mat(obj, i)


    
    # draw axes
    grid_fix.draw(screen, width=2)
    if show_trans_grid:
        grid.draw(screen, width=1)

    


    # draw vector
    vec1.draw(screen, yellow, width=2)
    vec1.draw(screen, yellow, width=1)
    
    vec2.draw(screen, colors.cyan, width=2)
    vec2.draw(screen, colors.cyan, width=1)

    vec2_o.draw(screen, colors.coral, width=2)

    vec_i.draw(screen, colors.green, width=3)
    vec_i.draw_fixed(screen, colors.green, width=1)

    vec_j.draw(screen, colors.orange, width=3)
    vec_j.draw_fixed(screen, colors.orange, width=1)

    star.draw(screen, colors.pink, width=3)
    # circle.draw(screen, colors.green, width=1)

    e_vec_1.draw(screen, colors.red, width=5)
    e_vec_1.draw_fixed(screen, colors.red, width=1)

    e_vec_2.draw(screen, colors.magenta, width=5)
    e_vec_2.draw_fixed(screen, colors.magenta, width=1)

    for point in points:
        point.draw(screen, colors.green, width=1)

    # (vec1 + vec2_o).draw(screen, colors.green, width=2)

    # Update the display
    pygame.display.flip()
    if not fix and not stop:
        i += 0.007
        i = min(i, 1)

# Quit Pygame
pygame.quit()
sys.exit()


