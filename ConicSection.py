import numpy as np
import tqdm
from Transformation import Transformable
from pygame_draw_utils import draw_line


class ConicSection(Transformable):

    def __init__(self, a, b, c, d, e, f, width, height, n=300):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.width = width
        self.height = height
        self.n = n
        self.points = self.get_points()
        self.transform_points = [quart.copy() for quart in self.points]

    def get_points(self):

        theta = np.linspace(0, 2*np.pi, self.n)
        x = self.a * np.cosh(theta) * 100
        y = self.b * np.sinh(theta) * 100
        points1 = list(zip(x, y))
        points2 = list(zip(-x, y))
        points3 = list(zip(x, -y))
        points4 = list(zip(-x, -y))
        return points1, points2,  points3,  points4

    
    def draw(self, screen, color, width=0):
        for quart in self.transform_points:
            for i in range(len(quart)-1):
                x,y = quart[i+1]
                draw_line(screen, color, quart[i], (x, y), width=width)
        
    def transform(self, transform_matrix):
        for i in range(len(self.points)):
            for j in range(len(self.points[i])):
                self.transform_points[i][j] = transform_matrix.dot(self.points[i][j])