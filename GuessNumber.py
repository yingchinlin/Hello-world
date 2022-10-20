import random
m = random.randint(1,100)
total = 5
count = 0

while True:
    n = int(input("请输入1-100间的整数："))
    if n < m:
        print("猜小了")
    elif n > m:
        print("猜大了")
    else:
        print("猜对了")
        break

    count = count +1
    if count >= total:
        print(f"你猜了{total}次了，正确答案是{m}游戏结束")
        break
