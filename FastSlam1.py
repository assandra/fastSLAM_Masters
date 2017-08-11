import numpy as np
import math

from Particle import Particle

from Step1 import sample_motion_model_odometry
from Step2 import measurement_prediction, calculate_Jacobian, measurement_covariance, update_step, initialize_covariance
from Step3 import importance_weighting
from Step4 import low_variance_sampling


def fastSLAM_1_0(control_past,control_present, measurement, particles, landmarks):

    #Loop through each particle
    for x in range(len(particles)):

        #Prediction Step
        particles[x].pose = sample_motion_model_odometry(control_past, control_present, particles[x].pose)

        #Feature extractor - find one online
        features_observed = [(1,2,1),(1,2,2)]

        #Run through each observed feature
        for elem in features_observed:

            #if we have not seen this feature before
            if elem not in landmarks:

                #initialize the mean
                #THIS NEEDS TO BE CHECKED OVER
                new_mu = features_observed[elem]
                particles[x].add_mu(new_mu)

                #calculate Jacobian
                H = calculate_Jacobian(landmarks, particles, elem, x)

                #Initialize covariance
                covariance =initialize_covariance(H)
                particles[x].add_covariance(covariance)


            #If we have seen this landmark before
            elif elem in landmarks:
                #Update step
                z_predicted_measurement = measurement_prediction(landmarks, particles, elem, x)
                jacobian_H = calculate_Jacobian(landmarks, particles, elem, x)
                measurement_covar = measurement_covariance(jacobian_H, particles, elem, x)
                update_step(particles, jacobian_H, measurement_covar, measurement, z_predicted_measurement, elem,
                            x)

                #Importance weighting step
                importance_weighting(measurement_covariance,measurement, z_predicted_measurement, particles, x)



    new_particles = low_variance_sampling(particles)

    return new_particles
