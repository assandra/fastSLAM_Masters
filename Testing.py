from Step1 import sample_motion_model_velocity
from Step1 import sample_normal_distribution
from Particle import Particle
import random
import numpy as np

"""sample_normal_distribution
Test: Check that output data generates bell curve
yvalarray=[]

print len(yvalarray)
for i in range(1000):
    #xval= random.rand(0,1000,1)
    xval = -23
    yval = sample_normal_distribution(xval)

    yvalarray.append(yval)


print yvalarray

np.savetxt('test_normal.txt', yvalarray, delimiter=',') """

#control_new = np.array([-8,-2])
#pose_old = np.array([2,4,3])

#sample_motion_model_velocity(control_new[0], control_new[1], pose_old[0], pose_old[1], pose_old[2])

landmarks = [(1,2,1), (3,4,5)]

print landmarks[0][1]

















