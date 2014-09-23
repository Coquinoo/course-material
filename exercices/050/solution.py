# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
num = [3, 5]
max = 999

result = 0
for mult in num:
    for i in range(1,max):
        if mult*i < max:
            result += mult*i
print result