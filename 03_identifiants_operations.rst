Fonctionnement des identifiants
-------------------------------

Vous avez peut-être remarqué que le mot variable
n'a pas été utilisé jusqu'à maintenant, son remplaçant
a été identifiant. De la même manière, il a été dit
que l'opération 'a=1' crée l'identifiant 'a' de type
entier et non que l'entier 1 est affecté à la variable
'a'. Vous pourrez bien sûr utiliser ce vocabulaire
en Python mais une fois que vous aurez compris
la réponse à la question: pourquoi parle-t-on d'identifiant
et non de variable?

Toute la réponse est contenu dans l'interpréteur, écrit en C,
qui comme son nom l'indique interpréte chaque ligne que
vous lui donnez. Ainsi lorsque vous tapez:

>>> a = 1
>>> b = 2

Voici ce qui se passe en mémoire, PyIntObject étant le
type entier de Python:

    Identifiants | Mémoire
    a ------------> PyIntObject(1)
    b ------------> PyIntObject(2)

Maintenant passons 'a' à 3:

>>> a = 3

Voici le status de l'interpréteur juste après votre ligne:

    Identifiants | Mémoire
                    PyIntObject(1)
    b ------------> PyIntObject(2)
    a ------------> PyIntObject(3)

Ainsi Python a laissé tomber le premier entier qui valait
1 pour en créer un nouveau avec la valeur 3 correspondant
à l'identifiant 'a'. Donc 'a' n'est pas une variable de type
entier dans laquelle on va affecter 1 puis 3.

Continuons la découverte du fonctionnement avec un tuple:

>>> a = ("pycon", 75019)
>>> b = a

Voici le status de l'interpréteur:

    Identifiants | Mémoire
    a
     \_____________
      _____________ PyTupleObject(("pycon", 75019))
     /
    b

'a' et 'b' sont donc égaux, on peut tester l'égalité
entre 2 identifiants par '==':

>>> a == b
True

Mais le lien entre 'a' et 'b' est plus fort que l'égalité
puisqu'ils identifient le même tuple. Pour tester que
2 identifiants référencent le même objet, le mot clé 'is'
est utilisé:

>>> a is b
True

Créeons maintenant un nouveau tuple avec les mêmes valeurs:

>>> a = ("pycon", 75019)

Le status de l'interpréteur devient:

    Identifiants | Mémoire

      _____________ PyTupleObject(("pycon", 75019))
     /
    b
    a ------------- PyTupleObject(("pycon", 75019))

'a' et 'b' sont-ils encore égaux?

>> a == b
True

En revanche identifient-t'ils le même objet?

>>> a is b
False

C'est par ce mécanisme d'identifiants que vous pourrez
appliquez en Python les concepts de pointeur ou de référence
appris dans d'autres langages.

1. Trouver les 3 identifiants suivants:

>>> a = 0
>>> b = 0
>>> c = 0

afin d'obtenir les résultats:

>>> a == [3, 7]
True
>>> b == a
True
>>> b is a
False
>>> c is a
True

Enfin que deviennent les objets perdant tous leurs identifiants,
comme le PyIntObject(1) délaissé plus haut? Ils sont collectés pas
le ramasse-miette (ou garbage collector) qui va soit rendre la mémoire
au système, soit la conserver pour une future utilisation.

Operateurs
----------

L'opérateur d'égalité a déjà été présenté par '=='. Les opérateurs
restants  sont l'infériorité '<', l'infériorité ou l'égalité
'<=', la supériorité ou l'égalité '>=', la supériorité '>' et la
différence '!='.
Une comparaison avec un opérateur de test renvoit un booléen:

>>> a = 1.5
>>> a > 1.2
True

Il est parfois pratique de souligner que le résultat de la comparaison
renvoit un booléen par des parenthèses:

>>> (a > 1.2)
True

Enfin on peut obtenir le booléen contraire par le mot clé 'not':

>>> not (a > 1.2)
False


2. Modifiez les identifiants 'b' et 'c':

>>> b = 0
>>> c = 0

pour obtenir

>>> not (b < 12)
True
>>> 1 <= c < 3
True

Les opérations sur les types numériques (int, long, float, complex)
sont l'addition '+', la soustraction '-', la multiplication '*' et
la division '/'.

3. Modifiez 'a', 'b' et 'num', 'dem':

>>> a = 0
>>> b = 0
>>> num = 0
>>> dem = 0

tel que:

>>> a + b > 10
True
>>> num/dem > 1
True

Les opérateurs '+' et '*' s'appliquent aussi sur les séquences (str, tuple
et list). On peut ainsi concaténer 2 tuple par l'opérateur d'addition:

>>> a = ('pycon', 75019)
>>> b = ('paris', '31/05/09')
>>> a + b
('pycon', 75019, 'paris', '31/05/09')

Et on peut recopier trois fois le contenu de 'a' dans un nouveau tuple par
l'operateur de multiplication:

>>> a * 3
('pycon', 75019, 'pycon', 75019, 'pycon', 75019)


4. Découvrez ces propriétés sur le type str pour affficher:

===== Bienvenu =====

5. Voici un extrait de conférences pour le samedi et dimanche avec leur
   temps en minutes:

>>> samedi = [('PyQuery', 20), ('PyQt4', 10)]
>>> dimanche = [('twisted', 10), ('pyOCC', 20)]

   Construisez l'identifiant 'confs' pour obtenir:

>>> confs
[('PyQuery', 20), ('PyQt4', 10), ('twisted', 10), ('pyOCC', 20)]


