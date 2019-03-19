import numpy as np
import matplotlib.pyplot as plt
cross = np.load('cross.npy').item()
road = np.load('road.npy').item()

road_cross = {}

f_cross = np.zeros((65, 65))
for i in range(105):
    road_cross[i+5000] = []
# print(road_cross)

for j in range(1, 65):
    for k in range(4):
        if cross[j][k] != -1:
            road_cross[cross[j][k]].append(j)

# print(road_cross)

np.save('road_cross.npy', road_cross)

for l in range(5000, 5105):
    f_cross[road_cross[l][0]][road_cross[l][1]] = f_cross[road_cross[l][1]][road_cross[l][0]] = 1
print(f_cross)

plt.imshow(f_cross)
plt.show()
