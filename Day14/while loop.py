#While looop
#print numbers from 1 to 10
"""""
i=1
while i<=10:
    print(i)
    i+=1   
#printnumbers from 10 to 1
i=10
while i>=1:
    print(i)
    i-=1 
#print 1 to 100 even numbers
i=2
while i<=100:
    print(i)
    i+=2
#print 1 to 100 odd numbers
i=2
while i<=100:
    print(i)
    i+=1
"""""
"""""
#print 1 to 100 even numbers using if condition
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i = i + 1
#reverse a string using while loop
s="Python programming"
i=len(s)-1
while i>=0:
    print(s[i],end="")
    i-=1
#remove the zeros from a list using while loop
a=[1,0,2,0,3,0,4,0]
while 0 in a:
    a.remove(0)
print(a)
"""

#while loop using dictionary
d={}
total_bill=0
while True:
    product=input("Enter the product(for exit):" )
    if product=="exit":
        break
    price=int(input("Enter the price: "))
    total_bill+=price
    d[product]=price

print("Total bill:", total_bill)
print("Products purchased:", d)