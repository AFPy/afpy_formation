1.

::
    #!/usr/bin/env python 

    nom_fichier = "/etc/passwd"
    fichier = open(nom_fichier)
    for i in fichier.readlines():
        if i.startswith('nobody:'):
            print i

2.

::
    #!/usr/bin/env python 

    nom_fichier = "/etc/passwd"
    fichier = open(nom_fichier)
    for i in fichier.readlines():
        if int(i.split(':')[2]) > 500:
            print i

3.

::
    #!/usr/bin/env python 

    nom_fichier_lecture = "/etc/passwd"
    nom_fichier_2 = "/tmp/passwd"

    fichier_lecture = open(nom_fichier_1)
    fichier_ecriture = open(nom_fichier_2, 'w')

    compteur = 1
    for i in fichier.readlines()
        fichier_ecriture.write(i)
        compteur = compteur + 1
        if compteur = 5:
            fichier_ecriture.write('toto:x:1234:1234:User toto:/var/lib/empty:/sbin/nologin')


4.

::
    #!/usr/bin/env python 

    nom_fichier_lecture = "/etc/passwd"
    nom_fichier_2 = "/tmp/passwd"

    fichier_lecture = open(nom_fichier_1)
    fichier_ecriture = open(nom_fichier_2, 'w')

    deja_ecrit = False
    for i in fichier.readlines()
        fichier_ecriture.write(i)
        if i.split(':') in ('adm', 'operator') and not deja_ecrit:
            fichier_ecriture.write('toto:x:1234:1234:User toto:/var/lib/empty:/sbin/nologin')
            deja_ecrit = True


5.
::
    #!/usr/bin/env python 

    nom_fichier = "/tmp/nombre"

    fichier_ecriture = open(nom_fichier, 'w')
    for i in xrange(0,20,2):
        fichier_ecriture.write("%s\n" % i)



6.
::
    #!/usr/bin/env python 

    nom_fichier = "/tmp/nombre"

    fichier_ecriture = open(nom_fichier, 'a')
    for i in xrange(1,21,2):
        fichier_ecriture.write("%s\n" % i)


