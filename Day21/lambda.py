#even or odd using Lambda
iseven=lambda n:"even" if n%2==0 else "odd"
print(iseven(48))
print(iseven(45))
print(iseven(40))

#calling string using lambda
wish=lambda name:f"welcome {name}"
print(wish("charan"))
print(wish("nani"))

#max number using lambda function
max=lambda a,b: a if a>b else b
print(max(12,13))
print(max(15,18))
print(max(10,15))

#average
avg=lambda a,b,c:(a+b+c)/3
print(avg(4,5,6))
print(avg(4,5,9))

#finding domain name from mail
domain=lambda mail:(mail.split("@")[-1]).split(".")[0]
print(domain("charan@gmail.com"))
print(domain("charan@yahoo.com"))
print(domain("charan@outlook.com"))

#using strip()
domain = lambda mail: mail[mail.index("@") + 1:].strip(".com")
print(domain("charan@gmail.com"))

#gst
gst=lambda price:price+price*0.18
print(gst(1000))
print(gst(2000))

gst=lambda price:price-price*0.18
print(gst(1000))
print(gst(2000))

#lambda function using list
prices=[4000,5000,5600,8900]
res=list(map(lambda price:price+10,prices))
print(res)

#title of the names
names=["sai","charan","nani"]
res=list(map(lambda name: name.title(),names))
print(res)


prices=[4000,5000,5600,8900]
res=list(filter(lambda price:price>=5000,prices))
print(res)

#len() characters using filter
names=["nnnn","djfhkks","dsfkfdgs"]
res=list(filter(lambda name:len(names)<5,names))
print(res)

#reduce
from functools import reduce
l=[3,456,6,34,6,66]
res=reduce(lambda sum,i:sum+i,l)
print(res)


names=['dfks','dsfjhfkjg','djgksfgs']
res=reduce(lambda res,i:res+' - '+i,names)
print(res)
