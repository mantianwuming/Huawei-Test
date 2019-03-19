import numpy as np
import matplotlib.pyplot as plt

cross = np.load('cross.npy').item()
road = np.load('road.npy').item()
road_cross = np.load('road_cross.npy').item()
cross_coordinate = np.load('cross_coordinate.npy').item()

# print(road_cross)
print(cross_coordinate)

def draw_line(x1, y1, x2, y2):
    if x2 == 180 and y2 == 120:
        print(x1, y1, x2, y2)
    y = np.linspace(-1 * y1, -1 * y2, 100)
    x = np.linspace(x1, x2, 100)
    # print(x)
    # print(y)
    plt.plot(x,y)
    # if x1 == 180 and y1 == 120:
    #     print(x2,y2)
    # if x2 == 180 and y2 == 120:
    #     print(x1,y1)

x = []
y = []
for i in range(1, 65):
    # print(cross_coordinate[i][0])
    y.append(-1 * cross_coordinate[i][0])
    x.append(cross_coordinate[i][1])

# print(x,y)
plt.scatter(x,y, s=50)

for i in range(5000, 5105):
    num_1, num_2 = road_cross[i][0], road_cross[i][1]
    y1, x1 = cross_coordinate[num_1][0],  cross_coordinate[num_1][1]
    y2, x2 = cross_coordinate[num_2][0],  cross_coordinate[num_2][1]
    draw_line(x1,y1,x2,y2)
    # if x1 != x2 and y1 != y2:
    #     print(i, x1,y1,x2,y2)
# x = np.linspace(150,135);
# draw_line(150, 150, 150, 135)





plt.ylim(-200, 0)
plt.xlim(100, 300)
# plt.xticks(())
# plt.yticks(())

plt.show()
