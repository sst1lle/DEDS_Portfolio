import matplotlib.pyplot as plt
import numpy as np # Nieuwe import nodig voor rolling mean


# De plot_convergence_curve functie voor directe weergave kan ook de rolling mean gebruiken
def plot_convergence_curve(rewards, window_size=100):
    """
    Plot de convergentiecurve direct in een grafiek, inclusief een rolling mean.
    :param rewards: Een lijst met beloningen per episode.
    :param window_size: De grootte van het venster voor de rolling mean.
    """
    plt.figure(figsize=(12, 6)) # Grotere figuur voor betere leesbaarheid
    plt.plot(rewards, alpha=0.3, label='Total Reward per Episode') # Individuele rewards lichtjes weergeven

    if len(rewards) >= window_size:
        rolling_mean = np.convolve(rewards, np.ones(window_size)/window_size, mode='valid')
        # Pas de x-waarden aan zodat de rolling mean op de juiste plek begint
        plt.plot(np.arange(len(rolling_mean)) + window_size - 1, rolling_mean, label=f'Rolling Mean (Window {window_size})', color='red')
    else:
        plt.plot(rewards, label='Total Reward per Episode', color='blue')

    plt.xlabel('Episode')
    plt.ylabel('Total Reward')
    plt.title('Q-Learning Convergence Curve')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show() # Gebruik plt.show() om de grafiek direct weer te geven