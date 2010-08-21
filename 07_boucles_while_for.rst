Les boucles
-----------

En python il n'y a que deux manières classiques de répéter plusieurs fois l'exécution
d'un groupe de lignes : les boucles 'while' et 'for'.

La boucle 'while' permet de répeter un bloc tant qu'une expression est vraie ::

  >>> i = 1
  >>> while i <= 1024:
  ...     print i
  ...     i *= 2
  1
  2
  4
  8
  16
  32
  64
  128
  256
  512
  1024

Exercice 7.1: Ecrire un programme qui boucle a l'infini en écrivant:
"All work and no play makes Jack a dull boy" (faire un ctrl-C pour l'arrêter).

La deuxième manière est de parcourir une collection itérable d'éléments (liste,
tuple, chaîne, dictionnaire)::

  >>> jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']
  >>> for jour in jours:
  ...      print 'il faut travailler le ' + jour
  ...
  il faut travailler le lundi
  il faut travailler le mardi
  il faut travailler le mercredi
  il faut travailler le jeudi
  il faut travailler le vendredi

  >>> mon_dico = {0: 'zero', 1: 'un', 2: 'deux'}
  >>> for clef, valeur in mon_dico.items():
  ...      if clef % 2 == 0:
  ...          print valeur, 'est divisible par deux'
  ...

Exercice 7.2: Écrire un programme qui affiche 'j'aime pas les ' + chaque mot passé
en arguments de la ligne de commande.


