# 可变参数
# 在不确定一个函数需要传递几个参数时，可以在参数前加*，该参数则定义为可变参数
def add(*a):
	total = 0
	for val in a:
		total += val
	return total
print(add(1,2,3,4))
print(add())
print(add(1,2))
