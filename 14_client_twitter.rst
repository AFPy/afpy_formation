Programmation d'un petit client twitter
---------------------------------------

But: utiliser la bibliothèque standard de Python pour faire une
petit client HTTP qui affiche le buzz autour de la conférence PyCon
France. Cet excercice va nous permettre faire une requête HTTP et de
parser le contenu du résultat au format XML pour extraire l'auteur et
le contenu de chaque tweet.

twitter.com est un service de micro-blogging ou les utilisateur peuvent
poster des messages de maximum 140 caractères de long. Twitter a
l'avantage de fournir une interface programmatique (API) RESTful_, c'est
a dire qu'il est possible de d'éxecuter des requêtes HTTP de type
GET ou POST en passant des arguments en paramètres de la requête et
en récupérant le résultat dans le corp de la réponse généralement
au format XML ou JSON (liste de dictionnaires javascript).

.. RESTful_:: http://fr.wikipedia.org/wiki/Representational_State_Transfer


Exécuter une requête HTTP
~~~~~~~~~~~~~~~~~~~~~~~~~

En python pour faire une requête HTTP GET le plus simple est d'importer
le module ``urllib2`` de Python 2.5 / 2.6 (en Python 3.x ce module est
renommé urllib.request)::

  >>> import urllib2
  >>> help(urllib2)

  >>> f = urllib2.urlopen('http://www.afpy.org/')
  >>> print f.read()
  ...

La variable ``f`` se comporte comme une instance de ``file`` sauf que
le contenu est lu via une connexion réseau HTTP au lieu d'un accès au
disque dur. Ici le résultat affiché par ``print`` est le contenu du
code source HTML de la page d'accueil du site de l'AFPy.

L'API de recherche de twitter est décrite sur cette page::

  http://apiwiki.twitter.com/Twitter-Search-API-Method%3A-search

En particulier il est possible de faire une recherche sur le mot clef
'python' en tappant l'url suivante dans un navigateur::

  http://search.twitter.com/search.atom?q=python

Le résultat est rendu au format XML 'Atom' qui permet d'enregister
le flux de résultats dans un lecteur de flux comme Google Reader par
exemple.

Il est aussi possible d'obtenir les même resultats dans au format
JSON::

  http://search.twitter.com/search.json?q=python


Exercices HTTP
~~~~~~~~~~~~~~

Exercice 14.1: Écrire un programme qui recupère une connexion sur la
page de résultats de la recherche sur un mot clef saisi par l'utilisateur
et qui affiche le contenu XML brut de la réponse du serveur. Tester le
programme avec le mot clef 'pycon-fr'.

Exercice 14.2: Modifier le programme précendent pour faire 2 print
sucessifs sur le même résultat de recherche (c'est à dire le résultat
du même appel à la fonction ``urlopen``). Expliquer le comportement
observé.


Parser un contenu XML
~~~~~~~~~~~~~~~~~~~~~

Le contenu XML obtenu est illisible pour un humain normalement
constitué. Nous allons maintenant tenter d'extraire les informations qui
nous intéressent pour afficher juste le nom de l'auteur et le contenu
textuel de chaque résultat. Pour cela nous allons 'parser' le contenu XML
avec le module ``xml.etree.cElementTree`` de la bibliothèque standard.

Pour parser une chaine de caractères contenant un arbre XML il suffit de
tapper les instruction suivantes dans un terminal::

  >>> import xml.etree.cElementTree as etree
  >>> chaine_xml = '<a><b attribut="valeur">Contenu de b</b><c><b/></c></a>'

  >>> racine = etree.fromstring(chaine_xml)
  >>> racine.tag
  'a'
  >>> fils_de_a = racine.getchildren()
  >>> fils_de_a
  [<Element 'b' at 0x...>, <Element 'c' at 0x...>]

  >>> b = fils_de_a[0]
  >>> b.keys()
  ['attribut']
  >>> b.get('attribut')
  'valeur'

Il est aussi possible de trouver tous les éléments de l'arbre de tag ``b``
en faisant un requète de type XPATH avec ``findall`` au niveau de la
racine::

  TODO

Enfin il est possible de parser le XML contenu dans un objet python qui se
comporte comme un ``file`` (ce qui est le cas de l'objet retourné par
``urlopen``)::

  >>> f = urllib2.urlopen('http://search.twitter.com/search.atom?q=python')
  >>> arbre = etree.parse(f)
  >>> arbre
  <__builtin__.ElementTree instance at 0x...>

A noter dans ce cas on obtient un objet ``ElementTree`` au lieu de la
racine de type ``Element``. Pour obtenir la nouvelle racine il suffit de
faire::

  >>> racine_2 = arbre.getroot()
  >>> racine_2.tag
  '{http://www.w3.org/2005/Atom}feed'

Dans ce cas on peut noter que le nom du tag contient aussi un "namespace" XML
qu'il ne fait pas oublier lors de traitements.


Exercices XML
~~~~~~~~~~~~~

Exercice 14.3: Modifier le programme du 14.1 pour parser le XML obtenu et
afficher tous les objets dont le tag est ``{http://www.w3.org/2005/Atom}entry``.

Exercice 14.4: Modifier le programme précédent pour faire un programme qui
demande un mot clef à l'utilisateur, fait la recherche sur twitter et
retourne la liste des noms des auteur et le contenu du message posté.


Pour aller plus loin
~~~~~~~~~~~~~~~~~~~~

- quand on passe des paramètres après le '?' d'une requête GET il
  faut prendre en compte certains caractères spéciaux ('/' s'écrit
  '%2F' par exemple). La fonction ``urlencode`` du module ``urllib``
  (sans le 2 final) permet de s'assurer que tous les paramètres sont
  encodés correctement::

    http://docs.python.org/library/urllib.html#urllib.urlencode

  Exercice complémentaire: reprendre le programme précédent pour
  prendre en compte la gestion de l'URL encoding des paramètres.

- certaines méthodes de l'API REST de twitter nécessitent une
  authentification HTTP Basic avec un login / mot de passe. La
  documentation en ligne du module ``urllib2`` montre comment charger
  un ``handler`` dédié à ce mode d'authentifications.

- le module xml.etree de la lib standard de python est un peu limité
  notamment concernant le support de XPATH. Il existe une alternative
  plus complète disponible en module d'extension::

    http://codespeak.net/lxml/

  ``lxml`` fournit notamment un parser spécial pour les pages HTML
  malformées qui corrige les tags mal fermés par exemple de manière
  à obtenir un ``ElementTree`` similaire à celui d'une page XHTML
  équivalente valide.

- ``pyquery`` est un autre module basé sur ``lxml`` pour manipuler
  des documents XML de manière très similaire au projet javascript
  ``jquery`` mais en restant en python::

    http://pypi.python.org/pypi/pyquery

  La documentation en ligne présente des cas d'utilisation qui
  mettent en évidence la simplicité d'utilisation de cette API.

