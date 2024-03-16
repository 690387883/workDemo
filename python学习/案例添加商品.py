
from gettext import find


lst= []
for item in range(3):
    num=input('请添加商品：')
    lst.append(num)
goods=[]
while(True):
    inp=input('请输入要购买的商品编号：')
    flag=False
    if(inp == 'q'):
        if(len(goods)):
            print('退出购买，已选择{0}件商品，分别是{1}'.format(len(goods),','.join(goods)))
        else:
            print('退出购买')
        break
    for item in lst:
        if(item[0:4]==inp and len(lst) != len(goods)):
            print('添加购物车成功！')
            goods.append(item[4:])
            flag=True
            break
        else:
            flag=False
    if(len(lst) == len(goods)):
        print('添加完成，您添加的商品为：{0}'.format(','.join(goods)))
        break
    if(not flag):
        print('商品不存在,请重新添加')