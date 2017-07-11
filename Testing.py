from Step1 import sample_motion_model_velocity
from Particle import Particle
import numpy as np


vector_1 = np.array([1,3,2])[:,None]

p1 = Particle(vector_1)
print p1.theta



sample_motion_model_velocity(1.2, 3.4, 0,0,0)