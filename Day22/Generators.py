"""def retrivedata():
    data=['1..100','101..200','201..300','301..400','401..500']
    for i in data:
        yield i
reels=retrivedata()
while True:
    status=input("[s]croll or [q]uit: ")
    if status=="s":
        print(next(reels))
    else:
        break

# Even numbers using generators
def even():
    i=0
    while True:
        i+=2
        yield i
n=10
res=even()
for i in range(n):
    print(next(res))

# Factorial using generators
def fact():
    i = 1
    while i <= n:
        if n % i == 0:
            yield i
        i += 1
n = 12
for i in fact():
    print(i)


# Prime Number using generators
def prime(n):
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            yield i
n=10
res=prime(n)
for i in res:
    print(i)
"""

def countdown(data):
    data=['10','9','8','7','6','5','4','3','2','1']
    for i in data:
        yield i
data=10
result=countdown(data)
for i in result:
    print(i)
