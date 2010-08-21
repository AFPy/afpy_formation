2.1.

>>> val = 1
>>> type(val)
<type 'int'>
>>> mess = 'Bienvenu à Pycon'
>>> type(mess)
<type 'str'>

2.2.

>>> a = 1
>>> type(a)
<type 'int'>
>>> a = 2 ** 31
>>> type(a)
<type 'long'>
>>> a = 1.
>>> type(a)
<type 'float'>
>>> a = 1j
>>> type(a)
<type 'complex'>
>>> a = True
>>> type(a)
<type 'bool'>
>>> a = 'Bonjour'
>>> type(a)
<type 'str'>
>>> a = ('Pycon', 75019)
>>> type(a)
<type 'tuple'>
>>> a = ['misc', 'ogrisel', 'dede']
>>> type(a)
<type 'list'>
>>> a = {'lang' : 'Python', 'type' : 'dynamic'}
>>> type(a)
<type 'dict'>

2.3.

>>> mess = "Bienvenue à Pycon"
>>> mess[0]
'B'
>>> mess[0:9]
'Bienvenue'
>>> mess[14:17]
'con'

On peut aussi omettre l'indice de début au de fin:

>>> mess[:8]
'Bienvenu'
>>> mess[12:]
'Pycon'

Voir partir de la fin:

>>> mess[-3:]
'con'

4.
>>> lst = [('Gar', 34), ('Her', 30)]
>>> lst[0] = ('Gard', 30)
>>> lst[1] = ('Herault', 34)
>>> lst
[('Gard', 30), ('Herault', 34)]

5. On ne peut pas modifier le contenu d'un non-mutable:

>>> dpt = ('Gar', 30)
>>> dpt[0] = 'Gard'
TypeError: 'tuple' object does not support item assignment

On est obligé de créer un nouvel objet mais le nom de
l'identifiant peut être identique:

>>> dpt = ('Gard', 30)

Le fonctionnement des identifiants est expliqué plus en
détail dans la section suivante.

