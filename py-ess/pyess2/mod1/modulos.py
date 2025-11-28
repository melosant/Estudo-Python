from math import ceil, trunc, floor
from random import random, randint, randrange, choice, sample
from platform import platform, machine, processor, system, version

x = 2.6
y = 1.4

print(f'''
IMPORT MATH
  X / Y
-----------
  {floor(x)} / {floor(y)}
 {floor(-x)} / {floor(-y)}
  {ceil(x)} / {ceil(y)}
 {ceil(-x)} / {ceil(-y)}
  {trunc(x)} / {trunc(y)}
 {trunc(-x)} / {trunc(-y)}''')

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'''
IMPORT RANDOM
-------------
{random()}
{randint(1,10)}
{randrange(1,10)}
{choice(lista)}
{sample(lista, 5)}''')

print(f'''
IMPORT PLATFORM
---------------
{platform()}
{platform(1)}
{platform(0,1)}
{machine()}
{processor()}
{system()}
{version()}''')