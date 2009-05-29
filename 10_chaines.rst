Programmation des chaines
-------------------------

::
    #!/usr/bin/env python

    ma_chaine = "bonjour"
    print ma_chaine

    mon_autre_chaine = ma_chaine
    # une copie de la chaine est rapide
    print id(ma_chaine)
    print id(mon_autre_chaine)

    ma_chaine = "monde"
    print id(ma_chaine)
    print id(mon_autre_chaine)

    print ma_chaine
    print len(ma_chaine)

    mon_autre_chaine = raw_input("Entrez votre nom : ")
    print ma_chaine + ' ' + mon_autre_chaine


1.  Saluer l'utilisateur si son nom fait plus de 4 caractéres, et lui faire
une remarque si c'est pas le cas.


::

    #!/usr/bin/env python

    ma_chaine = "bonjour"
    print ma_chaine[:3]

    # ceci ne marche pas
    # ma_chaine[:3] = 'ert'

    if ma_chaine.startswith('bon'):
        print "la chaine commence par bon"

    if ma_chaine.endswith('jour'):
        print "La chaine fini par jour"

    print ma_chaine.title()
    print ma_chaine.upper()
    print ma_chaine.lower()

2. Remplacer les 4 derniers lettres d'une chaine entrée par l'utilisateur par
les lettres soir, si la chaine se termine par bonjour.

3. Demander le nom d'un utilisateur, et lui dire bonjour avec une majuscule à son nom

::
    #!/usr/bin/env python

    ma_chaine = "bonjour utilisateur"
    print ma_chaine.split()
    print ma_chaine

    ma_chaine = raw_input("> ")
    for i in ma_chaine.split():
        if i == 'bonjour':
            print "Oui, bonjour encore"

4. Corriger le programme suivant pour qu'il ne tienne pas
compte de la casse des mots

5. Corriger le programme pour qu'il ne réponde bonjour que
si c'est le premier mot, avec une majuscule.

6. Corriger le programme pour également utiliser
"salut" et "bonsoir" ( indice : utiliser l'instruction in )



::
    #!/usr/bin/env python

    chaine = raw_input("Entrez une chaine : ")
    nombre = raw_input("Entrez un nombre : ")
    for i in range(int(nombre)):
        print chaine

7. Corriger le programme pour vérifier que le nombre n'est pas
négatif, ou trop grand ( supérieur à 100 ).

8. Corriger le programme pour voir si on rentre autre chose qu'un
entier ( indice : utiliser la méthode isdigit )


