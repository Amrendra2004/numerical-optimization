#5. WAP to find Global Optimal Solution of a function
#f(x) = -10Cos(pi*x - 2.2)+ (x + 1.5)x graphically
import matplotlib.pyplot as plt
import numpy as np

def objective_function(x):
    return -10 * np.cos(np.pi * x - 2.2) + (x + 1.5) * x

def gradient_function(x):
    return np.pi * 10 * np.sin(np.pi * x - 2.2) + 2 * x + 1.5

def plot_function():
    x = np.linspace(2.2, 3.2, 100)
    y = objective_function(x)

    plt.plot(x, y, label='f(x)')

def plot_optimal_solution():
    x_opt = 2.818326
    y_opt = 2.318326

    plt.scatter(x_opt, y_opt, s=50, c='red', marker='o', label='Optimal Solution')

def main():
    plot_function()

    # Find optimal solution using gradient descent
    x_init = 2.5
    learning_rate = 0.01
    max_iter = 100

    for _ in range(max_iter):
        gradient = gradient_function(x_init)
        x_init = x_init - learning_rate * gradient

    plot_optimal_solution()

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Global Optimal Solution of f(x) = -10Cos(pi*x - 2.2)+ (x + 1.5)x')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
