Identifiants livrés avec l'interpréteur: les builtins
-----------------------------------------------------
Au démarrage de l'interpréteur, des identifiants sont déjà présents:
ce sont les builtins. Nous avons déjà vu 'help' et 'type' ainsi que
'True' et 'False'.  Tous les types de bases présentés ('int', 'long',
'float', 'complex', 'bool', 'str', 'tuple', 'list' et 'dict') sont aussi
présents. Un nouvel identifiant très utile est 'None' qui permet de 
spécifier qu'un identifiant ne référence aucun objet significatif:

>>> a = None
>>> a is None
True

Nous utilisions jusqu'à maintenant '0'.

1. Trouvez les identifiants:

>>> a = None
>>> b = None
>>> c = None

permettant les résultats:

>>> type(a) is dict
True
>>> type(b) is list
True
>>> type(c) is str
True

L'appel des types de base permet aussi de faire des conversions:

>>> a = 1
>>> type(a) is int
True
>>> str(a)
'1'

2. Modifiez une des lignes pour obtenir le résultat final:
>>> num = 4
>>> dem = 3
>>> num/dem > 1
True

3. Cherchez la conversion de 'b' pour obtenir le résultat final:
>>> a = ('pycon', 75019)
>>> b = None
>>> b == ['pycon', 75019]  
True

Enfin un autre builtin intéressant est 'raw_input' qui permet 
de saisir une valeur sur la sortie standard:

>>> nom = raw_input('Votre now? ')

4. Tapez la ligne du dessus pour constater que l'entrée 
   standard est stockée dans dans l'identifiant 'nom' de type
   'str'. 


Exceptions
----------
Python permet aussi de lever des exceptions pour interrompre le flux
d'exécution d'un programme. Vous avez dû en voir passer si vous vous êtez
trompés dans la syntaxe ou l'utilisation d'un objet. Dans cette partie, 
la présentation se limite à la récupération d'exceptions dans l'interpréteur.
Les exceptions lancées par les objets de base sont en effet décrites par 
des classes livrées dans les builtins. Par exemple la conversion d'un 
entier en tuple n'est pas permise:

>>> a = tuple(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable

La dernière ligne affiche le type d'exception lancé, 'TypeError', 
une classe livrée avec l'interpréteur:

>>> TypeError
<type 'exceptions.TypeError'>

Vous pouvez ainsi saisir l'exception par une structure de type 
'try' qui essaie d'exécuter vos instructions, puis 'except' qui 
est appelée en cas d'erreur. Ainsi:

>>> try:
...   a = tuple(3)
... except TypeError:
...   print 'pas de conversion de 3 en tuple'
...
pas de conversion de 3 en tuple

Attention! L'indentation des blocks est significative en python. Essayez
toujours de respecter la convention 4 espaces pour un niveau d'indendation
(il faut penser a configurer son éditeur pour convertir les tabs en 4
espaces automatiquement).

5. Essayez de tapper une suite d'instructions saissisant un âge par
   'raw_input' et avertit l'utilisateur si l'âge rentré n'a pas pu
   être converti en réel.

