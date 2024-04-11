import numpy as np
import pygame as pg
import sys
from cube import Cube
from trans_matrix import TransformationMatrix
from math import *

S_WIDTH = 800
S_HEIGHT = 600
GRAY = (200,200,200)
COLOR = (255,0,0)

RADIOUS = (15 * pi ) / 180
STEP = 50

tm = TransformationMatrix()

def multi_matrix(m1, m2):
    return np.dot(m2, m1)


def main():
    t_m = np.eye(4)
    pg.init()
    screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))
    paths = sys.argv[1:]
    
    cubes = []
    for path in paths:
        cube = Cube(path, screen)
        cubes.append(cube)
    dispaly = True
    while dispaly:
        screen.fill(GRAY)
        for cube in cubes:
            cube.draw_cube()
        
        pg.draw.line(screen, COLOR, (S_WIDTH/2-25, S_HEIGHT/2), (S_WIDTH/2+25, S_HEIGHT/2), 2)
        pg.draw.line(screen, COLOR, (S_WIDTH/2, S_HEIGHT/2-25), (S_WIDTH/2, S_HEIGHT/2+25), 2)
        
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                # screen.fill(GRAY)
                if event.key == pg.K_a:
                    t_m = multi_matrix(t_m, tm.translation_matrix(STEP, 0, 0))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(t_m)
                if event.key == pg.K_d:
                    t_m = multi_matrix(t_m, tm.translation_matrix(-STEP, 0, 0))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(t_m)
                if event.key == pg.K_w:
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, STEP, 0))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(t_m)
                if event.key == pg.K_s:
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, -STEP, 0))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(t_m)
                if event.key == pg.K_UP:
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, 0, -STEP))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(t_m)
                if event.key == pg.K_DOWN:
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, 0, STEP))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(t_m)
                if event.key == pg.K_z:
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, -S_HEIGHT*1, 1000))
                    t_m = multi_matrix(t_m, tm.x_rotation_matrix(RADIOUS))
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, S_HEIGHT*1, -1000))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(t_m)
                if event.key == pg.K_c:
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, -S_HEIGHT*1, 1000))
                    t_m = multi_matrix(t_m, tm.x_rotation_matrix(-RADIOUS))
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, S_HEIGHT*1, -1000))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(t_m)
                if event.key == pg.K_e:
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, -S_HEIGHT*1, 1000))
                    t_m = multi_matrix(t_m, tm.y_rotation_matrix(RADIOUS))
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, S_HEIGHT*1, -1000))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(t_m)
                if event.key == pg.K_q:
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, -S_HEIGHT*1, 1000))
                    t_m = multi_matrix(t_m, tm.y_rotation_matrix(-RADIOUS))
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, S_HEIGHT*1, -1000))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(t_m)
                if event.key == pg.K_LEFT:
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, -S_HEIGHT*1, 1000))
                    t_m = multi_matrix(t_m, tm.z_rotation_matrix(RADIOUS))
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, S_HEIGHT*1, -1000))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(t_m)
                if event.key == pg.K_RIGHT:
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, -S_HEIGHT*1, 1000))
                    t_m = multi_matrix(t_m, tm.z_rotation_matrix(-RADIOUS))
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, S_HEIGHT*1, -1000))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(t_m)
                if event.key == pg.K_i:
                    for cube in cubes:
                        # cube.points_transformation(tm.translation_matrix(0, -S_HEIGHT*1, 0))
                        cube.zoom_transformation(1.2)
                        # cube.points_transformation(tm.translation_matrix(0, S_HEIGHT*1, 0))
                if event.key == pg.K_o:
                    for cube in cubes:
                        # cube.points_transformation(tm.translation_matrix(0, -S_HEIGHT*1, 0))
                        cube.zoom_transformation(0.8)
                        # cube.points_transformation(tm.translation_matrix(0, S_HEIGHT*1, 0))
                    
            elif event.type == pg.QUIT:
                dispaly = False
                
        pg.display.flip()
    pg.quit()
    
if __name__ == '__main__':
    main()
        
        
