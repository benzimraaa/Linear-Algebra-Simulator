from Transformation import Transformable
from pygame_draw_utils import *


class Circle(Transformable):

    def __init__(self, radius, center=(0,0)):
        self.radius = radius
        self.center = center
        self.center_trans = center

    def draw(self, screen, color, width=0):
        center = math_to_pixel(self.center_trans)
        if check_boundaries(center):
            pygame.draw.circle(screen, color, center, self.radius, width=width)
        
    def transform(self, transform_matrix):
        self.center_trans = transform_matrix.dot(self.center)
        return self