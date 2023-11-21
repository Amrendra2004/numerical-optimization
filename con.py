#6. WAP to solve constraint optimization Problem.

from scipy.optimize import minimize

# Define the objective function to minimize
def objective_function(x):
    return x[0]**2 + x[1]**2  # Example objective function 

# Define the constraint function(s)
def constraint_function(x):
    return x[0] + x[1] - 1  # Example constraint function 
# Initial guess
initial_guess = [0, 0]

# Define the bounds for each variable
variable_bounds = ((-10, 10), (-10, 10))  # Example bounds 

# Define the constraint(s)
constraints = {'type': 'eq', 'fun': constraint_function}

# Solve the constrained optimization problem
result = minimize(objective_function, initial_guess, bounds=variable_bounds, constraints=constraints)

# Display the result
print("Optimal solution:", result.x)
print("Optimal value of the objective function:", result.fun)
