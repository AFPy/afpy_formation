Exploration des modules
-----------------------

::
    #!/usr/bin/env python
    
    entier = 1
    print dir(entier)
    
    chaine = "plop"
    print dir(chaine)

    print chaine.zfill.__doc__


1. En utilisant la console python, afficher la documentation de la méthode
extend d'une list.

2. Afficher, avec une ligne par méthode, la liste des méthodes d'un 
dictionnaire

:: 
    #!/usr/bin/env python

    import os
    print "%s a pour groupe principal : %s" % (os.geteuid(), os.getgid() )

3. Utiliser une fonction du module os pour afficher tout les groupes du processus, 
avec une boucle. 

::
    #!/usr/bin/env python
    
    import shutils
    shutils.copyfile('/etc/passwd', '/tmp/passwd')


4. En utilisant la variable d'environement $TMP et le module os, copier
le fichier dans $TMP/passwd au lieu de copier dans /tmp/.

::
    #!/usr/bin/env python

    import os
    proc = os.uname()[4]
    print 'Mon systéme tourne sur une architecture de type %s' % proc

5. En utilisant les divers fonctions du module os, affiché la phrase suivante
en complétant les trous : 
"... a lancé le programme sur un noyau ... en version ... et une machine nommé ..."
