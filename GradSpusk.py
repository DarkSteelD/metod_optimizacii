import numpy as np
import matplotlib.pyplot as plt

def f(x):
    x1, x2 = x
    return 7*x1**2 + x2**2 - x1*x2 + x1

def grad_f(x):
    x1, x2 = x
    df_dx1 = 14*x1 - x2 + 1
    df_dx2 = 2*x2 - x1
    return np.array([df_dx1, df_dx2])

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
    
def gradient_descent_with_golden_section(f, grad_f, x0, alpha=1, tol=1e-5, max_iter=100):
    x = x0
    trajectory = [x]
    print(f"Initial position: {x}")
    for i in range(max_iter):
        grad = grad_f(x)
        if np.linalg.norm(grad) < tol:
            print(f"Convergence reached at iteration {i}.")
            break
        def func(alpha): return f(x - alpha * grad)
        optimal_alpha = golden_section_search(func, 0, alpha)
        x = x - optimal_alpha * grad
        trajectory.append(x)
        print(f"Iteration {i+1}: position = {x}, gradient = {grad}, step size = {optimal_alpha}")
    print(f"Final position: {x}, Function value: {f(x)}")
    return x, np.array(trajectory)

x0 = np.array([1, 2])
optimal_x, trajectory = gradient_descent_with_golden_section(f, grad_f, x0)
X1, X2 = np.meshgrid(np.linspace(-2, 2, 400), np.linspace(-1, 3, 400))
Z = 7*X1**2 + X2**2 - X1*X2 + X1
fig, ax = plt.subplots(figsize=(8, 6))
CS = ax.contour(X1, X2, Z, levels=np.logspace(-1, 3, 20), cmap='viridis')
ax.plot(trajectory[:, 0], trajectory[:, 1], 'r*-')
ax.plot(optimal_x[0], optimal_x[1], 'bo') 
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_title('Градиентный спуск с использованием метода золотого сечения')
plt.show()
