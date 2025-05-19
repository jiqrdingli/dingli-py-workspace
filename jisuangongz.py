def salary_calculator(base, bonus=0, tax_rate=0.12):
    """薪资计算器（含默认参数和类型注解）"""
    total = base + bonus
    after_tax = total * (1 - tax_rate)
    return round(after_tax, 2)
print(salary_calculator(5000,1000))
print(salary_calculator(10000,2000))
print(salary_calculator(5000))