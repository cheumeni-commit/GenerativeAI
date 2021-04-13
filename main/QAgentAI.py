# AI generatrice
# Author : JM Cheumeni
import numpy as np
import copy


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