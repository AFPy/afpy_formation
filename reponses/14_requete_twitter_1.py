#!/usr/bin/env python

import urllib2

# demande de saisie du mot clef a l'utilisateur
mot_clef = raw_input('Tapper le mot clef: ')

# construction de l'URL de la requete HTTP
requete = 'http://search.twitter.com/search.json?q=' + mot_clef

# execution de la requete HTTP
f = urllib.urlopen(requete)

# affichage du XML resultat
print f.read()
