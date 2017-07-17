from Step1 import sample_motion_model_velocity
from Particle import Particle
import numpy as np
import Testing
from Step2 import EKF_localization_known_correspondence
from Step3 import importance_weighting


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

mu_old = np.array([1,3,2])[:,None]
control_new = np.array([88,2])
covariance_old = np.matrix ([[2,6,5],
                             [2,4,1],
                             [3,5,1]])
environment_2d = np.array([1,2,1])
measurement_3D = np.array([2,2,2])[:,None]
measurement_corrected_vector = np.array([5,5,1])[:,None] # this will come from step 2

measurement_correction = EKF_localization_known_correspondence(mu_old, covariance_old, control_new, measurement_3D,1,environment_2d)
importance_weighting(measurement_correction, measurement_3D, measurement_corrected_vector)


keep = np.empty(5)
print keep
keep[0] =1
print keep

