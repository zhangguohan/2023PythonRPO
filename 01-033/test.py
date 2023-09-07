# num_char=len(input("what is your nma？"))
#
# new_num_char = str(num_char)
#d
# print("Yout name is " + new_num_char+"characters")
# a = 1
# print(7 + a )
#
# print(8 + float(1232.345))
#
# # Do not change these lines
# number = input("Enter a two-digit number: ")
# first_digit = int(number[0])
# second_digit = int(number[1])
#
# # Add the two digits
# result = first_digit + second_digit
#
# # Display the result
# print(f"The sum of {first_digit} and {second_digit} is {result}")
#
#



# study =int((199+46+200)/60)
# print(study)
#
# print( round(8/3))
#
# print( round(8//3))

#
# score = 0
# height =1.9
# isWing =True
#
# # f - string
#
# print(f"your socre is {score},yout height{height},you are wing {isWing}")
#
#


#
from datetime import datetime
#
# # 获取当前日期
current_date = datetime.now()
#
# # 接受用户输入的当前年龄
current_age = int(input("请输入您的当前年龄："))
#
# # 计算剩余寿命（假设最大寿命为80岁）
max_age = 80
remaining_years = max_age - current_age
#
# # 计算剩余天数、月数和周数
remaining_days = remaining_years * 365
remaining_months = remaining_years * 12
remaining_weeks = remaining_years * 52
#
# # 输出结果
print(f"当前时间为：{current_date.strftime('%Y-%m-%d')},假设你能活到{max_age},您还剩余 {remaining_days} 天, {remaining_months} 个月, {remaining_weeks} 个周.")
#
#
# # 获取用户输入的消费总额、小费百分比和消费人数
# total_bill = float(input("请输入消费总额："))
# tip_percentage = float(input("请输入小费百分比（例如，15表示15%）："))
# num_people = int(input("请输入消费人数："))
#
# # 计算小费金额
# tip_amount = (total_bill * tip_percentage) / 100
#
# # 计算每个人需要支付的金额
# total_per_person = (total_bill + tip_amount) / num_people
#
# # 输出结果
# print(f"每个人需要支付：{total_per_person:.2f} 元")


