
# 找到了返回re对象，没找到返回None
import re

# email = 'someone@example.com'

# print(re.match(r'someone@example.com','someone@example.com'))

# print(re.search(r'someone@example.com',email)) 
# print(re.findall(r'someone@example.com',email)) # ['someone@example.com']

# 
num = r'abd123sss'
print(re.sub('\d','',num)) 
