import numpy as np

class Cube(object):
    vertices = []
    
    def __init__(self):
        self.vertices.append(np.matrix([1,1,1]))
        self.vertices.append(np.matrix([-1,1,1]))
        self.vertices.append(np.matrix([-1,-1,1]))
        self.vertices.append(np.matrix([-1,-1,-1]))
        self.vertices.append(np.matrix([1,-1,1]))
        self.vertices.append(np.matrix([1,-1,-1]))
        self.vertices.append(np.matrix([1,1,-1]))
        self.vertices.append(np.matrix([-1,1,-1]))
        
    




