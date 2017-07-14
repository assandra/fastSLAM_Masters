import math
import numpy as np

def importance_weighting(uncertainty_measurement,measurement, measurement_with_correction):

    det_S =np.linalg.det(2*math.pi*uncertainty_measurement)
    vector_product =1/math.sqrt(abs(det_S))

    difference_terms = (measurement - measurement_with_correction)
    exponent_gaussian =math.exp((-0.5) * difference_terms.T * np.linalg.inv(uncertainty_measurement)*difference_terms)

    weighting = vector_product*exponent_gaussian
    return weighting


