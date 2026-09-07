res=[i for i in range(1,11)]
print(res)

n=12
res=[i for i in range(1,n+1) if n%i==0]
print(res)

r=[12,23,45,687,34,123,34,12,43,90]
res=[i if i%2==0 else 0 for i in r]
print(res)

r=[[12,23,45],[687,34,123],[34,43,90]]
res=[j for i in r for j in i if j%2==0]
print(res)

res={i for i in range(1,11)}
print(res)

#syntax for list comprehensions
"""
l=[updating for loop]
l=[updating for loop if condi]
l=[up1 if condi else up2 for loop]
l=[update for loop1 for loop2]
l=[update for loop1 for loop2 if condi]

#taking input in list comprehension
l=[int(input(f"Enter - {i+1}:")) for i in range(10)]
print(l)



names=[input(f"Enter names-{i+1}") for i in range(5)]
print(names)
"""
names={input(f"Enter the name-{i+1}:"):
       int(input("enter the marks"))
       for i in range(5)}
print(names)