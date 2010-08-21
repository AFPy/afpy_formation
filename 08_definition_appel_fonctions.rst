Définitions et appels de fonctions
----------------------------------

Une fonction se définit grace au mot clef 'def' et un bloc indenté::

  >>> def ma_fonction(a, b):
  ...     if b != 0:
  ...         return a / b
  ...     return a
  ...
  >>> ma_fonction(1.0, 2.0)
  0.5
  >>> ma_fonction(1.0, 0.0)
  1.0

Exercice 8: Écrire une fonction "jaimepas" qui prend une liste en paramètre et
qui se comporte comme dans le programme 07_boucle_2.py. Appeler cette fonction
pour la liste des 5 jours travaillés de la semaine.
