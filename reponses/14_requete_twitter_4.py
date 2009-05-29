#!/usr/bin/env python

import urllib2
import xml.etree.cElementTree as etree

# definition d'une constante qui contient le tag recherche
ATOM_NAMESPACE = "{http://www.w3.org/2005/Atom}"
ENTRY_TAG = ATOM_NAMESPACE + "entry"
AUTHOR_NAME_TAG = ATOM_NAMESPACE + "author" + "/" + ATOM_NAMESPACE + "name"
CONTENT_TAG = ATOM_NAMESPACE + "content"

# demande de saisie du mot clef a l'utilisateur
mot_clef = raw_input('Tapper le mot clef: ')

# construction de l'URL de la requete HTTP
requete = 'http://search.twitter.com/search.atom?q=' + mot_clef

# execution de la requete HTTP
f = urllib2.urlopen(requete)

# parsing du XML contenu dans la reponse de la requete
arbre = etree.parse(f)
for entry in arbre.findall(ENTRY_TAG):
    print entry.find(AUTHOR_NAME_TAG).text, ":",
    print entry.find(CONTENT_TAG).text

