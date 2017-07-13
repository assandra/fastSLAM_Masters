
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
    update_covariance =(jacobian_G * covariance * jacobian_G).T
        #jacobian_V* motion_noise_covariance*jacobian_V.T


    std_range = 1.2
    std_bearing = 1.2
    std_sign = 1.2

    q = np.matrix([[std_range**2,0,0],
                   [0,std_bearing**2,0],
                   [0,0,std_sign**2]])



    """Correction step in EKF"""
    #For each observed feature measurement, do:

    #j=c assigns to j the correspondence of the the i-th feature in the measurement vector
    q_helper = ((map[0] - update_mu[0])**2) + ((map[0] - update_mu[1])**2)

    z_predicted_measurement = np.array([math.sqrt(q_helper), math.atan2(map[1]-update_mu[1], map[0]-update_mu[0]) - update_mu[2], map[2]])[:,None]

    h_helper1 = (map[0] - update_mu[0])
    h_helper2 = (map[1] - update_mu[1])

    h_0 =update_mu[0]
    h_1_1 = -(map[0] - update_mu.item(0,0))/math.sqrt(q_helper)
    h_1_2 = -(map[1] - update_mu.item(1,0))/math.sqrt(q_helper)
    h_2_1 = (map[1] - update_mu.item(1,0))/q_helper
    h_2_1 = -(map[0] - update_mu.item(0,0))/q_helper
    jacobian_H= np.matrix([[h_1_1, h_1_2 , 0],
                          [h_2_1 ,h_2_1 , -1],
                          [0,0,0]])


    uncertainty_measurement = jacobian_H * update_covariance*(jacobian_H.T) + q

    try:
        inverse_S = np.linalg.inv(uncertainty_measurement)
    except np.linalg.LinAlgError:
        print "Matrix cannot be inverted"
    else:
        kalman_gain = update_covariance*(jacobian_H.T)*inverse_S

    difference_prediction = z_predicted_measurement-measurement
    update_mu = update_mu + kalman_gain*(difference_prediction)

    identity_3matrix = np.matrix(np.identity(3), copy=False)

    update_covariance1 = (identity_3matrix - kalman_gain*jacobian_H)*update_covariance
    return update_covariance
