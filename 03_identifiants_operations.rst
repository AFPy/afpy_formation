Fonctionnement des variables
----------------------------

Les variables en Python sont des références sur des structures de données
allouées en mémoire par l'interpréteur (écrit en C).

Lorsque vous tapez ::

  >>> a = 1
  >>> b = 2

Voici ce qui se passe en mémoire, PyIntObject étant le
type entier de Python:

    Identifiants | Mémoire
    a ------------> PyIntObject(1)
    b ------------> PyIntObject(2)

Maintenant passons 'a' à 3 ::

  >>> a = 3

Voici l'état de l'interpréteur juste après votre ligne:

    Identifiants | Mémoire
                    PyIntObject(1)
    b ------------> PyIntObject(2)
    a ------------> PyIntObject(3)

Ainsi Python a laissé tomber le premier entier qui valait
1 pour en créer un nouveau avec la valeur 3 correspondant
à l'identifiant 'a'. Donc 'a' n'est pas une variable de type
entier dans laquelle on va affecter 1 puis 3.

Continuons la découverte du fonctionnement avec un tuple ::

  >>> a = ("pycon", 75019)
  >>> b = a

Voici le status de l'interpréteur:

    Identifiants | Mémoire
    a
     \_____________
      _____________ PyTupleObject(("pycon", 75019))
     /
    b

'a' et 'b' sont donc égaux, on peut tester l'égalité
entre 2 identifiants par '=='::

  >>> a == b
  True

Mais le lien entre 'a' et 'b' est plus fort que l'égalité
puisqu'ils identifient le même tuple. Pour tester que
2 identifiants référencent le même objet, le mot clé 'is'
est utilisé ::

  >>> a is b
  True

Créons maintenant un nouveau tuple avec les mêmes valeurs ::

  >>> a = ("pycon", 75019)

L'état de l'interpréteur devient :

    Identifiants | Mémoire

      _____________ PyTupleObject(("pycon", 75019))
     /
    b
    a ------------- PyTupleObject(("pycon", 75019))

'a' et 'b' sont encore égaux ::

  >> a == b
  True

En revanche ils n'identifient pas le même objet ::

  >>> a is b
  False


C'est par ce mécanisme d'identifiants que vous pourrez
appliquez en Python les concepts de pointeur ou de référence
appris dans d'autres langages.

1. Affecter trois variables 'a', 'b', 'c' afin d'obtenir ces résultats ::

  >>> a == [3, 7]
  True
  >>> b == a
  True
  >>> b is a
  False
  >>> c is a
  True

Lorsqu'un objet n'a plus de référence pointant sur lui, le ramasse-miette
(garbage collector) le supprime de la mémoire.


Operateurs
----------

Les opérateurs permettent de former des expressions, possédant une valeur.
Une comparaison avec un opérateur de test renvoit un booléen ::

  >>> a = 1.5
  >>> a > 1.2
  True

Il est parfois pratique de souligner que le résultat de la comparaison
renvoit un booléen par des parenthèses ::

  >>> (a > 1.2)
  True

Enfin on peut obtenir le booléen contraire par le mot clé 'not' ::

  >>> not (a > 1.2)
  False


2. Affectez les variables b et c pour obtenir ::

  >>> not (b < 12)
  True
  >>> 1 <= c < 3
  True

Parmi les opérations sur les types numériques (int, long, float, complex)
on trouve l'addition '+', la soustraction '-', la multiplication '*' et
la division '/'.

3. Affectez 'a', 'b' et 'c', 'd' pour obtenir ::

  >>> a + b > 10
  True
  >>> c / d > 1
  True

Les opérateurs '+' et '*' s'appliquent aussi sur les séquences (str, tuple
et list). On peut ainsi concaténer 2 tuples avec l'opérateur d'addition ::

  >>> a = ('pycon', 75019)
  >>> b = ('paris', '31/05/09')
  >>> a + b
  ('pycon', 75019, 'paris', '31/05/09')

Et on peut recopier trois fois le contenu de 'a' dans un nouveau tuple par
l'operateur de multiplication ::

  >>> a * 3
 ('pycon', 75019, 'pycon', 75019, 'pycon', 75019)


4. Utilisez ces propriétés sur le type str pour afficher en utilisant le
caractère '=' au maximum deux fois ::

  ===== Bienvenue =====

5. Voici un extrait de conférences pour le samedi et dimanche de l'édition 2009
avec leur temps en minutes ::

  >>> samedi = [('PyQuery', 20), ('PyQt4', 10)]
  >>> dimanche = [('twisted', 10), ('pyOCC', 20)]

Construisez l'identifiant 'confs' pour obtenir ::

  >>> confs
  [('PyQuery', 20), ('PyQt4', 10), ('twisted', 10), ('pyOCC', 20)]


