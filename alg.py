#4. WAP to find global optimal solution of a function
#f(x) = -10cos(pi*x - 2.2)+(x+1.5)x algebraically
import numpy as np
import scipy.optimize as opt

def f(x):
    return -10*np.cos(np.pi*x - 22) + (x+1.5)*x

x0 = [-2]
minimizer_kwargs = {"method":"BFGS"}
optimization_algorithm = opt.basinhopping(f, x0 , minimizer_kwargs =minimizer_kwargs,niter = 200)
print("1-D function")
print (optimization_algorithm.message[0])

optimized_x = optimization_algorithm.x
optimized_fun = optimization_algorithm.fun

print("optimized x: ",optimized_x)
print("optimized function value: ",optimized_fun)
