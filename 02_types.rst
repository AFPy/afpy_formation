Présentation des types de base
------------------------------

Connaître le type d'une variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le type d'un identifiant est défini au moment de sa création par une
analyse de l'interpréteur. Vous pouvez ensuite connaître le type d'un
identifiant 'idt' par l'appel: 'type(idt)'.

1. Demandez les types des identifiants 'val' et 'mess'
   créés au point 2 de l'introduction.


Mutables / non mutables
~~~~~~~~~~~~~~~~~~~~~~~

Les types de Python peuvent être classés en 2 catégories:
les non-mutables et les mutables. Par définition un type
est mutable s'il possède des méthodes permettant de modifier
son contenu. Les types de base non-mutables sont:

    - les types numériques (int, long, float, complex)
    - les booléens (bool)
    - les chaînes de caractères (str, unicode)
    - les 'tuple' ou (n-uplets) (tuple)

Les types de base mutables sont:

    - les listes ou listes chaînées (list)
    - les dictionnaires ou tables de hachage (dict)
    - les ensembles (set)


2. Tapez dans l'interpréteur les lignes suivantes
et vérifiez que le type change après chaque création de 'a'::

  >>> a = 1
  >>> a = 2 ** 31
  >>> a = 1.
  >>> a = True
  >>> a = 'Bonjour'
  >>> a = u'Bonjour'
  >>> a = ('Pycon', 75019)
  >>> a = ['misc', 'ogrisel', 'dede']
  >>> a = {'lang': 'Python', 'type': 'dynamic'}


Séquences
~~~~~~~~~

Les séquences sont des suites d'éléments indexées par
des entiers. Les types de base concernés sont:

    - les chaînes de caractères
    - les tuples
    - les listes

On accède à l'élement numéro i de la séquence
'seq' avec 'seq[i]'. La numérotation commence à zéro. Il est
possible de récupérer le dernier élément par 'seq[-1]'. Enfin
on peut demander une tranche de 'i' à 'j-1' par 'seq[i:j]'.

Exemple ::

  >>> a = ('Pycon', 75019, 'Paris', '30/05/09')
  >>> a[0]
  'Pycon'
  >>> a[-1]
  '30/05/09'
  >>> a[0:3]
  ('Pycon', 75019, 'Paris')

3. Créez la chaîne ::

  >>> mess = "Bienvenue à Pycon"
  puis essayez d'obtenir les résultats suivants:
  'B'
  'Bienvenue'
  'con' # ceux qui sont à l'aise peuvent essayer de le faire
            avec des indices négatifs

La méthode permettant de placer un identifiant 'a' à la position
'i' de la séquence  'seq' se fait par : 'seq[i] = a'. Le seul type
concerné à ce niveau du cours est 'list'.

Exemple ::

  >>> persons = ['misc', 'ogrisel', 'dede']
  >>> persons[-1] = 'DD'
  >>> persons
  ['misc', 'ogrisel', 'DD']

4. Créez la liste ::

  >>> lst = [('Gar', 34), ('Her', 30)]

puis modifiez-la pour obtenir ::

  [('Gard', 30), ('Herault', 34)]

5. Créez le tuple ::

  >>> dpt = ('Gar', 30)

Peut-on modifier le premier élement de 'dpt' en 'Gard'?


Dictionnaires
~~~~~~~~~~~~~

Les dictionnaires permettent l'assocation d'une clé avec un élément.  Pour un
dictionnaire 'dico', vous pouvez accéder à l'élément de la clé 'k' par
'dico[k]'. L'affectation de 'elt' à la clé 'k', se fait par 'dico[k] = elt'.

Exemple ::

  >>> env = {'PATH' : '/usr/bin', 'CPPPATH' : '/include'}
  >>> env['PATH']
  '/usr/bin'
  >>> env['CPPPATH'] = '/usr/include'
  >>> env
  {'PATH': '/usr/bin', 'CPPPATH': '/usr/include'}

