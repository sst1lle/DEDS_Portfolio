import pygame
import numpy as np

# Define constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0) # Obstacles
RED = (200, 50, 50) # Hazards
GREEN = (50, 200, 50) # Goal
GRAY = (200, 200, 200) # Empty cells
BLUE = (50, 50, 200) # Agent

# Constants for grid types (These are internal grid markers, not rewards directly)
EMPTY = 0
OBSTACLE = 1
HAZARD = -1
GOAL = 10 

CELL_SIZE = 60 # Aangepast naar 60, consistent met main.py
# Omgevingsklasse voor de grid wereld
class Environment:
    def __init__(self, grid_size=10):
        self.grid_size = grid_size
        self.width = grid_size
        self.height = grid_size
        # Definieer rewards voor de omgeving
        self.rewards = {
            EMPTY: -0.05,  # Een beetje hogere penalty per stap, om efficiëntie te stimuleren
            HAZARD: -50,   # Grote penalty voor gevaren, om ze te vermijden
            GOAL: 100      # Grote beloning voor doel
        }
        self.reset()
        
    def reset(self):
        # Initialiseer het grid met allemaal 'lege' cellen
        self.grid = np.zeros((self.height, self.width), dtype=int)
        
        # Definieer start en doelposities
        self.start = (0, 0)
        self.goal = (5, 0) # (9,9) voor een 10x10 grid
        
        # --- HAALBARE MAZE LAY-OUT MET MINDER OBSTAKELS EN HAZARDS ---
        # Deze lay-out is getest en de agent zou hier een pad doorheen moeten kunnen vinden.
        
        self.obstacles = [
            # Horizontale muren
            (1, 1), (1, 2), (1, 3), (1, 4), # Muur boven de start
            (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), # Middelste barrière
            (5, 5), (5, 6), (5, 7), (5, 8), # Muur rechterkant
            (7, 1), (7, 2), (7, 3), (7, 4), # Muur onder
            (7, 9), (7, 8), (8,8), (8, 9),
            (3, 9),
            
            # Verticale muren
            (0, 7), (1, 7), (2, 7), # Muur rechtsboven
            (2, 5), (3, 5), (4, 5), # Muur midden
            (6, 0), (7, 0), (8, 0), # Muur linksonder
         
            (6, 6), (7, 6), (8, 6), # Muur rechtsonder
        ]
        
        self.hazards = [
            (0, 6), # Hazard vlakbij start (niet direct blokkerend)
            (2, 4),
            (4, 7),
            (6, 3),
            (8, 4), # Hazard vlakbij doel
            (9, 9),
            (4, 0),
            (0, 8)
        ]
        
        # --- EINDE MAZE LAY-OUT ---

        # Plaats de obstakels en gevaren op het grid
        for obs_y, obs_x in self.obstacles:
            if 0 <= obs_y < self.height and 0 <= obs_x < self.width:
                self.grid[obs_y, obs_x] = OBSTACLE
        for haz_y, haz_x in self.hazards:
            if 0 <= haz_y < self.height and 0 <= haz_x < self.width:
                self.grid[haz_y, haz_x] = HAZARD
        
        # Controleer of start en doel niet toevallig in een obstakel of hazard liggen
        # Dit is een basiscontrole; een geavanceerder systeem zou een geldige maze genereren
        if self.grid[self.start[0], self.start[1]] != EMPTY:
            print(f"WAARSCHUWING: Startpunt {self.start} is geblokkeerd! Pas de maze lay-out aan.")
        if self.grid[self.goal[0], self.goal[1]] != EMPTY:
            print(f"WAARSCHUWING: Doelpunt {self.goal} is geblokkeerd! Pas de maze lay-out aan.")

        # Zet de agent op de startpositie
        self.agent_pos = self.start
        return self.agent_pos

    def step(self, action):
        y, x = self.agent_pos
        new_y, new_x = y, x

        # Bepaal de nieuwe positie op basis van de actie
        if action == 0: new_y -= 1  # Up
        elif action == 1: new_y += 1  # Down
        elif action == 2: new_x -= 1  # Left
        elif action == 3: new_x += 1  # Right

        # Controleer op geldige beweging (binnen de grenzen en niet tegen een obstakel)
        if 0 <= new_y < self.height and 0 <= new_x < self.width and \
           self.grid[new_y, new_x] != OBSTACLE:
            self.agent_pos = (new_y, new_x)
        # Anders blijft de agent op de huidige positie (heeft een muur geraakt)

        # Bepaal de beloning voor de nieuwe positie
        reward_value = self.rewards.get(self.grid[self.agent_pos[0], self.agent_pos[1]], self.rewards[EMPTY])
        done = False # Standaard is de episode nog niet afgelopen

        # Controleer of het doel is bereikt
        if self.agent_pos == self.goal:
            reward_value = self.rewards[GOAL]
            done = True
        # Controleer of een hazard is geraakt
        elif self.grid[self.agent_pos[0], self.agent_pos[1]] == HAZARD:
            reward_value = self.rewards[HAZARD]
            done = True # De episode eindigt als een hazard wordt geraakt
        
        # Als de episode is afgelopen, reset de omgeving voor de volgende episode
        if done:
            next_state = self.reset() # Reset de omgeving naar de startpositie
        else:
            next_state = self.agent_pos # De volgende staat is de huidige positie van de agent

        return next_state, reward_value, done

    def render(self, screen):
        """
        Render the grid world and the agent's position.
        Deze methode rendert alleen de omgeving en de agent.
        De Q-waarden worden in main.py gerenderd.
        """
        screen.fill(WHITE) # Vul de achtergrond wit

        # Teken de cellen van het grid
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                
                # Bepaal de kleur van de cel op basis van het type
                color = GRAY # Standaard voor lege cellen
                if self.grid[y, x] == OBSTACLE:
                    color = BLACK
                elif self.grid[y, x] == HAZARD:
                    color = RED
                elif (y, x) == self.goal:
                    color = GREEN
                
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, BLACK, rect, 1) # Celranden

        # Teken de agent
        ay, ax = self.agent_pos
        agent_rect = pygame.Rect(ax * CELL_SIZE + CELL_SIZE // 4, ay * CELL_SIZE + CELL_SIZE // 4, CELL_SIZE // 2, CELL_SIZE // 2)
        pygame.draw.ellipse(screen, BLUE, agent_rect) # Blauwe cirkel voor agent