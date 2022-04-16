# 定义阶乘函数
def fac(num):
	result = 1
	for n in range(1,num + 1):
		result *= n
	return result
# 输入数字计算阶乘结果
m = int(input('请输入要计算的阶乘: '))
print(fac(m))