import numpy as np


n_samples = 50
n_inputs = 1
x = 30*np.random.random((n_samples,n_inputs))
print type(x)
print x.shape


# generate sample data WE WILL HAVE REAL DATA HERE
x = np.zeros([n_samples, 1], dtype=float)
increment = 0.0686688498
start_inc = 0


print type(x)
print x

for i in range(0,61):
    start_inc = start_inc + increment

    x[i] = start_inc
    print x[i]