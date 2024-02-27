
# def fn(name,age):
#     return '我的名字叫{0},今年{1}岁'.format(name,age)

# print(fn('张三',18))

# def  fn1(*num):
#     print('i-',num)
#     for i in num:
#         print(i)

# fn1([10,20,30])
# for i in 80.0:
#     print(i)

# x=20 

# def fn(*n) 表示元祖 (n,)，def fn(**n)表示 {集合}

# def fn2(**num):
#     print('num',num)  # {'name':20}

# fn2(name=20)

# def fn2(*num):
#     print('num',num)  # (222,)

# fn2(name=20)

# filter map 函数

# arr = [1,2,3,4]

# def fn (num):
#     return num > 2 

# arr1 = filter(fn,arr)

# print(list(arr1))

# arr = ('男','女')

# def fn (num):
#      print(num)
#      num = '女'
#      return num

# arr1 = map(fn,arr)

# print(list(arr1),arr)


# lambda函数是匿名函数，只有一条语句，不能有return

# a = 2;b=2

# def fn(x1,x2):
#     return lambda x1,x2 : x1+x2

# print(fn(a,b)(a,b))


# def fn (num):
#     return  lambda x : num * x 

# print(fn(2)(3))

# 215

# def sum(*numbers):
#     total=0.0
#     for number in numbers:
#         total+=number
#     return total


# x=200
# def print_value():
#     global x
#     x=100
#     print("函数中x={0}".format(x))

# print_value()

# print("全局中x={0}".format(x))