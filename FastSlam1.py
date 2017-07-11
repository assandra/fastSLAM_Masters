from Step1 import sample_motion_model_velocity
from Particle import Particle
import numpy as np


""" Initialize a set of N initial particles, these will 
  take for the pose vector, the known coordinates to begin with. 
  This will most likely come from ROS. 
  What will the initial covariance and mean values be for each landmark?"""
#Read in corrdinate values from ROS
#Use these values to initial N particles, using a particle array of size n

""" Read in the control vector reading from ROS"""

"""For each particle:
    Get the last pose estimate and the control vector, and send it to
    the velocity motion model sampling algorithm, which will return a new pose, this will
    then be used to initiate a new particle set"""

