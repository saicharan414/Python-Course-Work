Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> c='stringds'
>>> c.startswith('py')
False
>>> c.endswith('s')
True
>>> c.isupper()
False
>>> c.islower()
True
>>> c.isaplha()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    c.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
>>> c.isalpha
<built-in method isalpha of str object at 0x000001D066A3F530>
>>> c.isalpha()
True
>>> c.isalphanum
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    c.isalphanum
AttributeError: 'str' object has no attribute 'isalphanum'. Did you mean: 'isalnum'?
>>> c.isalphanum()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    c.isalphanum()
AttributeError: 'str' object has no attribute 'isalphanum'. Did you mean: 'isalnum'?
>>> c.isalnum()
True
