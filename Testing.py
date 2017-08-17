import numpy as np
from Particle import Particle
from Step1 import sample_motion_model_odometry, trial
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
raw_odom_file = open("data2.txt", "r")
#raw_laser_file = open("laser.txt", "r")

#Read all the data files in, line for file in a list data structure
odom_list = raw_odom_file.readlines()

#laser_list = raw_laser_file.readlines()

path = []
i = 0
print len(odom_list)
#Start loop to format and call function
while (i<len(odom_list) -3):
    print "New step"
    #Format odometry data
    odom_array_past = odom_list[i].split( ",")
    k = i +1
    odom_array_present = odom_list[k].split( ",")


    cntr1 = [float(odom_array_past[1]), float(odom_array_past[5]), float(odom_array_past[6]), float(odom_array_past[8])]
    cntr2 = [float(odom_array_present[1]), float(odom_array_present[5]), float(odom_array_present[6]), float(odom_array_present[8])]

    i = i + 1

    for x in range(len(particles)):
        print "This is " +str(x)
        particles[x].pose = sample_motion_model_odometry(cntr1, cntr2, particles[x])
        print particles[x].pose[0]





















