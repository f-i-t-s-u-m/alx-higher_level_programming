#!/usr/bin/python3
for y in range(0, 10):
    for x in range(0, 10):
        if int('%d%d' % (y,x)) == 99:
            print(int('%d%d' % (y,x)))
        elif int('%d%d' % (x,y)) >= int('%d%d' % (y,x)):
            print("{:0>2}".format(int('%d%d' % (y,x))), end=', ')
