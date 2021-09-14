
"""ASSIGNMENT"""
prime = input("enter the number")
prime = int(prime)
flag = False
if prime > 1 :
for each in range(2,prime):
if (prime % each ) == 0:
    flag = True
    break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
