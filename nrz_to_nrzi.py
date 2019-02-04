#!/bin/env python


def tab_2D(dim1, dim2):
    a = []
    for i in range(dim1):
        a.append([])
        for j in range(dim2):
            a[i].append(0)
    return a

b = tab_2D(2, 2)
b[0][0] = 1
b[0][1] = 0
b[1][0] = 0
b[1][1] = 1


def nrz_to_nrzi(etat,nrz):
    entrees = 0
    if nrz == 0:
        entrees += 0
    if nrz == 1 :
        entrees += 1

    transition = b[entrees][etat]

    if transition == 1:
        print  transition,"\n"

    elif transition == 0:
        print transition,"\n"

    return transition


etat = int(raw_input("ETAT ? : "))
i=0

while i<10:
    i=+1
    nrz = int(raw_input("NRZ ? : "))
    etat = nrz_to_nrzi(etat,nrz)
