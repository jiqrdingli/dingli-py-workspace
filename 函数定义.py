def calculate_salary(base_salary,jixiao,shuie=0.12):
    base_salary = input("请输入你的工资")
    gongzizonghe=base_salary+jixiao
    print(gongzizonghe)

    gongzizonghe * (1 - shuie)
    return round(gongzizonghe,2)
print(round())


def calculate_salary(base_salary, bonus, tax_rate=0.12):
    """计算税后工资"""
    total_salary = base_salary * bonus
    after_tax = total_salary * (1 - tax_rate)
    return round(after_tax, 2)

# 调用函数
result = calculate_salary(5000, 1.2)  # 基本工资5000，奖金系数1.2
print(f"税后工资: {result}")