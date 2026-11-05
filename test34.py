import os
os.system('cls')

a = 10
b = 20
c = 30

bigger = a if (a > b) else  b

print("\nBigger is", bigger)
#------------------------------------------------

if (a > b):
    if (a > c):
        print("A is bigger")
    else:       
        print("C is bigger")
else:
    if (b > c):
        print("B is bigger")
    else:
        print("C is bigger")


print("A") if (a > b) else print("=") if (a == b) else print("B")


biggest = max(a, b, c)
print ("\nBiggest is(max)", biggest)


#------------------ while  break --------------
i = 1
while i < 10:
  print(i)
  if i == 5:
    break
  i += 1 

print('--------- while  continue --------')

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


print('-------- while  else ------------')

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("\ni is no longer less than 6\n")
