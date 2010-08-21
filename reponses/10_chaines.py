import urllib2
texte = urllib2.urlopen("http://www.gutenberg.org/files/11/11.txt").read()

words = texte.lower().split()
occurrences = {}
for word in words:
    if len(word) < 4:
        continue
    if word in occurrences:
        occurrences[word] += 1
    else:
        occurrences[word] = 1

freqs = []
for word, occ in occurrences.items():
    freqs.append((occ, word))

freqs.sort(reverse=True)

for occ, freq in freqs[:5]:
    print "%s : %s" % (freq, occ)



