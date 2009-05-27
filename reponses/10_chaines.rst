1.

::
    #!/usr/bin/env python 
    ma_chaine = raw_input("Entrez votre nom : ")
    if len(ma_chaine) <= 4:
        print 'Votre nom est trop court' 
    else:
        print 'Bonjour ' + ma_chaine 
  

2.

::
    #!/usr/bin/env python 
    ma_chaine = raw_input("Entrez une chaine : ")
    if ma_chaine.endswith('bonjour'):
        m = ma_chaine[:-4] 
        ma_chaine = m + 'soir'
    print ma_chaine 

3.

::
    #!/usr/bin/env python 
    nom = raw_input("Entrez votre nom : ")
    print "Bonjour " + nom.title()
   
4.

::
    #!/usr/bin/env python 

    ma_chaine = "bonjour utilisateur"
    print ma_chaine.split()

    ma_chaine = raw_input("> ")
    ma_chaine = ma_chaine.lower()
    for i in ma_chaine.split():
        if i == 'bonjour':
            print "Oui, bonjour encore"

5.

::
    #!/usr/bin/env python 

    ma_chaine = "bonjour utilisateur"
    print ma_chaine

    ma_chaine = raw_input("> ")
    ma_chaine = ma_chaine.lower()
    if ma_chaine.startswith('Bonjour '):
        print "Oui, bonjour encore"


6.

::
    #!/usr/bin/env python 

    ma_chaine = "bonjour utilisateur"
    print ma_chaine

    ma_chaine = raw_input("> ")
    for i in ma_chaine.split():
        if i in('bonjour', 'salut', 'bonsoir'):
            print "Oui, bonjour encore"

7.

:: 
    #!/usr/bin/env python 
    
    chaine = raw_input("Entrez une chaine : ")
    nombre = raw_input("Entrez un nombre : ")
    n = int(nombre)
    if n > 0 and n <= 100:
        for i in range(int(nombre)):
            print chaine

8.

:: 
    #!/usr/bin/env python 
    
    chaine = raw_input("Entrez une chaine : ")
    nombre = raw_input("Entrez un nombre : ")
    if nombre.isdigit():
        n = int(nombre)
        if n > 0 and n <= 100:
            for i in range(int(nombre)):
                print chaine


