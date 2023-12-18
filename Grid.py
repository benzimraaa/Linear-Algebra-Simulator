import numpy as np
from pygame_draw_utils import *

class Grid:
    def __init__(self, width, height, cell_length=10, color=(255, 255, 255)) -> None:
        self.width = width
        self.height = height
        self.cell_length = cell_length
        self.color = color
        
        self.longitude_start = [(-width/2, i) for i in np.arange(-height/2, height/2, cell_length)]
        self.longitude_end = [(width/2, i) for i in np.arange(-height/2, height/2, cell_length)]
        
        self.latitude_start = [(i, -height/2) for i in np.arange(-width/2, width/2, cell_length)]
        self.latitude_end = [(i, height/2) for i in np.arange(-width/2, width/2, cell_length)]

        self.cellsX = len(self.longitude_start)
        self.cellsY = len(self.latitude_start)

        self.longitude_s_trans = self.longitude_start.copy()
        self.longitude_e_trans = self.longitude_end.copy()
        self.latitude_s_trans = self.latitude_start.copy()
        self.latitude_e_trans = self.latitude_end.copy()

    def draw(self, screen, width=1):
        for i in range(self.cellsX):
            draw_line(screen, self.color, self.longitude_s_trans[i], self.longitude_e_trans[i], width=width)
        for i in range(self.cellsY):    
            draw_line(screen, self.color, self.latitude_s_trans[i], self.latitude_e_trans[i], width=width)
    
    def transform(self, transform_matrix):
        for i in range(self.cellsX):
            self.longitude_s_trans[i] = transform_matrix.dot(self.longitude_start[i])
            self.longitude_e_trans[i] = transform_matrix.dot(self.longitude_end[i])
        for i in range(self.cellsY):
            self.latitude_s_trans[i] = transform_matrix.dot(self.latitude_start[i])
            self.latitude_e_trans[i] = transform_matrix.dot(self.latitude_end[i])
        return self