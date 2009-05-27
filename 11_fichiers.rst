Utilisation des fichiers
------------------------

::
    #!/usr/bin/env python 

    nom_fichier = "/etc/passwd"
    fichier = open(nom_fichier)
    for i in fichier.readlines()
        print i

1. Faire en sorte de ne pas afficher les lignes, sauf pour l'utilisateur nobody.
    
2. En utilisant split, et int, n'afficher que les lignes pour les utilisateurs avec
un uid supérieur à 500 ( l'uid est le troisiéme champ de la ligne, séparé par : )

::
    #!/usr/bin/env python 

    nom_fichier_lecture = "/etc/passwd"
    nom_fichier_2 = "/tmp/passwd"

    fichier_lecture = open(nom_fichier_1)
    fichier_ecriture = open(nom_fichier_2, 'w')

    for i in fichier.readlines()
        fichier_ecriture.write(i)

    fichier_ecriture.write('toto:x:1234:1234:User toto:/var/lib/empty:/sbin/nologin')


3. Avec l'aide d'un compteur, ajouter la ligne avec l'utilisateur toto en 5eme position.

4. Ajouter la ligne avec l'utilisateur toto aprés le premier des utilisateurs 
'adm' ou 'operator'.

5. Ecrire les 10 premiers nombres pairs un fichier dans /tmp/. 

6. Ecrire à la suite du fichier précedent les 10 premiers nombres impairs, sans
écraser le contenu du fichier. Le mode 'a' ( comme append ) n'écrase pas le fichier.
