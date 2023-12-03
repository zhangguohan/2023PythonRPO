def get_days_in_month(year,month):
    """
    :这是一个计算每月多少天的方法
    :param year:
    :param month:
    :return:
    """
    if month <1 or month>12:
        return None

    days_in_month = [31, 28, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):

        days_in_month[1] = 29
    return days_in_month[month - 1]

# 测试
year = int(input("输入年份: "))
month = int(input("输入月份: "))
days = get_days_in_month(year, month)

get_days_in_month()
if not days:
    print("月份输入错误")
else:
    print(f"{year}年{month}月有{days}天")

#print(days)
