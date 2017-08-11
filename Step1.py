"""" Step 1 module:
    Contains all the algorithms necessary to complete step 1 of FastSLAM 1.0. In this step a new robot pose is calculated for each particle
    given the new control.
"""


import random
import math
import numpy as np

alpha_1 = 0.99
alpha_2 = 0.99
alpha_3 = 0.99
alpha_4 = 0.99
alpha_5 = 0.99
alpha_6 = 0.99

def sample_motion_model_velocity(control,past_pose):
    """ This is the sampling algorithm which samples the velocity motion model to generate a new value for the robot pose.
        It samples this, with use of a given control vector and a past pose, which is uses to generate a random value for the recent pose,
        drawn from the velocity motion model. The values are perturbed by noise, which is modelled by a normal distribution on the control vectors.
        Inputs: Control vector at time t, Pose vector at time t-1
        Outputs: Pose vector at t
    """

    # Noise values, still need to determine, probably through testing


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

def sample_motion_model_odometry(control_past,control_present, particle):
    """Algorithm for sampling from the conditional density based on odometry information"""

    #Calculate odometry values
    delta_rot1 = math.atan2(control_past[1]-control_present[1], control_past[0] - control_present[0]) - control_present[2]
    delta_trans = math.sqrt(((control_present[0] - control_past[0])**2) + (control_present[1] - control_past[1])**2)
    delta_rot2 = control_past[2] - control_present[2] - delta_rot1

    #Add noise
    perturb_delta_rot1 = delta_rot1 - sample_normal_distribution(alpha_1*abs(delta_rot1) + alpha_2*delta_trans)
    perturb_delta_trans = delta_trans - sample_normal_distribution(alpha_3*delta_trans + alpha_4*(abs(delta_rot1) + abs(delta_rot2)))
    perturb_delta_rot2 = delta_rot2 - sample_normal_distribution(alpha_1*abs(delta_rot2) + alpha_2*delta_trans)

    #Calculate new pose values
    x_val = particle.pose[0] + perturb_delta_trans*math.cos(particle.pose[2] + perturb_delta_rot1)
    y_val = particle.pose[1] + perturb_delta_trans*math.sin(particle.pose[2] + perturb_delta_rot1)
    theta_val = particle.pose[2] + perturb_delta_rot1 + perturb_delta_rot2

    new_pose = np.array(x_val, y_val, theta_val).T
    return new_pose


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