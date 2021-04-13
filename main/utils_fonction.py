# AI generatrice
# Author : JM Cheumeni
import numpy as np
import copy
from tkinter import *

## construction de la liste des coordonnees des points entre
## le point de depart et le point d'arrivee
def listeCordBox(a, b, liste_pos_x, liste_pos_y):
    '''

    :param a:
    :param b:
    :param liste_pos_x:
    :param liste_pos_y:
    :return:
    '''

    if a[0]>b[0]:
        for i in range(1, a[0]-b[0]+1):
            liste_pos_x.append(a[0]-i)
    elif a[0]< b[0]:
        for i in range(1, b[0]-a[0]+1):
            liste_pos_x.append(a[0]+i)
    else:
        liste_pos_x.append(a[0])

    if a[1]>b[1]:
        for i in range(0, a[1]-b[1]+1):
            liste_pos_y.append(a[1]-i)
    elif a[1]<b[1]:
        for i in range(0, b[1]-a[1]+1):
            liste_pos_y.append(a[1]+i)
    else:
        liste_pos_y.append(a[1])


def circleCoord(list1, offset):
    '''

    :param list1:
    :param offset:
    :return:
    '''
    pt_x = list1[1] + offset
    pt_y = list1[0] + offset
    return pt_x, pt_y

def textCoord(pt_x, pt_y, pas):
    '''

    :param pt_x:
    :param pt_y:
    :param pas:
    :return:
    '''
    pt_x_text = pas * (pt_x - 1)
    pt_y_text = pas * (pt_y - 1)
    return pt_x_text, pt_y_text