import numpy as np
import matplotlib.pyplot as plt
def dichotomy(f, a, b, tol=1e-5):
    x_p = []
    y_p = []
    x = np.linspace(a, b, 400)    
    plt.figure(figsize=(b-a, 6)) 
    y = f(x)
    plt.plot(x, y, label='f(x)', color='red',zorder=-1)
    while (b - a) > tol:
        x1 = a + (b - a) / 3
        x2 = b - (b - a) / 3
        f_x1 = f(x1)
        f_x2 = f(x2)
        
        x_p.extend([x1, x2])
        y_p.extend([f_x1, f_x2])
        
        if f_x1 > f_x2:
            a = x1
        else:
            b = x2
        
    min_p = (a + b) / 2
    plt.scatter(x_p, y_p, color='black', label='Точки Сходимости')
    plt.scatter(min_p, f(min_p), color='gray', s=100, label='Точка Минимума', zorder=2)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Метод Дихотомии')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return min_p
def f(x):
    return (x)**2 + 4*x +6
min_p = dichotomy(f, -4, 6)
print(f"Минимум функции находится в точке: {min_p:.5f}, значение функции в этой точке {f(min_p)}")
