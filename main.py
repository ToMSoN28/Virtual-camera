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
STEP = 100

tm = TransformationMatrix()

def perspective_matrix(fov, aspect_ratio, near, far):
    f = 1.0 / np.tan(np.radians(fov) / 2)
    m = np.zeros((4, 4))
    m[0, 0] = f / aspect_ratio
    m[1, 1] = f
    m[2, 2] = (far + near) / (near - far)
    m[3, 2] = -1
    m[2, 3] = (2 * far * near) / (near - far)
    # m[2, 2] = -(far + near) / (far - near)  # Uwaga na znak minus!
    # m[2, 3] = -(2 * far * near) / (far - near)  # Uwaga na znak minus!
    # m[3, 2] = -1
    return m

def multi_matrix(m1, m2):
    return np.dot(m2, m1)


def main():
    t_m = np.eye(4)
    fov = 60
    aspect_ratio = 4/3
    near = 0.1
    far = 1000
    v_m = perspective_matrix(fov, aspect_ratio, near, far)

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
                        cube.points_transformation(multi_matrix(t_m, v_m))
                if event.key == pg.K_d:
                    t_m = multi_matrix(t_m, tm.translation_matrix(-STEP, 0, 0))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(multi_matrix(t_m, v_m))
                if event.key == pg.K_w:
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, STEP, 0))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(multi_matrix(t_m, v_m))
                if event.key == pg.K_s:
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, -STEP, 0))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(multi_matrix(t_m, v_m))
                if event.key == pg.K_UP:
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, 0, STEP))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(multi_matrix(t_m, v_m))
                if event.key == pg.K_DOWN:
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, 0, -STEP))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(multi_matrix(t_m, v_m))
                if event.key == pg.K_z:
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, -S_HEIGHT*0, -1000))
                    t_m = multi_matrix(t_m, tm.x_rotation_matrix(RADIOUS))
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, S_HEIGHT*0, 1000))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(multi_matrix(t_m, v_m))
                if event.key == pg.K_c:
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, -S_HEIGHT*0, -1000))
                    t_m = multi_matrix(t_m, tm.x_rotation_matrix(-RADIOUS))
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, S_HEIGHT*0, 1000))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(multi_matrix(t_m, v_m))
                if event.key == pg.K_e:
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, -S_HEIGHT*0, -1000))
                    t_m = multi_matrix(t_m, tm.y_rotation_matrix(RADIOUS))
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, S_HEIGHT*0, 1000))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(multi_matrix(t_m, v_m))
                if event.key == pg.K_q:
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, -S_HEIGHT*0, -1000))
                    t_m = multi_matrix(t_m, tm.y_rotation_matrix(-RADIOUS))
                    t_m = multi_matrix(t_m, tm.translation_matrix(0, S_HEIGHT*0, 1000))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(multi_matrix(t_m, v_m))
                if event.key == pg.K_LEFT:
                    # t_m = multi_matrix(t_m, tm.translation_matrix(0, -S_HEIGHT*0, 1000))
                    t_m = multi_matrix(t_m, tm.z_rotation_matrix(RADIOUS))
                    # t_m = multi_matrix(t_m, tm.translation_matrix(0, S_HEIGHT*0, -1000))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(multi_matrix(t_m, v_m))
                if event.key == pg.K_RIGHT:
                    # t_m = multi_matrix(t_m, tm.translation_matrix(0, -S_HEIGHT*0, 1000))
                    t_m = multi_matrix(t_m, tm.z_rotation_matrix(-RADIOUS))
                    # t_m = multi_matrix(t_m, tm.translation_matrix(0, S_HEIGHT*0, -1000))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(multi_matrix(t_m, v_m))
                if event.key == pg.K_n:
                    t_m = multi_matrix(t_m, tm.translation_matrix(-S_WIDTH*1, -S_HEIGHT*0, 0))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(multi_matrix(t_m, v_m))
                if event.key == pg.K_m:
                    t_m = multi_matrix(t_m, tm.translation_matrix(S_WIDTH*1, S_HEIGHT*0, 0))
                    print(t_m)
                    for cube in cubes:
                        cube.points_transformation(t_m)
                if event.key == pg.K_o:
                    # t_m = multi_matrix(t_m, tm.translation_matrix(-S_WIDTH*0.5, -S_HEIGHT*0.5, 0))
                    # t_m = multi_matrix(t_m, tm.zoom_matrix(1.2))
                    fov += 10
                    if fov > 120:
                        fov = 120
                    v_m = perspective_matrix(fov, aspect_ratio, near, far)
                    for cube in cubes:
                        # cube.points_transformation(t_m)
                        # cube.zoom_transformation(1.2)
                        cube.points_transformation(multi_matrix(t_m, v_m))
                    # t_m = multi_matrix(t_m, tm.translation_matrix(S_WIDTH*0.5, S_HEIGHT*0.5, 0))
                    # for cube in cubes:
                    #     cube.points_transformation(t_m)
                if event.key == pg.K_i:
                    # t_m = multi_matrix(t_m, tm.zoom_matrix(0.8))
                    fov -= 10
                    if fov < 20:
                        fov = 20
                    v_m = perspective_matrix(fov, aspect_ratio, near, far)
                    for cube in cubes:
                        # cube.points_transformation(t_m)
                        # cube.zoom_transformation(0.75)
                        cube.points_transformation(multi_matrix(t_m, v_m))
                        
                    
            elif event.type == pg.QUIT:
                dispaly = False
                
        pg.display.flip()
    pg.quit()
    
if __name__ == '__main__':
    main()
        
        
