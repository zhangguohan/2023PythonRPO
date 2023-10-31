from art import logo  # 导入logo图像文件

bids = {}  # 创建一个空字典用于存储竞价信息
bidding_finished = False  # 设置一个标记用于判断竞价是否结束


# 定义函数find_highest_bidder用于在dictionary中找到最高出价
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # 遍历竞价记录dict,找到最高出价
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    # 打印最高出价和竞价者名字
    print(f"The winner is {winner} with a bid of ${highest_bid}")


# 主程序循环
while not bidding_finished:
    # 打印logo
    print(logo)
    # 接收用户输入
    name = input("What is your name?")
    price = int(input("What is your bid:$"))

    # 将姓名和出价记录到dict中
    bids[name] = price

    # 查询是否还有其他用户竞价
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.")
    if should_continue == "no":
        # 改变循环条件,退出循环
        bidding_finished = True
        # 调用函数获取最高竞价者
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("clear")  # 清屏操作

