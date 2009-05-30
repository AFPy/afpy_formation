#!/usr/bin/env pythoon

import sys

# on ignore le premier element de sys.argv qui est le nom du programme
arguments = sys.argv[1:]

for mot in arguments:
    print "J'aime pas les", mot
