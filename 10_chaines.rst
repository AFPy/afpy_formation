Programmation des chaînes
-------------------------

Les chaînes de caractères sont des objets possédant des méthodes permettant
d'agir sur elles. Voici quelques exemples ::

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

Exercice 10.1. Remplacer les 4 dernières lettres d'une chaîne entrée par l'utilisateur par
les lettres soir, si la chaine se termine par bonjour.

Exercice 10.2. Demander le nom d'un utilisateur, et lui dire bonjour avec une majuscule à son nom

::
    #!/usr/bin/env python

    ma_chaine = "bonjour utilisateur"
    print ma_chaine.split()
    print ma_chaine

    ma_chaine = raw_input("> ")
    for i in ma_chaine.split():
        if i == 'bonjour':
            print "Oui, bonjour encore"

Exercice 10.3. Corriger le programme suivant pour qu'il ne tienne pas
compte de la casse des mots

Exercice 10.4. Corriger le programme pour qu'il ne réponde bonjour que
si c'est le premier mot, avec une majuscule.

Exercice 10.5. Corriger le programme pour également utiliser
"salut" et "bonsoir" ( indice : utiliser l'instruction in )



::
    #!/usr/bin/env python

    chaine = raw_input("Entrez une chaine : ")
    nombre = raw_input("Entrez un nombre : ")
    for i in range(int(nombre)):
        print chaine

Exercice 10.6. Corriger le programme pour vérifier que le nombre n'est pas
négatif, ou trop grand ( supérieur à 100 ).

Exercice 10.7. Corriger le programme pour voir si on rentre autre chose qu'un
entier ( indice : utiliser la méthode isdigit )


