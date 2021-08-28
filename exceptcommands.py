# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 18:03:56 2021

@author: Matlon
"""
while True:
    try:
        x = int(input('enter num'))
        break
    except ImportError:
        print('try again')
    except ValueError:
        print('try again')

print('script done')