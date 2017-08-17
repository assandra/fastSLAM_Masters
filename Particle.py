class Particle:

    mu = []
    covariance = []
    ' Particle is created to hypothesises the robots pose '
    def __init__(self, pose=[0,0,0]):
        self.pose = pose



    def add_mu(self, mu_1):
        self.mu.append(mu_1)

    def add_covar(self, covariance):
        self.covariance.append(covariance)









    def set_covariance_1(self, covariance_1):
        self.covariance_1 = covariance_1

    def set_weight(self, weight):
        self.weight = weight