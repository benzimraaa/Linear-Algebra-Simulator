import numpy as np
import tqdm
from Transformation import *
from pygame_draw_utils import draw_line


class ConicSection(Transformable):

    def __init__(self, a, b, c, f, g, h, width, height, n=300, scale=10):
        self.a = a # x^2
        self.b = b # xy
        self.c = c # y^2
        self.f = f # x
        self.g = g # y
        self.h = h # 1
        self.width = width
        self.height = height
        self.n = n
        self.scale = scale
        self.points = self.get_points()
        self.transform_points = [quart.copy() for quart in self.points]

    def angle_of_rotation(self):
        if self.a == self.c:
            return np.pi/4
        else:
            return np.arctan(self.b/(self.a-self.c))/2

    def get_points(self):
        
        theta = np.linspace(0, 2*np.pi, self.n)
        x = self.a * np.cosh(theta) * self.scale
        y = self.b * np.sinh(theta) * self.scale
        points1 = list(zip(x, y))
        points2 = list(zip(-x, y))
        points3 = list(zip(x, -y))
        points4 = list(zip(-x, -y))
        if self.angle_of_rotation() != 0:
            return self.get_points_general(points1, points2,  points3,  points4)
        return points1, points2,  points3,  points4
    
    def get_points_general(self, points1, points2,  points3,  points4):
        p = Rotation(self.angle_of_rotation()).matrix
        A = np.array([[self.a, self.b/2], 
                      [self.b/2, self.c]])
        J = np.array([self.f,self.g])
        A = p.T @ A @ p

        J = J.T @ p
        J[0] /= -2*A[0,0]
        J[1] /= -2*A[1,1]

        Tr = (Transformation(p) * Translation(J[0], J[1])).matrix
        points1 = [Tr.dot(np.array(point)) for point in points1]
        points2 = [Tr.dot(np.array(point)) for point in points2]
        points3 = [Tr.dot(np.array(point)) for point in points3]
        points4 = [Tr.dot(np.array(point)) for point in points4]
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