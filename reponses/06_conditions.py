#!/usr/bin/env pythoon

import sys

# on ignore le premier element de sys.argv qui est le nom du programme
arguments = sys.argv[1:]

if not arguments:
    print "arguments requis"
elif len(arguments) > 5:
    print "trop d'arguments"
else:
    print arguments
