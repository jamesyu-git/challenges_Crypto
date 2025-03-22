# python .\task1.py 10

import sys

a = int(sys.argv[1])
b = a*2-1

for i in range(1, b+2, 2):
    move = round((b-i)/2)
    print(f' '*move, end='')
    print('*'*i)
