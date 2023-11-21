#3.WAP to compute the gradient and hessian of the flow

import sympy as sp

# Define variables
x1, x2 = sp.symbols('x1 x2')

# Define the function
f = 100 * (x2 - x1**2)**2 + (1 - x1)**2

# Compute the gradient
gradient = [sp.diff(f, var) for var in (x1, x2)]

# Compute the Hessian
hessian = [[sp.diff(gradient[i], var_j) for var_j in (x1, x2)] for i in range(len(gradient))]

# Display the results
print("Gradient:")
print(gradient)
print("\nHessian:")
print(hessian)
