#!/usr/bin/env python

import urllib2

# demande de saisie du mot clef a l'utilisateur
mot_clef = raw_input('Tapper le mot clef: ')

# construction de l'URL de la requete HTTP
requete = 'http://search.twitter.com/search.json?q=' + mot_clef

# execution de la requete HTTP
f = urllib2.urlopen(requete)

# affichage du XML resultat
print "Premier affichage du XML resultant:"
print f.read()

# affichage du XML resultat
print "Second affichage du XML resultant:"
print f.read()

# ce deuxieme appel n'affiche plus rien car le buffer contenant le resultat a
# ete vide lors du premier affichage: La solution est de stocker le resultat
# dans une variable et d'afficher deux fois le contenu de la variable

# execution de la requete HTTP
f = urllib2.urlopen(requete)

# recuperation du XML dans une chaine de caracteres
chaine_xml = f.read()

# affichage du XML resultat
print "Premier affichage du XML de la variable:"
print chaine_xml

print "Second affichage du XML de la variable:"
print chaine_xml



