import math
a = -1
b = -2
c = 3
# 计算判别式 D = b² - 4ac
D = b ** 2 - 4 * a * c
# 如果 D < 0，根是复数；否则，根据公式计算实数根
sqrt_D = math.sqrt(D)
# 根的表达式：(-b ± sqrt_D) / (2a)
x_plus = (-b + sqrt_D) / (2 * a)
x_minus = (-b - sqrt_D) / (2 * a)
print(f"根为：{x_plus} 和 {x_minus}")