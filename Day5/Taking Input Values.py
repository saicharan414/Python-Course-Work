Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#INPUT
a=input()
charan
a
'charan'
name=input()
nani
name
'nani'
age=input("enter the age: ")
enter the age: 21

age
'21'

type(age)
<class 'str'>

names=input("Enter the names: ")
Enter the names: sai charan 
names
'sai charan '
names.split()
['sai', 'charan']
names=input("enter the names: ").split()
enter the names: sai charan
names
['sai', 'charan']
names=input("enter the names: ").split()
enter the names: 1 2 3 4 5 6
names
['1', '2', '3', '4', '5', '6']
list(map(int,names))
[1, 2, 3, 4, 5, 6]
values=list(map(int,input().split()))
1 2 3 4 4 5 55 66
values
[1, 2, 3, 4, 4, 5, 55, 66]
values=list(map(float,input().split()))
1 2 3 4 4 5 55 66
values
[1.0, 2.0, 3.0, 4.0, 4.0, 5.0, 55.0, 66.0]
[1.0, 2.0, 3.0, 4.0, 4.0, 5.0, 55.0, 66.0]
[1.0, 2.0, 3.0, 4.0, 4.0, 5.0, 55.0, 66.0]
names =tuple(input("Enter the names: ").split())
Enter the names: shiva charan nani
names
('shiva', 'charan', 'nani')
('shiva', 'charan', 'nani')
('shiva', 'charan', 'nani')
values=set(map(float,input().split()))
values=set(map(int,input().split()))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    values=set(map(float,input().split()))
ValueError: could not convert string to float: 'values=set(map(int,input().split()))'
values=set(map(int,input().split()))
1 2 4 5
values
{1, 2, 4, 5}
  a,b=[1,2]
  
SyntaxError: unexpected indent
#Multiple Inputs
a,b=[1,2]
>>> a
1
>>> b
2
>>> a,b=(1,3)
>>> a
1
>>> b
3
>>> email,password=input("Enter the Email and Password: ")
Enter the Email and Password: charan@gmail.com 12345
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    email,password=input("Enter the Email and Password: ")
ValueError: too many values to unpack (expected 2)
>>> email,password=input("Enter the Email and Password: ")
Enter the Email and Password: charan@gmail.com
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    email,password=input("Enter the Email and Password: ")
ValueError: too many values to unpack (expected 2)
>>> email,password=input("Enter the Email and Password: ")
Enter the Email and Password: 
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    email,password=input("Enter the Email and Password: ")
ValueError: not enough values to unpack (expected 2, got 0)
>>> email,password=input("Enter the Email and Password: ").split()
Enter the Email and Password: charan@gmail.com 12345
>>> email
'charan@gmail.com'
>>> password
'12345'
>>> a,b,c=list(map(int,input().split()))
1 2 3
>>> a
1
>>> b
2
>>> c
3
