"""
for i in range(5):
    for j in range(4):
        print("*", end="")
    print()
#i=outer loop
#j=inner loop
#print()=nextline

for i in range(5):
    for j in range(5):
        print(i, end="")
    print()

for i in range(5):
    for j in range(5):
        print(j, end="")
    print()

for i in range(5):#sumof i + j
    for j in range(5):
        print(i+j, end="")
    print()
   
for i in range(5):
    print("*"*(i+1))


for i in range(5):
    for j in range(5):
        print(j%2,end="")
    print()
"""
"""""

for j in range(5):
    if j % 2 == 1:
        print(1, end="")
    else:
        print(0, end="")

for i in range(5):
    for j in range(5):
        print((i+j)%2,end="")
    print()

"""
for i in range(5):
    for j in range(5-i):
        print("*",end="")
    print()

for i in range(5):
    print("*" * (5 - i))