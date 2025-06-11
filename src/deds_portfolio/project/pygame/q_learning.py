import random
import numpy as np

class QLearningAgent:
    def __init__(self, actions, alpha=0.1, gamma=0.9, epsilon=1.0, epsilon_decay=0.98, epsilon_min=0.01):
        """
        Initialiseert de Q-Learning agent.
        :param actions: Een lijst van mogelijke acties (bijv. [0, 1, 2, 3] voor up, down, left, right).
        :param alpha: De leerfrequentie (learning rate).
        :param gamma: De disconteringsfactor (discount factor).
        :param epsilon: De initiële exploratiekans (epsilon).
        :param epsilon_decay: De vervalfactor voor epsilon per episode.
        :param epsilon_min: De minimale waarde die epsilon kan aannemen.
        """
        self.q_table = {}  # dictionary: (state_y, state_x) -> {action: q_value}
        self.actions = actions # Bijv. [0, 1, 2, 3]
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min

    def get_qs(self, state):
        """
        Haalt de Q-waarden op voor een gegeven staat.
        Initialiseert de Q-waarden op 0.0 als de staat nieuw is.
        :param state: De huidige staat (y, x).
        :return: Een dictionary van Q-waarden voor elke actie in die staat.
        """
        if state not in self.q_table:
            self.q_table[state] = {action: 0.0 for action in self.actions}
        return self.q_table[state]

    def choose_action(self, state):
        """
        Kiest een actie met behulp van de epsilon-greedy strategie.
        :param state: De huidige staat (y, x).
        :return: De gekozen actie (integer).
        """
        if random.random() < self.epsilon:
            # Exploratie: kies een willekeurige actie
            return random.choice(self.actions)
        else:
            # Exploitatie: kies de actie met de hoogste Q-waarde
            q_values = self.get_qs(state)
            # Vind de acties met de maximale Q-waarde
            max_q = -float('inf')
            best_actions = []
            for action, q_val in q_values.items():
                if q_val > max_q:
                    max_q = q_val
                    best_actions = [action]
                elif q_val == max_q:
                    best_actions.append(action)
            return random.choice(best_actions) # Kies willekeurig uit de beste acties om tie-breaking te voorkomen

    def update_q_value(self, state, action, reward, next_state):
        """
        Werkt de Q-waarde bij volgens de Q-learning update regel.
        Q(s,a) = Q(s,a) + alpha * (reward + gamma * max(Q(s',a')) - Q(s,a))
        :param state: De huidige staat (y, x).
        :param action: De uitgevoerde actie.
        :param reward: De ontvangen beloning.
        :param next_state: De volgende staat (y', x').
        """
        current_q = self.get_qs(state)[action]
        # Haal de maximale Q-waarde op voor de volgende staat
        next_max_q = max(self.get_qs(next_state).values()) if next_state in self.q_table else 0.0
        
        new_q = current_q + self.alpha * (reward + self.gamma * next_max_q - current_q)
        self.q_table[state][action] = new_q

    def decay_epsilon(self):
        """
        Vermindert de epsilon waarde na elke episode.
        """
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def reset(self):
        """
        Reset de Q-tabel en epsilon voor een nieuwe trainingssessie.
        """
        self.q_table = {}
        self.epsilon = 1.0 # Reset epsilon naar initiële waarde voor nieuwe trainingen

    def train_episode(self, env):
        """
        Simuleert één episode van de agent die interageert met de omgeving.
        :param env: De Environment instantie.
        :return: De totale beloning die in deze episode is ontvangen.
        """
        state = env.reset() # Reset de omgeving aan het begin van elke episode
        total_reward = 0
        done = False
        
        while not done:
            action = self.choose_action(state)
            next_state, reward, done = env.step(action)
            self.update_q_value(state, action, reward, next_state)
            state = next_state
            total_reward += reward
            
            # Voorkom oneindige loops in het geval van complexe mazes of fouten
            # if total_reward < -100: # Optioneel: als te veel negatieve rewards, stop episode
            #     done = True 
        
        self.decay_epsilon()
        return total_reward

