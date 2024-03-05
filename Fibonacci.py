import numpy as np
import matplotlib.pyplot as plt
fib = [0, 1, 1]
def FibCreate(n):
    for i in range(len(fib), n + 1):
        fib.append(fib[-1] + fib[-2])
def fibonacci_search(f, a, b, n):
    FibCreate(n)
    x_p, y_p = [], []
    x_p.extend([a,b])
    y_p.extend([f(a),f(b)])
    x = np.linspace(a, b, 400)    
    plt.figure(figsize=(8, 6))
    y = f(x)
    plt.plot(x, y, label='f(x)', color='red',zorder=-1)
    for k in range(n - 1):
        
        l = a + (fib[n - k - 2] / fib[n - k]) * (b - a)
        m = a + (fib[n - k - 1] / fib[n - k]) * (b - a)
        
        if f(l) > f(m):
            a = l
            x_p.extend([a])
            y_p.extend([f(a)])
        else:
            b = m
            x_p.extend([b])
            y_p.extend([f(b)])    
    plt.scatter(x_p, y_p, color='black', label='Точки сходимости')
    plt.scatter((a + b) / 2, f((a + b) / 2), color='blue', s=100, label='Точка минимума', zorder=2)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Метод Фибонначи')
    plt.legend()
    plt.grid(True)
    plt.show()
    return (a + b) / 2

def f(x):
    return x**2 + 4*x + 6

a, b = -4, 6
n = 24       

min_point = fibonacci_search(f, a, b, n)
print(f"Минимум функции находится в точке: {min_point:.5f}, значение функции в этой точке: {f(min_point):.5f}")
