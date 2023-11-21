                      # 2.Solving the LPP graphically
from pulp import *
import matplotlib.pyplot as plt
import numpy as np
# Create an object of a model
prob = LpProblem("Simple LP Problem", LpMinimize)
# Define the decision variables
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
# Define the objective function
prob += 60*x1 + 40*x2
# Define the constraints
prob += 4*x1 + 4*x2 >= 10.0, "1st constraint"
prob += 2*x1 + x2 >= 4.0, "2nd constraint"
prob += 6*x1 + 2*x2 <= 12.0, "3rd constraint"
# Solve the linear programming problem
prob.solve()
# Print the results
print ("Status: ", LpStatus[prob.status])
for v in prob.variables():
    print (v.name, "=", v.varValue)
print ("The optimal value of the objective function is = ", value(prob.objective))

# Plot the optimal solution
x = np.arange(0, 4)
plt.plot(x, 2.5 - x, label = '4x1 + 4x2 >= 10')
plt.plot(x, 4 - 2 * x, label= ' 2x1 + x2 >= 4')
plt.plot(x, 6 - 3 * x, label = '6x1 + 2x2 <= 12')
plt.plot(x, 2 - 2/3*x, '--')

# Define the boundaries of the feasible area in the plot
x = [0, 1.5, 1.75, 0]
y = [4, 1, 0.75, 6]
plt.fill(x, y, 'grey')

plt.text(0.1, 4, 'Feasible \n Region', size = '11')
plt.annotate('Optimal \n solution\n(1.5, 1)', xy = (1.5, 1.0))

plt.xlabel("x_1")
plt.ylabel("x_2")
plt.title('LPP:Graphical Solution')
plt.axis([0, 3, 0, 6])
plt.grid(True)
plt.legend()
plt.show()
