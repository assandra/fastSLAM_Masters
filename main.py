from Particle import Particle
from FastSlam1 import fastSLAM_1_0
import numpy as np
import matplotlib.pyplot as plt

"""Constants"""
MAX_PARTICLES = 3 # Total number of particles to begin with
MAX_DATA_ITEMS = 4 # This should be the number of lines in the data set


""" Initialize a set of N initial particles """
particles = []
for x in range(MAX_PARTICLES):
    particles.append(Particle())

""" Set up the list of known landmarks
    Note: This will be empty to begin with"""
landmarks = [(1,2,1), (3,4,5)]


""" Read in data from .txt files"""
#Open the raw data files
raw_odom_file = open("basicODO.txt", "r")
raw_laser_file = open("laser.txt", "r")

#Read all the data files in, line for file in a list data structure
odom_list = raw_odom_file.readlines()
laser_list = raw_laser_file.readlines()

path = []
#Start loop to format and call function
for x in range(0, MAX_DATA_ITEMS):

    #Format odometry data
    odom_array = np.array(odom_list[x].split( ))
    odom_array = odom_array.astype(np.float)

    #Format laser data
    laser_array = np.array(laser_list[x].split( ))
    laser_array = laser_array.astype(np.float)

    #Call fastSLAM 1.0 function
    new_path = fastSLAM_1_0(odom_array, laser_array, particles, landmarks)
    path.append(new_path)


x_values = []
y_values = []
for x in range(0, MAX_PARTICLES):
    x_values.append(particles[x].pose[0])
    y_values.append(particles[x].pose[1])

plt.plot(x_values,y_values)
plt.show()



