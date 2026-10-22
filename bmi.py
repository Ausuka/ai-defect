height = float(input("输入你的身高(米): "))
weight = float(input("输入你的体重(千克): "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    level = "体重过轻"
elif 18.5 <= bmi < 24:
    level = "体重正常"
elif bmi < 28:
    level = "体重过重"
else:
    level = "体重肥胖"
print(f"BMI指数为:{bmi:.2f} {level}")