from Circle import Circle
from Transformation import Transformable
from pygame_draw_utils import *
import numpy as np
import colors


class Star(Transformable):

    def __init__(self, vertices, inner_radius, outer_radius, center=(0,0)):
        self.vertices = vertices
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.center = center
        self.center_trans = Circle(5, center)

        self.points = self.get_points()
        self.points_trans = self.points.copy()

    def get_points(self):
        angle = np.pi / self.vertices
        points = []
        for i in range(self.vertices * 2):
            radius = self.outer_radius if i % 2 == 0 else self.inner_radius
            x = radius * np.cos(i * angle) + self.center[0]
            y = radius * np.sin(i * angle) + self.center[1]
            points.append((x, y))
        return points


    def draw(self, screen, color, width=0, text=False):
        model = self.points_trans
        for i in range(len(model)):
            x,y = model[(i+1)%len(model)]
            draw_line(screen, color, model[i], (x, y), width=width)

        if text:
            self.center_trans.draw(screen, color=colors.red,width=0)
            x, y = self.center_trans.center_trans
            draw_text(screen,  f'({x/100:.2f}, {y/100:.2f})', (x+20,y+20), (x+20,y+20))

    
    def draw_fixed(self, screen, color, width=0):
        model = self.points
        for i in range(len(model)):
            x,y = model[(i+1)%len(model)]
            draw_line(screen, color, model[i], (x, y), width=width)
            
        
    def transform(self, transform_matrix):
        for i in range(len(self.points)):
            self.points_trans[i] = transform_matrix.dot(self.points[i])
        self.center_trans.transform(transform_matrix)