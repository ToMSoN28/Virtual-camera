import numpy as np
from math import *

class Point:
     
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
        self.x_init = x
        self.y_init = y
        self.z_init = z

        self.zoom = 1.0
    
    def xyz_to_matrix(self):
        horizontal_m = np.matrix([self.x, self.y, self.z, 1])
        vertical_m = horizontal_m.reshape((4,1))
        return vertical_m
    
    def xyz_to_matrix1(self):
        horizontal_m = np.matrix([self.x_init, self.y_init, self.z_init, 1])
        vertical_m = horizontal_m.reshape((4,1))
        return vertical_m
    
    def get_transformation(self, transtormation_matrix):
        vertical_m = self.xyz_to_matrix1()
        new_positon = np.dot(transtormation_matrix, vertical_m)
        self.x = int(new_positon[0][0]*self.zoom)
        self.y = int(new_positon[1][0]*self.zoom)
        self.z = int(new_positon[2][0]*self.zoom)
        
    def zoom_transformation(self, value):

        self.zoom = self.zoom*value
        print(self.zoom)

        # self.x_init = self.x_init*value
        # self.y_init = self.y_init*value
        # self.z_init = self.z_init*value

        # self.x = self.x*value
        # self.y = self.y*value
        # self.z = self.z*value
        
    # def translation_matrix(self, tx, ty, tz):
    #     m = np.matrix([
    #         [1,0,0,tx],
    #         [0,1,0,ty],
    #         [0,0,1,tz],
    #         [0,0,0,1]
    #     ])
    #     self.get_transformation(m)
        
    # def x_rotation_matrix(self, radious):
    #     m  = np.matrix([
    #         [cos(radious),-sin(radious),0,0],
    #         [sin(radious),cos(radious),0,0],
    #         [0,0,1,0],
    #         [0,0,0,1]
    #     ])
    #     self.get_transformation(m)
        
    # def y_rotation_matrix(self, radious):
    #     m  = np.matrix([
    #         [cos(radious),0,sin(radious),0],
    #         [0,1,0,0],
    #         [-sin(radious),0,cos(radious),0],
    #         [0,0,0,1]
    #     ])
    #     self.get_transformation(m)
        
    # def z_rotation_matrix(self, radious):
    #     m  = np.matrix([
    #         [cos(radious),-sin(radious),0,0],
    #         [sin(radious), cos(radious),0,0],
    #         [0,0,1,0],
    #         [0,0,0,1]
    #     ])
    #     self.get_transformation(m)