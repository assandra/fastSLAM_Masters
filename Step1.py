"""" Step 1 module:
    Contains all the algorithms necessary to complete step 1 of FastSLAM 1.0. In this step a new robot pose is calculated for each particle
    given the new control.
"""


import random
import math
import numpy as np

def sample_motion_model_velocity(trans_vel, rot_vel, xval, yval, theta):
    """ This is the sampling algorithm which samples the velocity motion model to generate a new value for the robot pose.
        It samples this, with use of a given control vector and a past pose, which is uses to generate a random value for the recent pose,
        drawn from the velocity motion model. The values are perturbed by noise, which is modelled by a normal distribution on the control vectors.
        Inputs: Control vector at time t, Pose vector at time t-1
        Outputs: Pose vector at t
    """

    # Noise values, still need to determine, probably through testing
    alpha_1 = 0.99
    alpha_2 = 0.99
    alpha_3 = 0.99
    alpha_4 = 0.99
    alpha_5 = 0.99
    alpha_6 = 0.99

    #Need to find this value out - ROS
    duration = 1.1


    new_trans_vel = trans_vel + sample_normal_distribution(alpha_1*abs(trans_vel) + alpha_2*abs(rot_vel))
    new_rot_vel = rot_vel + sample_normal_distribution(alpha_3*abs(trans_vel) + alpha_4*abs(rot_vel))
    perturb_orient = sample_normal_distribution(alpha_5*abs(trans_vel) + alpha_6*abs(rot_vel))

    new_xval = xval - (new_trans_vel/new_rot_vel) * math.sin (theta) + (new_trans_vel/new_rot_vel) * math.sin (theta + new_rot_vel*duration)
    new_yval = yval + (new_trans_vel/new_rot_vel) * math.cos(theta) - (new_trans_vel/new_rot_vel) * math.cos(theta + new_rot_vel*duration)
    new_theta = theta + new_rot_vel*duration + perturb_orient*duration

    return "Vector still to print"

def sample_normal_distribution(b):
    """ Algorithm for sampling from an approximate normal distribution with zero mean and stardard deviation, b.
        Where the random function used, is assumed to be a pseudo random number generator with uniform distribution in [x,y]"""

    min = -1 * b
    max = b
    s = 0
    for x in range(0,12):
        rand = np.random.uniform(min,max)
        s = s + rand

    return s * 0.5
