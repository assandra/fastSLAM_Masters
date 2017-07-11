class Particle:
    """ Particle is created to hypothesises the robots pose"""
    #Initialisation, with known values for fields
  #  def __init__(self, xval, yval, theta):
    def __init__(self, pose):
        self.xval = pose[0]
        self.yval = pose[1]
        self.theta = pose[2]