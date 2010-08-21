Exercise pratique d'intrusion
-----------------------------

But: utiliser les fonctions fournies avec Python pour tester des mots de passe,
et réussir à vérifier la solidité de son système face à un attaquant motivé.
L'exercice va permettre de récapituler les différentes notions vues lors du cours,
les boucles, les fonctions, les fichiers.

Pour ce faire, nous allons supposer que vous avez réussi à mettre la main sur
un fichier de login/mot de passe, au format suivant ::
  
  chef:cbb4581ba3ada1ddef9b431eef2660ce
  souschef:1150615a91d3b19c6824401ac26ae59c
  admin:7321a0a60f5809733b8a12a55bb0845c
  admin2:0ce076e90db9532082d48cf801357478

Pour l'exercice, nous allons utiliser uniquement les 4 comptes donnés ici. Il
faut les recopier dans un fichier, qui va nous servir au cours de l'exercice.

Le format est simple, le login de l'utilisateur, suivi de son mot de passe
encodé en md5. Le md5 est un algorithme permettant de génerer une chaîne de
taille fixe, à partir d'une entrée de taille variable, de manière non reversible.
Ces fonctions, dites fonctions de hachage, sont utilisées notament pour 
vérifier l'intégrité des documents et des téléchargements, car si un seul 
bit change, toute la chaîne change. 

Dans notre cas, il permet de stocker les mots de passe sans qu'on puisse les
retrouver facilement. Quand on veut vérifier le mot de passe, on calcule son hash
md5, et on compare avec celui de la base. 

MD5 n'est pas recommandé actuellement, on recommande plutot d'autres fonctions,
comme SHA1.  La fonction est publiée et détaillée, notament sur Wikipedia_.

.. Wikipedia_:: http://fr.wikipedia.org/wiki/MD5

En Python, on utilise le module hashlib pour faire ce genre de calcul::

  >>> import hashlib 
  >>> hashlib.md5('a').hexdigest()
  '0cc175b9c0f1b6a831c399e269772661'

Pour vérifier les mots de passe, nous allons faire 2 vérifications. Tout d'abord, 
il va falloir vérifier qu'aucun utilisateur n'utilise un mot de passe qui correspond 
à son login, ou son login à l'envers. 

Puis nous allons devoir faire une vérification par rapport à un dictionnaire de
mots, pour vérifier que le mot de passe n'en fait pas partie.

1. Écrire un programme qui lit le fichier de mot de passe, et qui stocke
les comptes dans un dictionnaire ayant pour clé le login utilisé.

2. Compléter le programme précédent pour faire une boucle sur les logins, calculer la somme
md5 du login, et afficher un message si cela correspond au mot de passe.


La plupart des systèmes UNIX posséde un fichier /usr/share/dict/words, contenant
une liste de mots courants en anglais. Nous allons nous servir de la liste comme dictionaire
pour essayer de casser les mots de passe.

3. Reprendre le programme de l'exercice 2, et rajouter à la fin une boucle qui va tester 
tout les mots du dictionnaire, et tester tout les mots de passe avant une deuxième boucle.

La structure utilisée pour traiter les données n'est pas très efficace, car cela requiert 
2 boucles. Il est sans doute plus rapide de stocker ça dans le sens inverse, en mettant le
mot de passe comme clé du dictionnaire, et en stockant les logins qui correspondent comme
valeur. Ainsi, un accès direct est possible, ce qui évite de faire une boucle
supplémentaire.

4. Réécrire le programme de l'exercice 3 en utilisant la structure décrite pour les 
couples login/mot de passe.

