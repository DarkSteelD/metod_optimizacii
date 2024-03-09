import numpy as np
import matplotlib.pyplot as plt
def dichotomy(f, a, b, tol=1e-3, delta=1e-5):
    counter = 0
    x_p = []
    y_p = []
    x = np.linspace(a, b, 400)    
    plt.figure(figsize=(8, 6))
    y = f(x)
    plt.plot(x, y, label='f(x)', color='red',zorder=-1)
    while (b - a) > tol:
        midpoint = (a + b)
        x1 = (midpoint - delta)/2
        x2 = (midpoint + delta)/2
        f_x1 = f(x1)
        f_x2 = f(x2)
        x_p.extend([x1, x2])
        y_p.extend([f_x1, f_x2])
        counter+=1
        if f_x1 < f_x2:
            b = x2
        else:
            a = x1
    min_p = (a + b) / 2
    plt.scatter(x_p, y_p, color='black', label='Точки сходимости')
    plt.scatter(min_p, f(min_p), color='blue', s=100, label='Точка минимума', zorder=2)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Метод дихотомии')
    plt.legend()
    plt.grid(True)
    plt.show()
    print(counter)
    print(1/2**(counter/2))
    return min_p

def f(x):
    return x**2 + 4*x + 6

min_p = dichotomy(f, -4, 6)
print(f"Минимум функции находится в точке: {min_p:.5f}, значение функции в этой точке: {f(min_p):.5f}")
