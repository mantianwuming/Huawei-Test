import os
import numpy as np
import matplotlib
import cv2

cat_path = './1-map-training-2/cat.txt'
cross_path = './1-map-training-2/cross.txt'
road_path = './1-map-training-2/road.txt'


cross_dict = {}
with open(cross_path, 'r') as cross:
    for i in range(64):
        lines = cross.readline()
        lines = lines.strip( ).strip('()')
        lines = lines.split(',')
        # for j in range(len(lines)):
        #     if '(' in lines[j]:
        #         lines[j] = lines[j][1:]
        # print(lines)
        for j in range(len(lines)):
            lines[j] = int(lines[j])
        cross_dict[lines[0]] = lines[1:]
    print(cross_dict)
    np.save('cross.npy', cross_dict)

road_dict = {}
with open(road_path, 'r') as road:
    for i in range(105):
        lines = road.readline()
        lines = lines.strip( ).strip('()')
        lines = lines.split(',')
        # print(lines)
        for j in range(len(lines)):
            lines[j] = int(lines[j])
        # road_dict[lines[0]] = lines[1:]
        road_dict[lines[0]] = [lines[1], lines[3], lines[6]]
    print(road_dict)
    np.save('road.npy', road_dict)
