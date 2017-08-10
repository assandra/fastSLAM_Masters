import numpy as np
import random
def low_variance_sampling(particles):

    #Initialise empty list for particles
    new_particles = []

    #Find the size of the particle array
    M = len(particles)

    #Find a random number btw 0 and M^-1
    r = random.randrange(0,1/M)

    c = particles[0].weight

    i = 1

    for m in range(1, M):
        U = r + (m-1)/M

        while U > c:
            i = i+1
            c = c + particles[i].weight

        new_particles.append(particles[i])


    return new_particles
