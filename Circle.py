from CoordinatesTransform import *


class Circle:

    def __init__(self, radius, center=(0,0)):
        self.radius = radius
        self.center = center
        self.center_trans = center

    def draw(self, screen, color, width=0):
        center = math_to_pixel(self.center_trans)
        if check_boundaries(center):
            try:
                pygame.draw.circle(screen, color, center, self.radius, width=width)
            except Exception as e:
                print("Center: ",center)
                raise e
        else:
            print('circle out of bound')
            print(center)

    def transform(self, transform_matrix):
        self.center_trans = transform_matrix.dot(self.center)
        return self