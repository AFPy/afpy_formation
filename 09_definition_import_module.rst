Les modules
-----------

Dès qu'un programme en Python devient grand, il est nécessaire de le découper en
plusieurs fichiers appelés modules. Les modules qui se trouvent dans le
répertoire courant ou dans les répertoires désignés par la variable
d'environnement PYTHONPATH peuvent être importés dans le programme courant.

Supposons que mon_module.py comporte les lignes suivantes::

  #!/usr/bin/env python

  def fonction_1(a, b):
      return a + b

  def fonction_2(a, b):
      return a - b

Dans un shell Python (ou un programme) lancé dans le même répertoire il est
ainsi possible de faire::

  >>> import mon_module
  >>> mon_module.fonction_1(1, 2)
  3

Ou plus directement::

  >>> from mon_module import fonction_2
  >>> fonction_2(1, 2)
  -1

Exercice 9: écrire un nouveau programme qui importe le module défini
par le programme 08_fonction.py (en le renommant mon_module.py car un nom
de module ne peut pas commencer par un chiffre) et appelle la fonction
jaimepas pour les chiffres de 0 a 9.

Expliquez pourquoi les jours de la semaine sont haïs en priorité. Trouver
un moyen d'éviter cet effet de bord indésirable (en demandant à l'un
des animateurs de la session).

