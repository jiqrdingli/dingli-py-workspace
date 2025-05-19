user_height = float(input("请输入你的身高cm: "))
user_height_m = user_height/ 100
user_weight = float(input("请输入你的体重kg: "))
gender = input("请输入你的性别")


BMI = user_weight / (user_height_m) ** 2

print("你的BIM值为"+str(BMI))
if gender == "男":
    if 16 < BMI < 18.5:
        print("你的体重正常")
    elif 18.5 < BMI < 22.5:
        print("你的体重1偏胖")
    elif 22.5 < BMI < 25:
        print("你体重偏胖")
    else:
        print("你的体重肥胖")
else:
    if 16 < BMI < 18.5 :
        print("你的体重偏胖")
    elif 14.5 < BMI < 18.4 :
        print("你的体重正常")
    else:
        print("你的体重肥胖")
