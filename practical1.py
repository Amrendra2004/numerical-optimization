
import numpy as np

def line_search(f, df, x0, direction, alpha=0.1, beta=0.5):
    step_size = alpha
    while f(x0 + step_size * direction) > f(x0) - step_size * df(x0) @ direction:
        step_size *= beta

    return step_size

def gradient_descent(f, df, x0, max_iters=100, tol=1e-6):

    x_opt = x0
    f_opt = f(x0)

    for i in range(max_iters):
        direction = -df(x_opt)
        step_size = line_search(f, df, x_opt, direction)

        x_new = x_opt + step_size * direction
        f_new = f(x_new)

        if np.linalg.norm(x_new - x_opt) < tol or np.abs(f_new - f_opt) < tol:
            break

        x_opt = x_new
        f_opt = f_new

    return x_opt, f_opt

# Example usage
def f(x):
    return x**2 + 2 * x + 3

def df(x):
    return 2 * (x + 1)

x0 = np.array([1.0])
x_opt, f_opt = gradient_descent(f, df, x0)

print("Optimal solution:", x_opt)
print("Optimal function value:", f_opt)


