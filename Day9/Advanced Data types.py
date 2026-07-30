Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={}
type(s)
<class 'dict'>
s=set()
s={1,2,3,4,5,4,5,6,8}s
SyntaxError: invalid syntax
s
set()
s={1,2,3,4,5,4,5,6,8}
s
{1, 2, 3, 4, 5, 6, 8}
a={1,2,5,4,3}
b={4,3,7,5,3}
a+b
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a={1,2,5,4,3}
b={4,3,7,5,3}
SyntaxError: multiple statements found while compiling a single statement
a={1,2,5,4,3}b={4,3,7,5,3}
SyntaxError: invalid syntax
a={1,2,3,4,5}
b={9,3,5,7}
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a|b
{1, 2, 3, 4, 5, 7, 9}
a&b
{3, 5}
a-b
{1, 2, 4}
a^b
{1, 2, 4, 7, 9}
{1}<=a
True
{1,2,3,4,5,}<=a
True
a.disjoin({9,10})
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.disjoin({9,10})
AttributeError: 'set' object has no attribute 'disjoin'. Did you mean: 'isdisjoint'?
a.disjoint({9,10})
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.disjoint({9,10})
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
a.isdisjoint({9,10})
True
a.union(b)
{1, 2, 3, 4, 5, 7, 9}
a.issubset(b)
False
a.issuperset(b)
False
a={1,2,3,4,5}
5 in a
True
max(a)
5
min(a)
1
sorted(a)
[1, 2, 3, 4, 5]
sum(a)
15
a={1,2,3,4,5}
b=a
b
{1, 2, 3, 4, 5}
>>> b.add(12)
>>> b
{1, 2, 3, 4, 5, 12}
>>> c=a.copy()
>>> c.add(12)
>>> c.add(13)
>>> c
{1, 2, 3, 4, 5, 12, 13}
>>> #dictionaries
>>> d={}
>>> d=dict()
>>> type(d)
<class 'dict'>
>>> d={'k1:2','k2:3','k4:5'}
>>> d
{'k2:3', 'k4:5', 'k1:2'}
>>> id(d)
1688227781024
>>> d['k4']='v4'
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    d['k4']='v4'
TypeError: 'set' object does not support item assignment
>>> d['k6']='v4'
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    d['k6']='v4'
TypeError: 'set' object does not support item assignment
>>> d['k6']='9'
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    d['k6']='9'
TypeError: 'set' object does not support item assignment
>>> d={}
>>> d[1]='int'
>>> d
{1: 'int'}
>>> d[12.3]='float'
>>> d
{1: 'int', 12.3: 'float'}
