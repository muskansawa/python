Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("hey")
hey
>>> x==13
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x==13
NameError: name 'x' is not defined
>>> ch = input("enter any char:")
enter any char:f
>>> ptint(f)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    ptint(f)
NameError: name 'ptint' is not defined
>>> print(f)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(f)
NameError: name 'f' is not defined
>>> print(ch)
f
>>> print(x)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
>>> x =8
>>> x
8
>>> ch
'f'
>>> x.read()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x.read()
AttributeError: 'int' object has no attribute 'read'
>>> 
