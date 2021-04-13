# AI generatrice
# Author : JM Cheumeni
import numpy as np
import copy
from tkinter import *


class QAgentAI():
    '''

    '''
    # Initialisation de alpha, gamma, states, actions, rewards, and Q-values
    def __init__(self, alpha, gamma, location_to_state, actions, rewards, state_to_location, Q, dimMatrix):

        self.gamma = gamma
        self.alpha = alpha
        self.dim = dimMatrix

        self.location_to_state = location_to_state
        self.actions = actions
        self.rewards = rewards
        self.state_to_location = state_to_location

        self.Q = Q

    # Entrainement de l'agent dans l'environnement
    def training(self, list_current_pt, start_location, end_location, iterations):

        rewards_new = np.copy(self.rewards)

        ending_state = self.location_to_state[end_location]
        rewards_new[ending_state, ending_state] = 1000

        for i in range(iterations):
            current_state = np.random.choice(list_current_pt)  # l'etat courant initiale de l'Agent AI
            playable_actions = []

            for j in range(self.dim*self.dim):
                if rewards_new[current_state, j] > 0:
                    playable_actions.append(j) # Etat directement acceccible depuis l'etat courant

            next_state = np.random.choice(playable_actions)
            ## Calcul de la difference temporelle
            TempDiff = rewards_new[current_state, next_state] + \
                 self.gamma * self.Q[next_state, np.argmax(self.Q[next_state,])] - self.Q[current_state, next_state]

            self.Q[current_state, next_state] += self.alpha * TempDiff

        route = [start_location] # initialisation du point de depart
        next_location = start_location # Comme le prochain mouv de l'Agent n'est connu,
                                       # le next_loc est encore le point de depart

        # Obtenir le chemin optimal
        return self.get_optimal_route(start_location, end_location, next_location, route, self.Q)

    # Obtenir le chemin optimal
    def get_optimal_route(self, start_location, end_location, next_location, route, Q):

        interm = copy.copy(start_location)
        while (next_location != end_location): # On boucle tant que l'emplacement suivant different de la fin
            starting_state = self.location_to_state[start_location]
            next_state = np.argmax(Q[starting_state,])
            next_location = self.state_to_location[next_state]
            route.append(next_location)
            start_location = next_location

        print('Itineraire:{}-{}'.format(interm, next_location), route)
        return route

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

## Fonction permettant de tester l'IA generatrice
def testQAgentAI():
    '''

    :return:
    '''
    # Initailisation des parametres
    gamma = 0.75  # facteur de remise ou d'actualisation
    alpha = 0.9  # Taux d'apprentissage
    n = 4
    #board = [[iInitSeedsPerHole for x in range(iColumns)] for y in range(n)]
    ## Generation des etats de depart, tresor et sortie
    state_matrix = ['L'+ str(i+1) for i in range(n*n)]
    treasurekeypoint = np.random.choice(state_matrix)
    startkeypoint = treasurekeypoint
    endkeypoint = startkeypoint
    while(startkeypoint == treasurekeypoint):
        startkeypoint = np.random.choice(state_matrix)
    while (endkeypoint == treasurekeypoint or endkeypoint == startkeypoint):
        endkeypoint = np.random.choice(state_matrix)

    ## Table permettant d'associer les etats avec leurs voisins
    tableAssociation = [('L1', ('L2', 'L5')), ('L2', ('L1', 'L6', 'L3')), ('L3', ('L2', 'L7', 'L4')), ('L4', ('L3', 'L8')),
                        ('L5', ('L1', 'L6', 'L9')), ('L6', ('L2', 'L5', 'L7','L10')), ('L7', ('L8', 'L6', 'L3', 'L11')), ('L8', ('L4', 'L7', 'L12')),
                        ('L9', ('L5', 'L10', 'L13')), ('L10', ('L9', 'L6', 'L11', 'L14')), ('L11', ('L10', 'L7', 'L12', 'L15')),
                        ('L12', ('L8', 'L11', 'L16')), ('L13', ('L9', 'L14')), ('L14', ('L13', 'L10', 'L15')), ('L15', ('L14', 'L11', 'L16')),
                        ('L16', ('L15', 'L12'))]

    # Definition des etats de modele
    location_to_state = {} # etats de la grille
    actions = [] # action possible sur la grille
    for i in range(n*n):
        location_to_state['L'+ str(i+1)] = i
        actions.append(i)
    ## attribution de coordonnee a chaque box
    box_coord = []
    for i in range(n):
        for j in range(n):
            box_coord.append((i,j))
    ## Mappage entre coordonnee et location_state
    state_box_coord = {}
    state_coord_box = {}
    for i in range(len(box_coord)):
        state_box_coord['L'+ str(i+1)] = box_coord[i]
    for i in range(len(box_coord)):
        state_coord_box[box_coord[i]] = 'L'+ str(i+1)

    print("TreasureKeyPoint", treasurekeypoint)
    print("StartKeyPoint", startkeypoint)
    print("EndKeyPoint",endkeypoint)
    tkp = state_box_coord[treasurekeypoint]
    stp = state_box_coord[startkeypoint]
    etp = state_box_coord[endkeypoint]
    liste_pos_x, liste_pos_y = [], []
    liste_pos_m, liste_pos_n = [], []
    list_co_1,  list_co_2 = [], []
    list_co_1.append(tkp)
    list_co_2.append(stp)
    ## fonction donnant les coordonnees des points entre stp, tkp et etp
    listeCordBox(tkp, stp, liste_pos_x, liste_pos_y)
    listeCordBox(stp, etp, liste_pos_m, liste_pos_n)

    for i in liste_pos_x:
        for j in liste_pos_y:
            list_co_1.append((i,j))
    for i in liste_pos_m:
        for j in liste_pos_n:
            list_co_2.append((i,j))
    ##
    state_list_1 = np.sort([state_coord_box[res] for res in list_co_1])
    state_list_1 = list(set(state_list_1))
    state_list_2 = np.sort([state_coord_box[res] for res in list_co_2])
    state_list_2 = list(set(state_list_2))

    # Table des recompenses, permet de representer la possibilite de se deplacer
    # d'une case a une autre : des murs virtuels
    list_current_pt = []
    rewards = np.array(np.zeros([n*n, n*n]))
    for state in state_matrix:
        if state in state_list_1 or state in state_list_2:
            for res in tableAssociation:
                if state == res[0]:
                    if len(res[1]) == 2 :
                        rewards[state_matrix.index(state), state_matrix.index(res[1][0])] = 1
                        rewards[state_matrix.index(state), state_matrix.index(res[1][1])] = 1
                        list_current_pt.append(state_matrix.index(state))
                    elif len(res[1]) == 3 :
                        rewards[state_matrix.index(state), state_matrix.index(res[1][0])] = 1
                        rewards[state_matrix.index(state), state_matrix.index(res[1][1])] = 1
                        rewards[state_matrix.index(state), state_matrix.index(res[1][2])] = 1
                        list_current_pt.append(state_matrix.index(state))
                    elif len(res[1]) == 4 :
                        rewards[state_matrix.index(state), state_matrix.index(res[1][0])] = 1
                        rewards[state_matrix.index(state), state_matrix.index(res[1][1])] = 1
                        rewards[state_matrix.index(state), state_matrix.index(res[1][2])] = 1
                        rewards[state_matrix.index(state), state_matrix.index(res[1][3])] = 1
                        list_current_pt.append(state_matrix.index(state))
        else:
            if np.random.randint(0,1) == 0:
                for res in tableAssociation:
                    if state == res[0]:
                        if len(res[1]) == 2:
                            rewards[state_matrix.index(state), state_matrix.index(res[1][0])] = 1
                            rewards[state_matrix.index(state), state_matrix.index(res[1][1])] = 1
                            list_current_pt.append(state_matrix.index(state))
                        elif len(res[1]) == 3:
                            rewards[state_matrix.index(state), state_matrix.index(res[1][0])] = 1
                            rewards[state_matrix.index(state), state_matrix.index(res[1][1])] = 1
                            rewards[state_matrix.index(state), state_matrix.index(res[1][2])] = 1
                            list_current_pt.append(state_matrix.index(state))
                        elif len(res[1]) == 4:
                            rewards[state_matrix.index(state), state_matrix.index(res[1][0])] = 1
                            rewards[state_matrix.index(state), state_matrix.index(res[1][1])] = 1
                            rewards[state_matrix.index(state), state_matrix.index(res[1][2])] = 1
                            rewards[state_matrix.index(state), state_matrix.index(res[1][3])] = 1
                            list_current_pt.append(state_matrix.index(state))

    list_current_pt = list(set(list_current_pt))

    # Mappage inverse et Accessibilite des box
    state_to_location = dict((state, location) for location, state in location_to_state.items())
    # Initialisation des Q-Values
    Q_0 = np.array(np.zeros([n*n, n*n]))
    Q_1 = np.array(np.zeros([n*n, n*n]))
    ## instanciaiton des Agent AI
    qagentai_0 = QAgentAI(alpha, gamma, location_to_state, actions, rewards, state_to_location, Q_0, n)
    qagentai_1 = QAgentAI(alpha, gamma, location_to_state, actions, rewards, state_to_location, Q_1, n)

    ## Apprentissage de la Map pour relier le treasurekeypoint et le startkeypoint, le startkeypoint et le endkeypoint
    route1 = qagentai_0.training(list_current_pt, treasurekeypoint, startkeypoint, 1000)
    route2 = qagentai_1.training(list_current_pt, startkeypoint, endkeypoint, 1000)

    coord_route1 = [state_box_coord[res] for res in route1]
    coord_route2 = [state_box_coord[res] for res in route2]

    return coord_route1, coord_route2


def traceCercle (x, y, pas):
    '''

    :param x:
    :param y:
    :param PAS:
    :return:
    '''
    couleur_list = ['red', 'green','blue']
    r = 15  #rayon
    #passage des coordonnées en cases aux coordonnées pixels
    x = pas*(x-1)
    y = pas*(y-1)
    #ici la fonction renvoie une référence vers le cercle créé pour pouvoir le réutiliser ultérieurement
    return can.create_oval (x-r, y-r, x+r, y+r, fill=np.random.choice(couleur_list),outline='black')

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

if __name__ == "__main__":

    list1, list2 = testQAgentAI()

    ## affichage de key point dans une grille
    fen = Tk()
    offset = 1.5
    COTE = 400
    can = Canvas(fen, bg="ivory", height=COTE, width=COTE)
    can.pack()
    NB_DE_CASES = 4
    PAS = COTE / NB_DE_CASES
    x = 0
    while (x <= NB_DE_CASES):
        can.create_line(0, PAS * x, COTE, PAS * x, fill='black')
        can.create_line(PAS* x,0, PAS * x, COTE, fill='black')
        x = x + 1
    ## treasureKeypoint
    pt_x, pt_y = circleCoord(list1[0], offset)
    pt_x_text, pt_y_text = textCoord(pt_x, pt_y, PAS)
    monPion = traceCercle(pt_x, pt_y, PAS)
    can.create_text(pt_x_text, pt_y_text, text="TreasureKeyPoint")
    ## startkeypoint
    pt_x_1, pt_y_1 = circleCoord(list2[0], offset)
    pt_x_text_1, pt_y_text_1 = textCoord(pt_x_1, pt_y_1, PAS)
    monPion_1 = traceCercle(pt_x_1, pt_y_1, PAS)
    can.create_text(pt_x_text_1, pt_y_text_1, text="StartKeyPoint")
    ## endkeypoint
    pt_x_2, pt_y_2 = circleCoord(list2[len(list2)-1], offset)
    pt_x_text_2, pt_y_text_2 = textCoord(pt_x_2, pt_y_2, PAS)
    monPion_2 = traceCercle(pt_x_2, pt_y_2, PAS)
    can.create_text(pt_x_text_2, pt_y_text_2, text="EndKeyPoint")

    fen.mainloop()