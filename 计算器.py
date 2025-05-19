##我是一个求平均值的代码

print("我是一个求平均值的代码" )
count = 0
total = 0
user_input = input("请输入数字,输出结束后输入q结束程序")
while user_input != "q":
    num = float(user_input)
    total += num
    count = count + 1
    user_input = input("请输入数字,输出结束后输入q结束程序")
    total += float(user_input)
if count == 0:
    ruslt = 0
else:
    ruslt = total/count
print(str(ruslt))
