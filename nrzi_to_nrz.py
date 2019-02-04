#!/bin/env python

def tab_2D(dim1, dim2):
    a = []
    for i in range(dim1):
        a.append([])
        for j in range(dim2):
            a[i].append(0)
    return a

b = tab_2D(2, 4)
b[0][0] = 3
b[0][1] = 0
b[0][2] = 0
b[0][3] = 3

b[1][0] = 1
b[1][1] = 2
b[1][2] = 2
b[1][3] = 1




def nrzi_to_nrz(etat,nrzi):
    liste = []
    for i in nrzi:

        entrees = 0
        if i == 0:
            entrees += 0
        if i == 1 :
            entrees += 1


        transition = b[entrees][etat]


        if transition == 0:
            print  transition,"\n"
            etat = 0
        elif transition == 1:
            print transition,"\n"
            etat = 1
        elif transition == 2:
            print  transition,"\n"
            etat = 2
        elif transition == 3:
            print transition,"\n"
            etat = 3

        liste.append(transition)



etat = int(raw_input("ETAT ? : "))



nrzi = (raw_input("NRZI ? : "))
nrzi_to_nrz(etat,nrzi)
