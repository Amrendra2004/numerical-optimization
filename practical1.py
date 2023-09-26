from numpy import arange
from scipy.optimize import line_search
from matplotlib import pyplot

def objective(x):
	return (-5.0 + x)**2.0

def gradient(x):
	return 2.0 * (-5.0 + x)

point = -5.0
direction = -3.0
print('start=%.1f, direction=%.1f' % (point, direction))
result = line_search(objective, gradient, point, direction)
print('Alpha: %s' % result[0])
