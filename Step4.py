import numpy as np

def resampling_particle(particle_array, Nmin, do_resample):

    #Get the total number of particles in the array
    N = len(particle_array)

    #Create a vector of size N and set to zero
    w = np.zeros(N)

    #Set each element in w to match the weight of the particle
    for x in range(0,N):
        w[x] = particle_array[x].weight

    #Calculate the sum of all particles weights
    wsum = np.sum(w) # do a test to ensure it is not zero

    #Go through all the particle weights and normalise them, using the weighted sum
    for x in range(0,N):
        w[x] = w[x]/wsum

    #Set all the particles weight to the normalised version
    for x in range(0,N):
        particle_array[x].weight = (particle_array[x].weight)/wsum

    #DONT KNOW WHAT THIS IS FOR
    Neff = 0

    #Initialize an array which will hold the kept particles
    keep = np.array()

    stratified_resample(w, keep, Neff)

    old_particles = np.empty(len(keep))

    if ((Neff <Nmin)  && (do_resample ==1)):
        for x in range(0, len(range)):
            particle_array[x] = old_particles[keep[x]]

        for x in range(0, N):
            new_w = 1/N
            particle_array[x].weight = new_w



def stratified_resample(w, keep, Neff):

    #Create a vector, which is the same size as the weights array
    wsqrd = np.array(len(w))

    #Calculate the sum of the weights from the weights array
    wsum = np.sum(w)

    #Iterate through the weights vector and normalise the weights array,
    #and then use these normalised weights to calculate the power of 2 value
    for x in range(0, len(w)):
        w[x] = w[x]/wsum
        wsqrd[x] = w[x]**2

    #Calculate Neff, which is 1/ sum of the squared weights
    Neff = 1/np.sum(wsqrd)

    #Make keep vector, equal the size of the weights array vector
    keep = np.empty(len(w))

    #Set all of keep values to -1
    for x in range(0,len(keep)):
        keep[x] = -1

    #Create a vector to use in next function
    select = np.array()
    stratified_random(len(w), select)
    cummulative_sum(w)

    ctr = 0
    for x in range(0, w(len)):
        while ((ctr < len) && (select[ctr] < w[x])):
            keep[ctr] = x
            ctr=ctr +1


def stratified_random(length, select):

    #Find the value of k, 1/size of keep array
    k = 1/length

    #Deterministic interval

    #temp value
    temp = k/2

    #add temp to the end of the select vector IM ASSUMING ITS EMPTY SO MAKE IT AT THE START
    select[0] = temp

    #While loop, where a new tem is calculated and and added to the select array
    counter = 1
    while (temp < 1-k/2):
        temp = temp+k
        select[counter] = temp
        counter = counter +1

    #There is an iterator and random value function that might still need implementing

def cummulative_sum(weight_array):
    csum_vector = weight_array

    for x in range(0, len(weight_array)):
        sum =0
        for y in range(0, x+1):
            sum += csum_vector[y]

        weight_array[x] = sum







