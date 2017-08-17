import math
import numpy as np

#NEED TO CONSIDER HAVING MINIMUM VALUE OF ASSOCIATION
def nearest_neighbours(extracted_landmarks, observed_landmarks):

    #Loop through all extracted landmarks
    for i in range(0, len(extracted_landmarks)):

        #Method for getting the minimum distance
        minimum_distance = math.sqrt( ((extracted_landmarks[i][0] - observed_landmarks[0][0]) **2) + (extracted_landmarks[i][1] - observed_landmarks[0][1])**2)
        #Loop through all observed landmarks
        for j in range(1, len(observed_landmarks)):

            #Calculate the euclidean distance between the two landmarks
            euclid_distance = math.sqrt( ((extracted_landmarks[i][0] - observed_landmarks[j][0]) **2) + (extracted_landmarks[i][1] - observed_landmarks[j][1])**2)

            #See if this is a minimum
            if (euclid_distance < minimum_distance):

                #THERE NEEDS TO BE A CHECK HERE TO SEE IF THE LANDMARK HAS AN N VALUE LARGE ENOUGH
                minimum_distance = euclid_distance
                pairs = [i, j]

    return pairs


def validation_gate(extracted_landmark, observed_landmark, pose):

    #Add some gaussian noise to each term
    range_noise = 1
    bearing_noise = 1

    #Calculate the predicted range and bearing
    z_predicted_range = math.sqrt( ( (observed_landmark[0] - pose[0]) **2) + ( (observed_landmark[1] - pose[1]) **2 )) + range_noise
    z_predicted_bearing = math.atan((observed_landmark[1] - pose[1])/(observed_landmark[0] - pose[0])) - pose[2] + bearing_noise

    z_predicted = np.array([z_predicted_range, z_predicted_bearing])

    #Calculate the range and bearings of extracted landmark

    range_actual = math.sqrt((extracted_landmark[0] ** 2) + extracted_landmark[1] ** 2)
    bearing_actual = math.atan2(extracted_landmark[1], extracted_landmark[0])

    #THIS NEEDS RECONSIDERED
    z_actual = np.array([range_actual, bearing_actual])

    #Calculate innovation

    innovation = z_actual - z_predicted

    #Get the covariance matrix from Step 2


    innovsation_constant =


