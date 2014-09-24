# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
keywords = []
for l1 in alphabets:
    for l2 in alphabets:
            keywords.append(l1+l2)

for l1 in alphabets:
    keywords.remove(l1+l1)
    
print ('\n'.join(keywords))