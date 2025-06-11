import pygame
import sys
from environment import Environment, CELL_SIZE, BLACK, WHITE, GRAY, RED, GREEN, BLUE # Importeer direct constanten
from q_learning import QLearningAgent # Importeer alleen QLearningAgent
from utils import plot_convergence_curve # Importeer alleen plot_convergence_curve

# Config
GRID_SIZE = 10
# CELL_SIZE is nu geïmporteerd vanuit environment_agent.py
WINDOW_WIDTH = GRID_SIZE * CELL_SIZE * 2 # Linker grid + Rechter Q-value grid
WINDOW_HEIGHT = GRID_SIZE * CELL_SIZE
FPS = 60
EPISODES = 3000 # Verhogen voor betere training

# Pygame initialisatie
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Q-Learning Grid World")
clock = pygame.time.Clock()
font_small = pygame.font.SysFont(None, 18) # Klein font voor Q-waarden
font_large = pygame.font.SysFont(None, 24) # Groter font voor titels

# Initialiseer omgeving en Q-Learning agent
env = Environment(grid_size=GRID_SIZE)
# Definieer de acties voor de Q-Learning agent
ACTIONS = [0, 1, 2, 3] # 0: Up, 1: Down, 2: Left, 3: Right
q_agent = QLearningAgent(actions=ACTIONS) # Geef de acties door

def draw_q_values_grid(q_table, offset_x):
    """
    Tekent een aparte grid aan de rechterkant met Q-waarden voor elke staat.
    """
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = offset_x + col * CELL_SIZE
            y = row * CELL_SIZE
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect) # Achtergrond
            pygame.draw.rect(screen, BLACK, rect, 1) # Rand

            state = (row, col)
            q_values_for_state = q_table.get(state, {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0})
            
            # Toon de Q-waarden voor UP, DOWN, LEFT, RIGHT in de cel
            # Up
            text_up = font_small.render(f"U:{q_values_for_state[0]:.1f}", True, BLACK)
            screen.blit(text_up, (x + 5, y + 5))
            # Down
            text_down = font_small.render(f"D:{q_values_for_state[1]:.1f}", True, BLACK)
            screen.blit(text_down, (x + 5, y + 20))
            # Left
            text_left = font_small.render(f"L:{q_values_for_state[2]:.1f}", True, BLACK)
            screen.blit(text_left, (x + 5, y + 35))
            # Right
            text_right = font_small.render(f"R:{q_values_for_state[3]:.1f}", True, BLACK)
            screen.blit(text_right, (x + 5, y + 50))


def main():
    running = True
    training_mode = False # Om te schakelen tussen handmatig en training
    convergences = []

    while running:
        # Handmatige beweging wordt alleen afgehandeld als NIET in training_mode
        # en in de event loop.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: # Reset omgeving en Q-tabel
                    env.reset()
                    q_agent.reset()
                    convergences.clear()
                    print("Environment and Q-table reset.")
                elif event.key == pygame.K_t: # Start/Stop training
                    training_mode = not training_mode
                    if training_mode:
                        print(f"Training started for {EPISODES} episodes...")
                        convergences.clear()
                    else:
                        print("Training paused.")
                
                # Handmatige agent beweging (alleen als niet in training mode)
                if not training_mode:
                    if event.key == pygame.K_UP:
                        # Agent beweegt handmatig (zonder Q-learning)
                        next_state, reward, done = env.step(0) 
                        print(f"Manual Move: new pos={next_state}, reward={reward}")
                        if done:
                            print("Goal reached or Hazard hit! Environment reset for manual control.")
                    elif event.key == pygame.K_DOWN:
                        next_state, reward, done = env.step(1)
                        print(f"Manual Move: new pos={next_state}, reward={reward}")
                        if done:
                            print("Goal reached or Hazard hit! Environment reset for manual control.")
                    elif event.key == pygame.K_LEFT:
                        next_state, reward, done = env.step(2)
                        print(f"Manual Move: new pos={next_state}, reward={reward}")
                        if done:
                            print("Goal reached or Hazard hit! Environment reset for manual control.")
                    elif event.key == pygame.K_RIGHT:
                        next_state, reward, done = env.step(3)
                        print(f"Manual Move: new pos={next_state}, reward={reward}")
                        if done:
                            print("Goal reached or Hazard hit! Environment reset for manual control.")

        # Game State Update (training of rendering)
        if training_mode:
            if len(convergences) < EPISODES: # Voer episodes uit totdat het aantal EPISODES is bereikt
                reward = q_agent.train_episode(env) # Q-agent traint 1 episode
                convergences.append(reward)
                if len(convergences) % 100 == 0:
                    print(f"Episode {len(convergences)}/{EPISODES}, Total Reward: {reward}")
            else:
                training_mode = False
                print("Training complete.")
                plot_convergence_curve(convergences) # Plot de curve na training

        # Renderen van de omgeving
        env.render(screen) # Geef de Q-tabel door
        draw_q_values_grid(q_agent.q_table, GRID_SIZE * CELL_SIZE) # Teken de aparte Q-waarden grid
        pygame.display.flip() # Update het hele scherm
        clock.tick(FPS) # Beperk de framerate

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()