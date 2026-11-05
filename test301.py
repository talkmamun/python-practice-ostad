

import os

os.system('cls')


str="BCDDA"
str = "" .join(sorted(str, reverse=True))

print("len(str) " , len(str))

for i in str:
    print(i) 


print()
# Reserver Order
for i in reversed(str):
    print(i)

#---------------------------------------

print("str : " , str)

str_list= list(str)
str_list.sort()
print("List : " , str_list)
print("str_list[-1] : " , str_list[-1])
#---------------------------------------

result =set(str)
result = sorted(result)
print("Set : " ,  result)
print("result[-1] : " , result[-1])
#----------------------------------------

result = tuple(str)
result = tuple(sorted(result))
print("tuple : " ,  result)
print("result[-1] : " , result[-1])
#----------------------------------------
