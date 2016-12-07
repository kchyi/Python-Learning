# -*- coding: utf-8 -*-
"""
Created on Wed Dec 07 11:03:43 2016

@author: kchyi
"""

from random import randint

ans = randint(1,101)
a = input()
while a != ans:
    if a < ans:
        print '%d is too small' %a
        a = input()
    else:
        print '%d is too large' %a
        a = input()
print 'Bingo! %d is the right answer' %a