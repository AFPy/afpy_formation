Mot-clés livrés avec l'interpréteur : les builtins
--------------------------------------------------

Au démarrage de l'interpréteur, des mots-clés sont déjà présents :
ce sont les primitives (builtins). Nous avons déjà vu 'help' et 'type' ainsi que
'True' et 'False'.  Tous les types de base présentés ('int', 'long',
'float', 'complex', 'bool', 'str', 'tuple', 'list' et 'dict') sont aussi
présents. Un nouvel identifiant très utile est 'None' qui permet de 
spécifier qu'un identifiant ne référence aucun objet significatif::

  >>> a = None
  >>> a is None
  True

L'appel des types de base permet de faire des conversions::

  >>> a = 1
  >>> type(a) is int
  True
  >>> str(a)
  '1'

le mot-clé 'len' permet de connaître la longueur d'une séquence ::

  >>> len("python")
  6
  >>> len([1, 2, 3])
  3

Enfin un autre builtin intéressant est 'raw_input' qui permet 
de saisir une valeur sur la sortie standard::

  >>> nom = raw_input('Votre now? ')
  Votre now? Christophe
  >>> nom
  'Christophe'
  >>> 

Exercice 4.1. Demandez l'age de l'utilisateur à l'aide de 'raw_input' et affichez son age
dans dix ans.


Exceptions
----------

L'interpréteur Python aime bien vous injurier avec des lignes de Traceback. Ce
n'est pas grave. La plupart du temps le message d'erreur explique très bien la
cause du problème pour peu que l'on parle anglais::

  >>> a = tuple(3)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: 'int' object is not iterable

La dernière ligne affiche le type d'exception lancé, 'TypeError', 
une classe livrée avec l'interpréteur::

  >>> TypeError
  <type 'exceptions.TypeError'>

Vous pouvez ainsi intercepter l'exception par une structure de type 
'try' qui essaie d'exécuter vos instructions, puis 'except' qui 
est appelée en cas d'erreur. Ainsi::

  >>> try:
  ...     a = tuple(3)
  ... except TypeError:
  ...     print 'pas de conversion de 3 en tuple'
  ...
  pas de conversion de 3 en tuple

Attention ! L'indentation des blocs est significative en Python. Essayez
toujours de respecter la convention 4 espaces pour un niveau d'indendation
(il faut penser a configurer son éditeur pour convertir les tabs en 4
espaces automatiquement).

