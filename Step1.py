"""" Step 1 module:
    Contains all the algorithms necessary to complete step 1 of FastSLAM 1.0. In this step a new robot pose is calculated for each particle
    given the new control.
"""


import random
import math
import numpy as np

def sample_motion_model_velocity(control,past_pose):
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

    s1 = alpha_1*abs(control[0]) + alpha_2*abs(control[1])

    """test_array = []
    for x in range(100):
        test_s = sample_normal_distribution(alpha_1*abs(control[0]) + alpha_2*abs(control[1]))
        test_array.append(test_s)

    np.savetxt('test_motion_model.txt', test_array, delimiter=',')"""

    new_trans_vel = control[0] + sample_normal_distribution(alpha_1*abs(control[0]) + alpha_2*abs(control[1]))
    print "This is tthe parameter passed to the sample normal algorithm " +str(s1)

    print "This is the new trans value " + str(new_trans_vel)

    #new_rot_vel = rot_vel + sample_normal_distribution(alpha_3*abs(trans_vel) + alpha_4*abs(rot_vel))
    new_rot_vel = control[1]
    print "This is the new rot value " + str(new_rot_vel)
    #perturb_orient = sample_normal_distribution(alpha_5*abs(trans_vel) + alpha_6*abs(rot_vel))
    perturb_orient = 1

    new_xval = past_pose[0] - (new_trans_vel/new_rot_vel) * math.sin(past_pose[2]) + (new_trans_vel/new_rot_vel) * math.sin(past_pose[2] + new_rot_vel*duration)
    new_yval = past_pose[1] + (new_trans_vel/new_rot_vel) * math.cos(past_pose[2]) - (new_trans_vel/new_rot_vel) * math.cos(past_pose[2] + new_rot_vel*duration)
    new_theta = past_pose[2] + new_rot_vel*duration + perturb_orient*duration

    pose_new = np.array([new_xval, new_yval, new_theta])
    pose_new1 = np.transpose(pose_new)


    return pose_new1



def sample_normal_distribution(b):
    """ Algorithm for sampling from an approximate normal distribution with zero mean and stardard deviation, b.
        Where the random function used, is assumed to be a pseudo random number generator with uniform distribution in [x,y]"""

    min = -1 * b
    max = b

    """Checks on the min and max values
    print "This is max " +str(max)
    print "This is mix " + str(min)
    """

    s = 0

    for x in range(0,12):
        rand = np.random.uniform(min,max)
        s = s + rand

    return s * 0.5


def sample_motion_model_odometry(control, past_pose):
    return 0