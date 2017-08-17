import matplotlib.pyplot as plt
import numpy as np
import math
f = open("2017-08-04-14-44-12_odom_laser_sonar_depth-pointsLASER.data", "r")

#Read all the data files in, line for file in a list data structure
f_list = f.readlines()

print len(f_list)

radians = [0]*61
increment = 0.0686688498
start_inc = -2.0943999291

print len(radians)

for x in range(0,61):
    start_inc = start_inc + increment

    radians[x] = start_inc
    print radians[x]


i = 0
array_data = []
while (i < len(f_list)):
    f_data = f_list[i].split(",")
    i = i+1
    del f_data[0:11]
    f_data = map(float, f_data)

    array_data.append(f_data)




array_radians = np.array(radians)
array_laser = np.array(array_data[0])
print len(array_radians)
print len(array_laser)


x_values = np.zeros([61,1], dtype=float)
y_values = np.zeros([61,1], dtype=float)
for j in range (0,61):
    x_values[j] = array_laser[j] * math.cos(array_radians[j])
    y_values[j] = array_laser[j] * math.sin(array_radians[j])
print x_values

plt.plot(x_values, y_values)
plt.xlabel("Range [m]")
plt.ylabel("Radians ")
plt.show()