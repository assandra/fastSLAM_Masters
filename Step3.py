import math
import numpy as np

def importance_weighting(measurement_covariance,measurement, z_predicted_measurement, particles, x):

    det_S =np.linalg.det(2*math.pi*measurement_covariance)
    vector_product =1/math.sqrt(abs(det_S))

    difference_terms = measurement - z_predicted_measurement
    exponent_gaussian = math.exp((-0.5) * difference_terms.T * np.linalg.inv(measurement_covariance)*difference_terms)

    particles[x].weighting = vector_product*exponent_gaussian



