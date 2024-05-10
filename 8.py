from math import sqrt

def f(x1, x2):
    return 7 * x1**2 + x2**2 - x1 * x2 + x1

def grad(f, x1, x2):
    h = 1e-6
    df_dx1 = (f(x1 + h, x2) - f(x1 - h, x2)) / (2 * h)
    df_dx2 = (f(x1, x2 + h) - f(x1, x2 - h)) / (2 * h)
    return [df_dx1, df_dx2]

# Пример расчета градиента в точке (1, 2)
grad_f_at_initial_point = grad(f, 1, 2)
print(grad_f_at_initial_point)
