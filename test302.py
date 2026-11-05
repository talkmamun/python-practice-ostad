

import os

os.system('cls')

my_string = """ABC
    XYZ
    PQR
    ABC
    """

print("String:", my_string)

#-----------------------------------------------
str_list = [line.strip() for line in my_string.splitlines() if line.strip()]

str_list.sort()
print("List:", str_list)
print("str_list[-1]:", str_list[-1], "\n")
#----------------------------------------------

result_set = set(str_list)
print("Set : " ,  result_set)
print("Sorted Set:", sorted(result_set))


#print("result[-1] : " , result_set[0] ,"\n" )
print("First element:", sorted(result_set)[0])
print("Last element:",  sorted(result_set)[-1], "\n")
#----------------------------------------------


result = tuple(sorted(str_list))
print("tuple : " ,  result)
print("result[-1] : " , result[-1] ,"\n")

#---------------------------------------------

