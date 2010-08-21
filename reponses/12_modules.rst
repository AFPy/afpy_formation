1.

::

  >>> print [].extend.__doc__
  L.extend(iterable) -- extend list by appending elements from the iterable

2. ::

    #!/usr/bin/env python
    for i in dir({}):
       print i

3. ::

    #!/usr/bin/env python
    for i in os.getgroups():
       print i


4. ::
    #!/usr/bin/env python

    import os
    u = os.uname()
    user = os.getlogin()
    noyau = u[0]
    version = u[2]
    hostname = u[1]
    print "%s a lancé le programme sur un noyau %s en version %s et une machine nommée %s" % (user, noyau, version, hostname) 


   
