1.
>>> a = {}
>>> b = []
>>> c = ''
>>> type(a) is dict
True
>>> type(b) is list
True
>>> type(c) is str
True

2. Par défaut, Python réalise une division entière puisqu'il
   a des entiers:
>>> num = 4
>>> dem = 3
>>> float(num)/float(dem) > 1
True

Par ailleurs, convertir seulement un élément aurait suffit
pour que le résultat de la division soit un réel:

>>> float(num)/dem > 1
True

3.
>>> a = ('pycon', 75019)
>>> b = list(a)
>>> b == ['pycon', 75019]
True

C'est ainsi que l'on peut obtenir le contenu d'un non mutable
puis le modifier. Vous pouvez jongler avec les types comme vous
en avez besoin.

4.
>>> nom = raw_input("Votre nom? ")
Votre nom?
>>> type(nom) is str
True

5. Exemple en console:

>>> age = raw_input("Votre âge? ")
Votre âge?
>>> try:
...     age = int(age)
...     print 'Age entré ', age
... except ValueError:
...     print 'Pas de conversion en entier pour ', age

Mais l'idéal serait de le faire avec une function dans un script
sinon il faut écrire les blocs à chaque essai.

