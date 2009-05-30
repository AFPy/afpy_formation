Tests de conditions (if elif else)
----------------------------------

En python les tests de conditionels utilise la structure suivante
(attention aux deux points et à l'indentation)::

  >>> la_reponse = 6 * 7
  >>>
  >>> if la_reponse == 42:
  ...     print "la vie, l'univers et tout le reste"
  ... elif la_reponse > 40 and la_reponse < 44:
  ...     print "c'est pas tout a fait la bonne reponse"
  ... else:
  ...     print "c'est pas du tout la bonne reponse"
  la vie, l'univers et tout le reste

Les conditions après un if ou un elif sont l'évaluation bouléenne d'une
expression python. Les expressions python suivante sont équivalente au booléen
False:

  - le nombre entier zero: 0
  - le nombre flottant zero: 0.0
  - la liste vide: []
  - le tuple vide: ()
  - le dictionnaire vide: {}
  - la chaine de caractères vide: ""

Exercice 6: écrire un programme qui:
  - affiche "arguments requis" si aucun argument n'est passé en ligne de
    commande
  - affiche "trop d'arguments" si il y a plus de 5 arguments
  - affiche la liste des arguments dans les autres cas
