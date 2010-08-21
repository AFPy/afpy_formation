Utilisation des fichiers
------------------------

::
    #!/usr/bin/env python 

    nom_fichier = "/etc/passwd"
    fichier = open(nom_fichier)
    for i in fichier.readlines():
        print i

Exercice 10.1. Modifier ce programme pour n'afficher que la ligne de l'utilisateur nobody.
    
Exercice 10.2. En utilisant split, et int, n'afficher que les lignes pour les utilisateurs avec
un uid supérieur à 500 ( l'uid est le troisième champ de la ligne, séparé par : )

Exercice 10.3. Écrire les résultats dans un autre fichier.

Note :  pour ouvrir un fichier en écriture, utilisez open(nom_fichier, 'w') et
utilisez la méthode write.


