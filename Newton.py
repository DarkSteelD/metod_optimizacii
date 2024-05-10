from math import sqrt

# Функция f
def f(x1, x2):
    return 7 * x1**2 + x2**2 - x1 * x2 + x1

# Градиент функции
def grad(f, x1, x2):
    h = 1e-6
    df_dx1 = (f(x1 + h, x2) - f(x1 - h, x2)) / (2 * h)
    df_dx2 = (f(x1, x2 + h) - f(x1, x2 - h)) / (2 * h)
    return [df_dx1, df_dx2]

# Обратная матрица Гессе
H_inv = [[2 / 27, 1 / 27], [1 / 27, 14 / 27]]

# Умножение матрицы на вектор
def mat_x_vec(mat, vec):
    return [sum(mat[i][j] * vec[j] for j in range(len(vec))) for i in range(len(mat))]

# Норма вектора
def norm_vec(x):
    return sqrt(x[0]**2 + x[1]**2)

# Начальные параметры
M = 50
eps1, eps2 = 0.1, 0.15
x0 = [1, 2]
x = [x0]
k = 0
first_check = False

# Основной цикл оптимизации
while k < M:
    gk = grad(f, x[-1][0], x[-1][1])
    d_k = [-x for x in mat_x_vec(H_inv, gk)]
    x_next = [x[-1][i] + d_k[i] for i in range(2)]
    x.append(x_next)

    if norm_vec(grad(f, x[-1][0], x[-1][1])) < eps1:
        break
    if k > 1 and norm_vec([x[-1][i] - x[-2][i] for i in range(2)]) < eps2:
        if first_check:
            break
        else:
            first_check = True
    else:
        first_check = False
    k += 1

# Печать результатов
print("x* ~=", x[-1])
print("f(x*) ~=", f(x[-1][0], x[-1][1]))
