from math import sqrt

# Функция для вычисления нормы вектора
def norm_find(x):
    return sqrt(x[0]**2 + x[1]**2)

# Шаг метода градиентного спуска
def t_find(x, grad, r):
    numerator = (x[0] * grad[0] * r + 4 * x[0] * grad[0] + 2 * x[0] * grad[1] * r - x[0] * grad[1] + 2 * grad[0] * x[1] * r - grad[0] * x[1] - grad[0] * r + grad[0] + 4 * x[1] * grad[1] * r + 6 * x[1] * grad[1] - 2 * grad[1] * r)
    denominator = (grad[0]**2 * r + 4 * grad[0]**2 + 4 * grad[0] * grad[1] * r - 2 * grad[0] * grad[1] + 4 * grad[1]**2 * r + 6 * grad[1]**2)
    return numerator / denominator

# Метод градиентного спуска с учетом штрафа
def method_grad_spusk(x, r, eps1=0.1, eps2=0.2, M=20):
    k = 0
    while True:
        grad_f = [dx1func(x[0], x[1], r), dx2func(x[0], x[1], r)]

        if norm_find(grad_f) < eps1:
            return x

        if k >= M:
            return x

        t = t_find(x, grad_f, r)
        x1 = [x[0] - grad_f[0] * t, x[1] - grad_f[1] * t]

        if abs(func_big(x1[0], x1[1], r) - func_big(x[0], x[1], r)) < eps2 and norm_find([x[0] - x1[0], x[1] - x1[1]]) < eps2:
            print(f"{k}: ({x1[0]}; {x1[1]})\nFunc(xk): {func_small(x1[0], x1[1], r)}\n")
            return x1
        else:
            print(f"{k}: ({x1[0]}; {x1[1]})\nFunc(xk): {func_small(x1[0], x1[1], r)}\n")
            k += 1
            x = x1

# Новая функция цели
def func(x1, x2):
    return 7 * (x1**2) + x2**2 - x1 * x2 + x1

# Штрафная функция
def func_small(x1, x2, r):
    return (r / 2) * (x1 + 2 * x2 - 1)**2

# Комбинированная функция с учетом штрафа
def func_big(x1, x2, r):
    return 7 * (x1**2) + x2**2 - x1 * x2 + x1 + (r / 2) * (x1 + 2 * x2 - 1)**2

# Градиент функции по x1
def dx1func(x1, x2, r):
    return 14 * x1 - x2 + 1 + r * (x1 + 2 * x2 - 1)

# Градиент функции по x2
def dx2func(x1, x2, r):
    return 2 * x2 - x1 + 2 * r * (x1 + 2 * x2 - 1)

# Метод штрафа для решения задачи оптимизации
def penalty(x, r=1, c=10, eps=0.001):
    k = 0
    while True:
        x = method_grad_spusk(x, r)

        print(f"{k}: Метод штрафа\n")
        print(f"r = {r}\n")
        print(f"P = {func_small(x[0], x[1], r)}\n")
        print(f"R = {func_big(x[0], x[1], r)}\n")
        if func_small(x[0], x[1], r) <= eps:
            return x
        else:
            r += c * r
            k += 1

# Начальная точка оптимизации
x = [1, 3]
x = penalty(x)
print(f"Результат: {x}; f(x) = {func(x[0], x[1])}")
