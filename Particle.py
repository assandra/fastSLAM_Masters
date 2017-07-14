class Particle:
    ' Particle is created to hypothesises the robots pose '
    def __init__(self, pose):
        self.pose = pose
        self.xval = pose[0]
        self.yval = pose[1]
        self.theta = pose[2]


    def set_mu_1(self, mu_1):

        self.mu_1 = mu_1
        self.mu_x = mu_1[0]
        self.mu_y = mu_1[1]
        self.mu_theta = mu_1[2]


    def set_covariance_1(self, covariance_1):
        self.covariance_1 = covariance_1

    def set_weight(self, weight):
        self.weight = weight