
# try:
#     i = input('输入一个整数')
#     num = 8888
#     print(num % int(i))
# except ValueError as e:
#     print('valuerr',e)
# except ZeroDivisionError as e:
#     print('zerodivisionerror',e)

# try:
#     i = input('输入一个整数')
#     num = 8888
#     print(num % int(i))
# except (ValueError,ZeroDivisionError) as e:
#     print('valuerr',e)

try:
    i = input('输入一个整数')
    num = 8888
    print(num % int(i))
except (ValueError,ZeroDivisionError) as e:
    print('valuerr',e)
finally:
    print('finally')
