
# 长字符串需要用三个引号""""""

# a1 = """ 

# 知识管理者1
# 知识管理者1
# 知识管理者1

# """

# print(a1)

# format 字符串格式化

# a2 = "我叫{0}，今年{1}岁".format('张三',18)

# a3 = "我叫{name},今年{age}岁".format(name='李四',age=19)

# a4 = "我叫{0},他叫{1},我今年{2},他今年{3}".format('张三','李四',18,19)

# print(a2,a3,a4)


# 字符串方法 find，replace split

# a1 = '我是张三，我爱北京天安门'

# print(a1.find('三'))

# print(a1.replace('张三','李四'))

# a2 = '1,2,3,4,5,6,7,8,9,10'

# print(a2.split(','))

# 案例 统计英文出现的长度

# a1 = 'I am Li Si, and I love Tiananmen Square in Beijing'

# a1 = a1.replace(',','')

# a1= len(a1.split(' '))
# print(a1)

# 案例 统计英文单个单词出现的次数

# a1 = """
# it wasthe best of times it was the worst of times.
# it was the age of wisdom it was the age of foolishness.   

# """

# a1= a1.replace('.','')

# a1 = a1.split()

# arr = {}

# for i in a1:
#     if i in arr:
#         arr[i] += 1
#     else:
#         arr[i] = 1

# print(arr)

s='world'


print(s[-1::-1])

print("{0} * {1} 长方形的面积:{2:2f}".format(10,20,10*20))

