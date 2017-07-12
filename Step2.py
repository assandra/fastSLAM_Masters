
import numpy as np
import math

def EKF_localization_known_correspondence(mu_1, covariance, control, measurement, correspondence, map):

    duration = 1.1 # try and make all these global variables
    alpha_1 = 0.99
    alpha_2 = 0.99
    alpha_3 = 0.99
    alpha_4 = 0.99
    alpha_5 = 0.99
    alpha_6 = 0.99

    theta = mu_1[2]
    angle_constant = theta + control[1]*duration

    g_1_3 = -(control[0]/control[1])*math.cos(theta) + (control[0]/control[1])*math.cos(angle_constant)
    g_2_3 = -(control[0]/control[1])*math.sin(theta) + (control[0]/control[1])*math.sin(angle_constant)
    jacobian_G = np.matrix([[1,0,g_1_3],
                           [0,1, g_2_3],
                           [0,0, 1]])

    v_1_1 = - math.sin(theta) + math.sin(angle_constant)
    v_1_2 = (control[0]*(math.sin(theta) -math.sin(angle_constant))) + (control[0]*math.cos(angle_constant)*duration)
    jacobian_V = np.matrix([[v_1_1, v_1_2],
                            [0, duration]])

    motion_noise_covariance = np.matrix([[(alpha_1*abs(control[0]) + alpha_2*abs(control[1])) ** 2, 0],
                                         [0, (alpha_3 * abs(control[0]) + alpha_4 * abs(control[1]))**2]])


    mu_1_1 = -(control[0]/control[1])* math.sin(theta) + (control[0]/control[1])*math.sin(angle_constant)
    mu_1_2 = (control[0]/control[1])*math.cos(theta) - (control[0]/control[1]*math.cos(angle_constant))
    update_mu = mu_1 + np.matrix([[mu_1_1],
                                  [mu_1_2],
                                  [control[1]*duration]])

    #This step cannt work, as it is multiplying two different size matrices
    update_covariance =jacobian_V* motion_noise_covariance*jacobian_V.T
    #jacobian_G * covariance * jacobian_G.T   +jacobian_V* motion_noise_covariance*jacobian_V.T

    std_range = 1.2
    std_bearing = 1.2
    st_sign = 1.2







    return update_covariance
