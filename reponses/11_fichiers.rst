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

fichier = open("/etc/passwd")
fichier_out = open("/tmp/nouveau_passwd.txt", 'w')
for ligne in fichier:
    if int(ligne.split(':')[2]) > 500:
        fichier_out.write(ligne)

