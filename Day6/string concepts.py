Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="Python programming"
len(a)
18
#Ascii values
ord("p)
    
SyntaxError: unterminated string literal (detected at line 1)
ord("P")
    
80
ord("a")
    
97
#converting Ascii into chr
    
chr(66)
    
'B'
chr("0")
    
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    chr("0")
TypeError: 'str' object cannot be interpreted as an integer
ord("0")
    
48
min(a)
    
' '
max(a)
    
'y'
sorted(a)
    
[' ', 'P', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'r', 'r', 't', 'y']
#Case conversion
    
s="saicharan"
    
s.upper()
    
'SAICHARAN'
s.lower()
    
'saicharan'
s.swapcase()
    
'SAICHARAN'
s.casefold()
    
'saicharan'
s.title()
    
'Saicharan'
s.capitalize()
    
'Saicharan'
s.center(60,"-")
    
'-------------------------saicharan--------------------------'
s.center(100,"*")
    
'*********************************************saicharan**********************************************'
s.ljust(60,"-")
    
'saicharan---------------------------------------------------'
s.rjust(60,"-")
    
'---------------------------------------------------saicharan'
a="12"
    
a.zfill(10)
    
'0000000012'
#Search and Find Methods
    
x="python programming"
    
x.find("i")
    
15
x.find("-z")
    
-1
x.rfind("i")
    
15
x.index("i")
    
15
c.rindex("i")
    
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    c.rindex("i")
NameError: name 'c' is not defined
x.rindex('i')
    
15
x.count('p')
    
2
a="charan"
    
a.rfind('a')
    
4
#Replace and Modify
    
c="string is immutable"
    
c
    
'string is immutable'
c.replace("i",0)
    
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    c.replace("i",0)
TypeError: replace() argument 2 must be str, not int
c.replace("i","0')
          
SyntaxError: unterminated string literal (detected at line 1)
c.replace("i","0")
          
'str0ng 0s 0mmutable'
c.replace("string","Float")
          
'Float is immutable'
c.maketrans("aeiou","12345")
          
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
c.translate(c.maketrans("aeiou","12345"))
          
'str3ng 3s 3mm5t1bl2'
a="nenu mi chinna shimbam"
          
a
          
'nenu mi chinna shimbam'
c='string is immutable'
          
c
          
'string is immutable'
c.split()
          
['string', 'is', 'immutable']
c.split(',')
          
['string is immutable']
['string is immutable']
          
['string is immutable']

c.rsplit()
          
['string', 'is', 'immutable']
c.splitlines()
          
['string is immutable']
s='''
python
programming
language'''
          
s.splitlines()
          
['', 'python', 'programming', 'language']
s.join()
          
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    s.join()
TypeError: str.join() takes exactly one argument (0 given)
['', 'python', 'programming', 'language'].join()
          
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    ['', 'python', 'programming', 'language'].join()
AttributeError: 'list' object has no attribute 'join'
r=['', 'python', 'programming', 'language'].join()
          
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    r=['', 'python', 'programming', 'language'].join()
AttributeError: 'list' object has no attribute 'join'
''.join(['', 'python', 'programming', 'language'])
          
'pythonprogramminglanguage'
'&'.join(['', 'python', 'programming', 'language'])
          
'&python&programming&language'
>>> '$'.join(['', 'python', 'programming', 'language'])
...           
'$python$programming$language'
>>> s='java,python,c,cobol'
...           
>>> s.rpartition()
...           
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    s.rpartition()
TypeError: str.rpartition() takes exactly one argument (0 given)
>>> s.rpartition(',')
...           
('java,python,c', ',', 'cobol')
>>> s="     Hello world          "
...           
>>> s.strip()
...           
'Hello world'
>>> s.lstrip()
...           
'Hello world          '
>>> s.rstrip()
...           
'     Hello world'
>>> #Encoding and Decoding
...           
>>> text="Hello"
...           
>>> text.encode()#Encoding and Decoding
...           
b'Hello'
>>> text.encode()
...           
b'Hello'
>>> text="Hello $"
...           
>>> text.encode()
...           
b'Hello $'
