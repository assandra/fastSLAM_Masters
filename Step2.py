
import numpy as np
import math

def initialize_covariance(jacobian_H):
    std_range = 1.2
    std_bearing = 1.2
    std_sign = 1.2

    q = np.matrix([[std_range ** 2, 0, 0],
                   [0, std_bearing ** 2, 0],
                   [0, 0, std_sign ** 2]])


    covariance = (1/jacobian_H) * q * (1/jacobian_H).T

    return covariance

def measurement_prediction(landmarks, particles, elem, x):
    q_helper = ((landmarks[elem][0] - particles[x].mu[elem][0]) ** 2) + (landmarks[elem][1] - particles[x].mu[elem][1] ** 2)
    z_predicted_measurement = np.array([math.sqrt(q_helper), math.atan2(landmarks[elem][1] - particles[x].mu[elem][1],
                                                                    landmarks[elem][0] - particles[x].mu[elem][0])
                                    - particles[x].mu[elem][2], landmarks[elem][2]])

    return z_predicted_measurement

def calculate_Jacobian(landmarks, particles, elem, x):
    q_helper = ((landmarks[elem][0] - particles[x].mu[elem][0]) ** 2) + (landmarks[elem][1] - particles[x].mu[elem][1] ** 2)
    h_1_1 = -(landmarks[elem][0] - particles[x].mu[elem][0]) / math.sqrt(q_helper)
    h_1_2 = -(landmarks[elem][1] - particles[x].mu[elem][1]) / math.sqrt(q_helper)
    h_2_1 = (landmarks[elem][1] - particles[x].mu[elem][1]) / q_helper
    h_2_2 = -(landmarks[elem][0] - particles[x].mu[elem][0]) / q_helper
    jacobian_H = np.matrix([[h_1_1, h_1_2, 0],
                        [h_2_1, h_2_2, -1],
                        [0, 0, 0]])
    return jacobian_H


def measurement_covariance(jacobian_H, particles, elem, x):
    std_range = 1.2
    std_bearing = 1.2
    std_sign = 1.2

    q = np.matrix([[std_range ** 2, 0, 0],
                   [0, std_bearing ** 2, 0],
                   [0, 0, std_sign ** 2]])

    measurement_covariance = jacobian_H.T * particles[x].covariance[elem] * jacobian_H + q

    return measurement_covariance

def update_step(particles, jacobian_H, measurement_covariance, measurement, z_predicted_measurement, elem, x):
    kalman_gain = particles[x].covariance[elem] * jacobian_H * measurement_covariance
    particles[x].mu[elem] = particles[x].mu[elem] + kalman_gain * (measurement - z_predicted_measurement).T
    identity_3matrix = np.matrix(np.identity(3), copy=False)
    particles[x].covariance[elem] = (identity_3matrix - kalman_gain * jacobian_H.T) * particles[x].covariance[elem]


