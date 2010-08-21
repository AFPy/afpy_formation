1.

>>> a = [3, 7]
>>> b = [3, 7]
>>> c = a
>>> a == [3, 7]
True
>>> b == a
True
>>> b is a
False
>>> c is a
True


2.

>>> b = 13
>>> c = 2
>>> not (b < 12)
True
>>> 1 <= c < 3
True


3.

>>> a = 6
>>> b = 5
>>> a + b > 10
True
>>> c = 4.
>>> d = 3.
>>> c / d > 1 
True


4.

>>> dec = '=' * 5 
>>> print dec + ' Bienvenu ' + dec
===== Bienvenu =====


5.

>>> samedi = [('PyQuery', 20), ('PyQt4', 10)]
>>> dimanche = [('twisted', 10), ('pyOCC', 20)]
>>> confs = samedi + dimanche
>>> confs
[('PyQuery', 20), ('PyQt4', 10), ('twisted', 10), ('pyOCC', 20)]

