#!/usr/bin/env python

import hashlib

# chargement du fichier de mots de passe dans un dictionnaire en memoire
user_passwords = {}
for line in open("13_accounts_md5.txt"):
    line = line.strip()
    if not line:
        continue
    username, md5 = line.split(":")

    user_passwords[username] = md5

# premiere verification: login et login inverse utilise comme mot de passe
for username, md5 in user_passwords.items():
    if hashlib.md5(username).hexdigest() == md5:
        print "%s a pour mot de passe %s"  % (username, username)
        continue

    rev_username = "".join(reversed(username))
    if hashlib.md5(rev_username).hexdigest() == md5:
        print "%s a pour mot de passe %s"  % (username, rev_username)
        continue


# deuxieme verification: utilisation d'un dictionnaire de mots courants
password_users = {}
for u, p in user_passwords.items():
    password_users[p] = u

for line in open("/usr/share/dict/words"):
    word = line.strip()
    if not word:
        continue
    word_md5 = hashlib.md5(word).hexdigest()
    if word_md5 in password_users:
        username = password_users[word_md5]
        print "%s a pour mot de passe %s"  % (username, word)
