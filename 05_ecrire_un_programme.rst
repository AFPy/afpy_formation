Écrire un programme
-------------------

L'interpréteur interactif est très pratique pour tester rapidement
de nouvelles idées mais il ne permet pas de réutiliser facilement
des bouts de scripts.

Pour développer des scripts ou applications complètes en Python il suffit
d'utiliser un éditeur de texte (comme vim, emacs, gedit ou mate par
exemple) ou un environnement de développement plus complet tel eclipse
(et son plugin pydev) et d'écrire les instructions dans un fichier qui
dont le nom se termine  par '.py'.

L'exécution d'un programme Python se fait en cliquant sur le fichier
'.py' sous windows ou en lancant la commande suivante sous unix::

  $ python mon_programme.py

Exercice 5.1: Créer un nouveau fichier avec les lignes suivantes (sans
les 2 espaces en débuts de chaque ligne)::

  import sys

  # ceci est un commentaire et n'est pas execute
  print "voici la liste des arguments du programme:"
  print sys.argv

La première ligne est un import du module "sys" qui permet d'accéder
à un certain nombre de paramètres systèmes comme par exemple les
arguments passés en ligne de commande au lancement d'un programme.

Enregistrer le fichier avec le nom "exercice_5_1.py" et l'executer en
tappant dans un terminal::

  $ python exercice_5_1.py

Puis::

  $ python exercice_5_1.py argument_1 deux 3

Il est possible de rendre un programme Python automatiquement exécutable (comme
un script shell) en ajoutant la ligne suivante en première ligne::

  #!/usr/bin/env python

Puis en changeant la permission d'exécution du fichier::

  $ chmod u+x mon_programme.py
  $ ./mon_programme.py

Exercice 5.2: Copier le programme précédent en un nouveau
fichier nommé "exercice_5_2" et le rendre exécutable.

