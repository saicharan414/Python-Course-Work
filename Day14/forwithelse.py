for i in range(1,10):
    if i==16:
        break
    print(i)
else:
    print("end of the loop")


'''''
#Mobile Unlocking
pin=1234
for _ in range(5):
    epin=int(input("Enter your pin: "))
    if pin==epin:
        print("unlock")
        break
    else:
        print("wrong pin")
else:
    print("Try after 30 Seconds")

'''''

"""

#Find the Factors 
a=int(input("Enter a number: "))
print("Factors: ",end="")
for i in range(1,a+1):
    if a%i==0:
        print(i,end=" ")
"""""
"""""
#prime number using factors count
n=int(input("Enter a number: "))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("prime number")
else:
    print("Not a prime number")
"""""
#Prime number optimized
n=int(input("Enter a number: "))
for i in range(2,n//2+1):
    if n%i==0:
        print("Not a prime number")
        break
else:
    print("prime number")