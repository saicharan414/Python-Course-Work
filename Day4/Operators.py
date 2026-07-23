Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Operators
#7types
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
a//b
2
a=20
#comparision Operator
a=10
b=20
a<b
True
a>b
False
a==b
False
a!=b
True
a<=b
True
a>=b
False
#Assignment
a=10
a+=10
a
20
a-=20
a
0
a+=30
a
30
a*=2
a
60
a//=2
a
30
#Membership
#str,list,tuple,set,dict
s="charan"
"a" in s
True
"z" in s
False
"f" not in s
True
#in membership operators dictionaries works only for keys not for values
#Identity operator
l=[1,2,3,4]
m=[1,2,3,4]
id(l)
2022353408448
>>> id(m)
2022353409152
>>> l is m
False
>>> n=l
>>> n
[1, 2, 3, 4]
>>> id(n)
2022353408448
>>> #Bitwise Operator
>>> & 0(0,0) 0(0,1),0(1,0) 1(1,1)
SyntaxError: invalid syntax
>>> 9&10
8
>>> 9^10
3
>>> 8>>2
2
>>> 8<<2
32
>>> 8|10
10
>>> #Output Formatting
>>> a=10
>>> b=10.3
>>> 
>>> c="nani"
>>> print(a,b,c)
10 10.3 nani
>>> print("a value is",a)
a value is 10
>>> print(a,b,c,sep="")
1010.3nani
>>> print(a,b,c,sep="\n")
10
10.3
nani
>>> print(a,b,c,sep="\t",end="@")
10	10.3	nani@
>>> print(f"a={a} b={b} c={c}")
a=10 b=10.3 c=nani
