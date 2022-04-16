# 摇色子
from random import randint
def roll_dice(n=2):
	total = 0
	for _ in range(n):
		total += randint(1,6)
	return total
# 默认摇2个色子并相加
print(roll_dice())
# 摇3颗色子
print(roll_dice(3))

# 3个数求乘法
print("对3个数字求乘法：")
def multiply(a=1,b=2,c=3):
	return a*b*c
print("默认1,2,3相乘:")
print(multiply())
# 可以不按照顺序赋值
print("b=2，a=3，c=4")
print(multiply(b=2,a=3,c=4))
# 可以对部分参数赋值
print(multiply(4,5))

