#!/usr/bin/env python
# coding=utf-8
height = 1.75
weight = 80.5
bmi = weight / height / height
if bmi >= 18.5:
    if bmi <= 25:
        print('pass')
    else:
        print('sorry, be more healthy life you should!')
else:
    print('sorry, be more healthy life you should!')


