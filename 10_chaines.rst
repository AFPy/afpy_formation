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
    print ma_chaine.split()


Écrire un programme qui récupère le texte d'Alice au Pays des Merveilles, et
afficher les 5 mots les plus fréquents, indépendemment de leur casse, ainsi que
leurs occurrences respectives.


Note : pour télécharger le texte, utilisez ::

  >>> import urllib2
  >>> texte = urllib2.urlopen("http://www.gutenberg.org/files/11/11.txt").read()
  >>> print texte[:70]
  Project Gutenberg's Alice's Adventures in Wonderland, by Lewis Carroll
