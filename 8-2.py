# import matplotlib.pyplot as plt
# import numpy as np

# # Просто демонстрация, не конкретные буквы
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# y = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

# plt.scatter(x, y)
# plt.title('С 8 марта, дорогие преподаватели!')
# plt.xlabel('X координата')
# plt.ylabel('Y координата')
# plt.show()
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(12, 10))
ax.axis('off')
ax.text(0.5, 0.5, 'С 8 Марта,\nдорогие девушки!', fontsize=42, ha='center', color = 'red')
plt.show()

