'''
for i in range(1,11):
    print(i)

s="python programming"
for i in range(len(s)):
    if s[i] in "aeiou":
        print(i,s[i])
s=[1,2,3,4,5,6]
sum=0
for i in range(len(s)):
    if s[i]%2==0:
        sum+=s[i]
print(sum)

l=[1,2,3,4,5,6]
sum=0
for i in l:
    sum+=i
print(sum)

#Factorial of a number
n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
'''
n = int(input("Enter the number of products: "))

for i in range(n):
    print(f"\nProduct {i+1}")

    product_name = input("Enter the product name: ")
    product_price = int(input("Enter the product price: "))
    quantity = int(input("Enter the quantity: "))

    total = product_price * quantity

    print("Product Name:", product_name)
    print("Total Price:", total)
