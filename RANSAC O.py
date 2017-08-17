import numpy as np
import scipy
import matplotlib.pyplot as plt
import math
import sys




def find_line_model(points):
    """Find a line model for a set of given points"""

    m = (points[1, 1] - points[0, 1]) / (points[1, 0] - points[0, 0] + sys.float_info.epsilon)
    c = points[1, 1] - m * points[1, 0]

    return m, c


def find_intercept_point(m, c, x0, y0):
    x = (x0 + m * y0 - m * c) / (1 + m ** 2)
    y = (m * x0 + (m ** 2) * y0 - (m ** 2) * c) / (1 + m ** 2) + c

    return x, y

def ransac_plot(n, x, y, m, c, final=False, x_in=(), y_in=(), points=()):
    fname = "figure_" + str(n) + ".png"
    line_width = 1.
    line_color = '#0080ff'
    title = 'iteration ' + str(n)

    if final:
        fname = "final.png"
        line_width = 3.
        line_color = '#ff0000'
        title = 'final solution'

    plt.figure("Ransac", figsize=(15., 15.))

    # grid for the plot
    grid = [min(x) - 10, max(x) + 10, min(y) - 20, max(y) + 20]
    plt.axis(grid)

    # put grid on the plot
    plt.grid(b=True, which='major', color='0.75', linestyle='--')
    plt.xticks([i for i in range(min(x) - 10, max(x) + 10, 5)])
    plt.yticks([i for i in range(min(y) - 20, max(y) + 20, 10)])

    # plot input points
    plt.plot(x[:, 0], y[:, 0], marker='o', label='Input points', color='#00cc00', linestyle='None', alpha=0.4)

    # draw the current model
    plt.plot(x, m * x + c, 'r', label='Line model', color=line_color, linewidth=line_width)

    # draw inliers
    if not final:
        plt.plot(x_in, y_in, marker='o', label='Inliers', linestyle='None', color='#ff0000', alpha=0.6)

    # draw points picked up for the modeling
    if not final:
        plt.plot(points[:, 0], points[:, 1], marker='o', label='Picked points', color='#0000cc', linestyle='None',
                 alpha=0.6)

    plt.title(title)
    plt.legend()
    plt.savefig(fname)
    plt.close()

"""Given arguments
    data - a set of observed data points
    model - a model that can be fitted to the data points
    n - the mininium number of data values required to fit the model
    k - the maximum number of iterations allowed in the algorithm
    t - a threshold of close data values required to assert a model fits well to data"""

#RANSAC Parameters
k = 20 # number of iterations
t = 3 # threshold
n = 12 # minimum number of data values required to fit the model
Rratio =  n/k # ratio of data points which must line within the model to assert the model fits the data well

n_samples = 87 # number of input values WE USE SIZE OF DATA SET
outlier_ratio = 0.4 # ratio of data that seats outside the fitted line THIS IS JUST A DIFFERENCE

# NOT SURE WHAT THIS DOES
n_inputs = 1
n_outputs = 1

x = 30*np.random.random((n_samples,n_inputs))

# generate line's slope
perfect_fit = 0.5*np.random.normal(size=(n_inputs, n_outputs))

# compute output
y = scipy.dot(x, perfect_fit)

x_noise= x + np.random.normal(size=x.shape)
y_noise= y + np.random.normal(size=y.shape)

data = np.hstack( (x_noise, y_noise) )
ratio = 0.
model_m = 0.
model_c = 0.




for it in range(k):

    #pick two random points
    n = 2
    all_indices = np.arange(x_noise.shape[0])
    np.random.shuffle(all_indices)

    indices_1 = all_indices[:n]
    indices_2 = all_indices[n:]

    maybe_points = data[indices_1,:]
    test_points = data[indices_2,:]

    m, c = find_line_model(maybe_points)

    x_list = []
    y_list = []
    num = 0


    for ind in range(test_points.shape[0]):

        x0 = test_points[ind, 0]
        y0 = test_points[ind, 1]

        x1, y1 = find_intercept_point(m,c,x0, y0)


        dist = math.sqrt((x1-x0)**2 + (y1 - y0)**2)


        if dist < t :
            x_list.append(x0)
            y_list.append(y0)
            num+=1

    x_inliers = np.array(x_list)
    y_inliers = np.array(y_list)


    if num/float(n_samples) > ratio:
        ratio = num/float(n_samples)
        model_m = m
        model_c = c

    print '  inlier ratio = ', num/float(n_samples)
    print '  model_m = ', model_m
    print '  model_c = ', model_c

    ransac_plot(it, x_noise, y_noise, m, c, False, x_inliers, y_inliers, maybe_points)

    if num > n_samples*Rratio:
        print 'The model is found !'
        break

ransac_plot(0, x_noise, y_noise, model_m, model_c, True)

print '\nFinal model:\n'
print '  ratio = ', ratio
print '  model_m = ', model_m
print '  model_c = ', model_c

