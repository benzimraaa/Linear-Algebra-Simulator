# abstract class for transformation

import numpy as np
import scipy
from Star import Star
from vector import Vector
from Grid import Grid
from Circle import Circle

class CustomArray(np.ndarray):
    def __new__(cls, input_array):
        obj = np.asarray(input_array).view(cls)
        return obj

    def __array_finalize__(self, obj):
        if obj is None:
            return

    def dot(self, other):
        other = np.array(other)
        if self.shape[0] == 3 and other.shape[0] == 2:
            other = np.array([other[0], other[1],1])
        return (super(CustomArray, self).dot(other)[:2]).real
        
    


class Transformation:
    def __init__(self, matrix):
        self.matrix = matrix

    def __call__(self, vector, t):
        """Rotate a Vector object."""
        if isinstance(vector, (Vector, Grid, Circle , Star)):
            vector.transform(self.get_transformation(t))
        else:
            raise NotImplementedError("Transformation of {} is not implemented.".format(type(vector)))
    
    def get_transformation(self, t):
        """M(t) = exp(t * ln(M))"""
        return CustomArray(scipy.linalg.expm(t * scipy.linalg.logm(self.matrix)))
    
    def __mul__(self, other):
        if other.matrix.shape != self.matrix.shape:
            return Transformation(self.to3d().dot(other.to3d()))
        return Transformation(self.matrix.dot(other.matrix))
    
    # *= operator overloading
    def __imul__(self, other):
        if other.matrix.shape != self.matrix.shape:
            self.matrix = Transformation(self.to3d().dot(other.to3d())).matrix
        else:
            self.matrix = self.matrix.dot(other.matrix)
        return self
    
    def to3d(self):
        if self.matrix.shape == (3,3):
            return self.matrix
        x = np.identity(3)
        x[:2,:2] = self.matrix
        return x

    def get_eigenvectors(self):
        return np.linalg.eig(self.matrix)[1]
    

class Rotation(Transformation):

    def __init__(self, angle):
        """Initialize the rotation matrix 2D."""
        self.angle = angle
        self.matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
        super().__init__(self.matrix)
        
class Scaling(Transformation):
    def __init__(self, sx, sy=None):
        if sy is None:
            sy = sx
        self.sx = sx
        self.sy = sy
        self.matrix = np.array([[sx, 0],
                                [0, sy]])
        super().__init__(self.matrix)

class Translation(Transformation):
    def __init__(self, tx, ty):
        self.tx = tx
        self.ty = ty
        self.matrix = np.array([[1, 0, tx],
                                [0, 1, ty],
                                [0, 0, 1]])
        super().__init__(self.matrix)

class Shear(Transformation):
    def __init__(self, shx, shy=0):
        """Initialize the shear matrix 2D."""
        self.shx = shx
        self.shy = shy
        self.matrix = np.array([[1, shx],
                                [shy, 1]])
        super().__init__(self.matrix)