import numpy as np
import matplotlib.pyplot as plt

def golden_search(f, a, b, tol=1e-5):
    x = np.linspace(a, b, 400)    
    plt.figure(figsize=(8, 6))
    y = f(x)
    plt.plot(x, y, label='f(x)', color='red',zorder=-1)
    x_p = []
    y_p = []
    phi = (3 - 5**0.5) / 2
    c = a + phi * (b - a)
    d = b - phi * (b - a)
    x_p.extend([c,d])
    y_p.extend([f(c),f(d)])
    while abs(b - a) > tol:
        if f(c) < f(d):
            b = d
            x_p.extend([b])
            y_p.extend([f(b)])  
        else:
            a = c
            x_p.extend([a])
            y_p.extend([f(a)])
        c = a + phi * (b - a)
        d = b - phi * (b - a)
    plt.scatter(x_p, y_p, color='black', label='Точки сходимости')
    plt.scatter((b + a) / 2, f((b + a) / 2), color='blue', s=100, label='Точка минимума', zorder=2)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Метод Золотого Сечения')
    plt.legend()
    plt.grid(True)
    plt.show()
    return (b + a) / 2
def f(x):
    return x**2 + 4*x + 6
min_p = golden_search(f, -4, 6)
print(f"Минимум функции находится в точке: {min_p:.5f}, значение функции в этой точке: {f(min_p):.5f}")
