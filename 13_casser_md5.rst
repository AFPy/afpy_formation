Exercise pratique d'intrusion
-----------------------------

But: utiliser les fonctions fourni avec python pour tester des mots de passes,
et réussir à vérifier la solidité de son systéme face à un attaquant motivé.
L'exercice va permettre de récapituler les différentes notions vu lors du cours,
les boucles, les fonctions, les fichiers.

Pour ce faire, nous allons supposez que vous avez réussi à mettre la main sur
un fichier de login/mot de passe, au format suivant ::
  
  chef:cbb4581ba3ada1ddef9b431eef2660ce
  souschef:1150615a91d3b19c6824401ac26ae59c
  admin:7321a0a60f5809733b8a12a55bb0845c
  admin2:0ce076e90db9532082d48cf801357478

Pour l'exercise, nous allons utiliser uniquement les 4 comptes donnés ici. Il
faut les recopier dans un fichier, qui va nous servir au cours de l'exercise.

Le format est simple, le login de l'utilisateur, suivi de son mot de passe
encodé en md5. Le md5 est un algorithme permettant de génerer une chaine de
taille fixe, à partir d'une entrée de taille variable, de maniére non reversible.
Ce genre de fonction, dite fonction de hachage, est utilisé notament pour 
vérifier l'intégrité des documents et des téléchargements, car si un seul 
octet change, toute la chaine change. 

Dans notre cas, il permet de stocker les mots de passes sans qu'on puisse les
retrouver facilement. Quand on veut vérifier le mot de passe, on calcule son hash
md5, et on compare avec celui de la base. 

MD5 n'est pas recommendé actuellement, on recommande plutot d'autres fonctions, comme SHA1.
La fonction est publié et détaillé, notament sur Wikipedia_.

.. Wikipedia_:: http://fr.wikipedia.org/wiki/MD5

En python, on utilise le module hashlib pour faire ce genre de calcul::

  >>> import hashlib 
  >>> hashlib.md5('a').hexdigest()
  '0cc175b9c0f1b6a831c399e269772661'

Pour vérifier les mots de passe, nous allons faire 2 vérifications. Tout d'abord, 
il va falloir voir qu'aucun utilisateur n'utilise un mot de passe qui correspond 
à son login, ou son login à l'envers. 

Puis nous allons devoir faire une vérification par rapport à un dictionnaire de mot,
pour voir que le mot de passe n'en fait pas parti.

1. Ecrire un programme qui va lire le fichier de mot de passe, et qui va stocker
les comptes dans un dictionnaire ayant pour clé le login utilisé.

2. Compléter le programme précédent pour faire une boucle sur les logins, calculer la somme
md5 du login, et afficher un message si cela correspond au mot de passe.


La plupart des systémes unix posséde un fichier /usr/share/dict/words, contenant
une liste de mots en anglais. Nous allons nous servir de la liste comme dictionaire
pour essayer de casser les mots de passes.

3. Reprendre le programme de l'exercice 2, et rajouter à la fin une boucle qui va tester 
tout les mots du dictionnaire, et tester tout les mots de passes avant une deuxiéme boucle.

La structure utilisé pour traiter les données n'est pas trés efficace, car cela requiert 
2 boucles. Il est sans doute plus rapide de stocker ça dans le sens inverse, en mettant le
mot de passe comme clé du dictionnaire, et en stockant les logins qui correspondent comme
valeur. Comme ça, un accés direct est possible, ce qui évite de faire une boucle de plus.

4. Recoder le programme de l'exercise 3 en utilisant la structure décrite pour les 
couples login/mot de passe.

