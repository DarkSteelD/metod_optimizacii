import numpy as np
import matplotlib.pyplot as plt

def f(x):
    x1, x2 = x
    return 7 * x1**2 + x2**2 - x1 * x2 + x1

def grad_f(x):
    x1, x2 = x
    return np.array([14 * x1 - x2 + 1, 2 * x2 - x1])

def golden_section_search(f, a, b, tol=1e-5):
    gr = (np.sqrt(5) + 1) / 2
    c = b - (b - a) / gr
    d = a + (b - a) / gr
    while abs(c - d) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - (b - a) / gr
        d = a + (b - a) / gr
    return (b + a) / 2

def fletcher_reeves(x0, grad_f, tol=1e-5, max_iter=1000):
    x = x0
    grad = grad_f(x)
    p = -grad
    values = [f(x)]
    trajectory = [x.copy()]
    
    for k in range(max_iter):
        def func(alpha): return f(x + alpha * p)
        alpha = golden_section_search(func, 0, 1)
        x_new = x + alpha * p
        grad_new = grad_f(x_new)
        if np.linalg.norm(grad_new) < tol:
            print(f"Convergence achieved at iteration {k}")
            break
        
        print(f"Iteration {k}: x = {x_new}, f(x) = {f(x_new)}, alpha = {alpha}")
        
        beta = np.dot(grad_new, grad_new) / np.dot(grad, grad)
        p = -grad_new + beta * p
        x = x_new
        grad = grad_new
        values.append(f(x))
        trajectory.append(x.copy())
    
    return x, values, trajectory

x0 = np.array([1, 2])

optimal_x, f_values, trajectory = fletcher_reeves(x0, grad_f)
print("Optimal point:", optimal_x)
print("Function value at optimal point:", f_values[-1])

X1, X2 = np.meshgrid(np.linspace(-2, 3, 400), np.linspace(-1, 4, 400))
Z = 7*X1**2 + X2**2 - X1*X2 + X1
trajectory = np.array(trajectory)

fig, ax = plt.subplots(figsize=(8, 6))
CS = ax.contour(X1, X2, Z, levels=np.logspace(-1, 3, 20), cmap='viridis')
ax.plot(trajectory[:, 0], trajectory[:, 1], 'ro-')  
ax.plot(optimal_x[0], optimal_x[1], 'bo')  
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_title('Trajectory of Fletcher-Reeves Method')
plt.show()
