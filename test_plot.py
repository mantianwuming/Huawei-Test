import numpy as np
import matplotlib.pyplot as plt

# import sys
#
# sys.setrecursionlimit(1000000)

cross = np.load('cross.npy').item()
road = np.load('road.npy').item()
road_cross = np.load('road_cross.npy').item()

# # print('cross:', cross)
# # print('road:', road)
# print('road_cross:', road_cross)

class Plot_node():
    def __init__(self):
        self.f = np.zeros((300, 300))
        self.m = 150
        self.n = 150
        self.f[self.m][self.n] = 1
        self.flag = [1]
        self.cross = np.load('cross.npy').item()
        self.road = np.load('road.npy').item()
        self.road_cross = np.load('road_cross.npy').item()
        self.cross_coordinate = {1:[150, 150]}

    def find_node(self,node):
        # print(self.flag)
        if self.cross[node][0] != -1:
            num = self.cross[node][0]
            new_node = self.road_cross[num][0] if self.road_cross[num][0] != node else self.road_cross[num][1]
            if new_node not in self.flag:
                self.flag.append(new_node)
                length = self.road[num][0]
                self.m = self.m - length
                self.f[self.m][self.n] = 1
                print(new_node,self.m, self.n)
                self.cross_coordinate[new_node] = [self.m, self.n]
                self.find_node(new_node)
        if self.cross[node][1] != -1:
            num = self.cross[node][1]
            new_node = self.road_cross[num][0] if self.road_cross[num][0] != node else self.road_cross[num][1]
            if new_node not in self.flag:
                self.flag.append(new_node)
                length = self.road[num][0]
                self.n = self.n + length
                self.f[self.m][self.n] = 1
                print(new_node,self.m, self.n)
                self.cross_coordinate[new_node] = [self.m, self.n]
                self.find_node(new_node)
        if self.cross[node][2] != -1:
            num = self.cross[node][2]
            new_node = self.road_cross[num][0] if self.road_cross[num][0] != node else self.road_cross[num][1]
            if new_node not in self.flag:
                self.flag.append(new_node)
                length = self.road[num][0]
                self.m = self.m + length
                self.f[self.m][self.n] = 1
                print(new_node,self.m, self.n)
                self.cross_coordinate[new_node] = [self.m, self.n]
                self.find_node(new_node)
        if self.cross[node][3] != -1:
            num = self.cross[node][3]
            new_node = self.road_cross[num][0] if self.road_cross[num][0] != node else self.road_cross[num][1]
            if new_node not in self.flag:
                self.flag.append(new_node)
                length = self.road[num][0]
                self.n = self.n - length
                self.f[self.m][self.n] = 1
                print(new_node,self.m, self.n)
                self.cross_coordinate[new_node] = [self.m, self.n]
                self.find_node(new_node)
        return self.f

if __name__ == '__main__':
    p = Plot_node()
    f = p.find_node(1)
    print(f)

    count = 0
    for i in range(1,300):
        for j in range(1,300):
            if f[i][j] == 1:
                count += 1
                print(i,j)
    print(count)
    print(p.cross_coordinate)
    np.save('cross_coordinate.npy',p.cross_coordinate)
    plt.imshow(f)
    plt.show()
