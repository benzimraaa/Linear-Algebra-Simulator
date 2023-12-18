from pygame_draw_utils import draw_line, draw_text
import numpy as np

class Vector:

    def __init__(self, x, y, start=(0,0)):
        self.x = x + start[0]
        self.y = y + start[1]
        self.dir = (x,y)
        self.start = start
        self.end = (self.x, self.y)
        p3, p4 = self.arrow_head()
        self.points = [self.start, self.end, p3, p4]
        self.transform_points = [self.start, self.end, p3, p4]

    def arrow_head(self, head_length=10, head_angle=0.5):
        """Return the coordinates of the arrow head."""
        # Calculate the angle of the vector with the start
        
        angle = np.arctan2(self.dir[1] , self.dir[0] )
        # print(angle/ np.pi * 180)
        # print((angle - head_angle)/ np.pi * 180)

        # Calculate components of the arrow head
        x1 = self.x - head_length * np.cos(angle - head_angle)
        y1 = self.y - head_length * np.sin(angle - head_angle)
        x2 = self.x - head_length * np.cos(angle + head_angle)
        y2 = self.y - head_length * np.sin(angle + head_angle)

        return (x1, y1), (x2, y2)

    def draw(self, screen, color, width=1):
        p1, p2, p3, p4 = self.transform_points
        draw_line(screen, color, p1, p2, width=width)
        draw_text(screen, f'({p2[0]/100:.2f}, {p2[1]/100:.2f})', p1, p2)
        draw_line(screen, color, p2, p3, width=width)
        draw_line(screen, color, p2, p4, width=width)

    def draw_fixed(self, screen, color, width=1):
        p1, p2, p3, p4 = self.points
        draw_line(screen, color, p1, p2, width=width)
        draw_line(screen, color, p2, p3, width=width)
        draw_line(screen, color, p2, p4, width=width)

    def transform(self, transform_matrix):
        for i in range(len(self.points)):
            self.transform_points[i] = transform_matrix.dot(self.points[i])
        return self
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, start=self.start)