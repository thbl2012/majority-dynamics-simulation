import numpy as np
import math


class RandomGraph:

    def __init__(self, size):
        self.size = size
        self.vertices = np.empty(size, dtype=np.int)
        self.edges = None

    def set_color(self, mode='linear', **kwargs):
        if mode == 'linear':
            epsilon = kwargs['epsilon']
            pivot = int(self.size/2 + epsilon * self.size)
            self.vertices[:pivot] = 1
            self.vertices[pivot:] = -1
        elif mode == 'sqrt':
            c = kwargs['c']
            pivot = int(self.size/2 + c * math.sqrt(self.size))
            self.vertices[:pivot] = 1
            self.vertices[pivot:] = -1
        elif mode == 'const':
            c = kwargs['c']
            pivot = int(self.size/2 + c)
            self.vertices[:pivot] = 1
            self.vertices[pivot:] = -1

    def generate(self, p=.5):
        rd = np.random.random(size=(self.size, self.size))
        tmp = rd > p
        self.edges = tmp ^ tmp.T

    def diffuse(self, mode='majority'):
        tmp = np.copy(self.vertices)
        if mode == 'majority':
            self.vertices = (np.sum(self.edges * tmp, axis=1) > 0)*2 - 1

    def count(self):
        diff = self.vertices.sum()
        yes = (self.size + diff)//2
        no = (self.size - diff)//2
        return yes, no
