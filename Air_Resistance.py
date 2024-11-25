import numpy as np
import matplotlib.pyplot as plt

# Constantes physiques
g = 9.81  # Accélération gravitationnelle (m/s^2)
rho = 1.0  # Densité de l'air (kg/m^3)
Cd = 0.5  # Coefficient de traînée
A = 7e-4  # Surface de l'objet (m^2)
m = 0.00000001  # Masse de l'objet (kg)

# Conditions initiales
v0 = 18.0  # Vitesse initiale (m/s)
angle = np.pi / 4  # Angle de lancement (radians)
x0, y0 = 0.0, 300.0  # Position initiale (m)
v0x = v0 * np.cos(angle)  # Composante horizontale de la vitesse initiale
v0y = v0 * np.sin(angle)  # Composante verticale de la vitesse initiale

# Paramètres de simulation
t_max = 30.0  # Durée maximale de la simulation (s)
dt = 0.01  # Pas de temps (s)

# Fonctions pour calculer les accélérations
def acceleration_x(vx, vy):
    v = np.sqrt(vx**2 + vy**2)
    if v == 0:  # Éviter la division par zéro
        return 0
    Fd = 0.5 * Cd * rho * A * v**2
    ax = -Fd * vx / v
    return ax

def acceleration_y(vx, vy):
    v = np.sqrt(vx**2 + vy**2)
    if v == 0:  # Éviter la division par zéro
        return -g
    Fd = 0.5 * Cd * rho * A * v**2
    ay = -g - (Fd * vy / v)
    return ay

# Simulation avec la méthode d'Euler
def simulate_trajectory():
    # Initialisation des listes de résultats
    time = np.arange(0, t_max, dt)
    x, y = [x0], [y0]
    vx, vy = v0x, v0y  # Vitesse initiale
    t_touch_ground = None  # Instant où la pomme touche le sol

    # Boucle de simulation
    for i, t in enumerate(time[1:], 1):
        # Calcul des accélérations
        ax = acceleration_x(vx, vy)
        ay = acceleration_y(vx, vy)

        # Mise à jour des vitesses
        vx += ax * dt
        vy += ay * dt

        # Mise à jour des positions
        x.append(x[-1] + vx * dt)
        y.append(y[-1] + vy * dt)

        # Vérification si la pomme touche le sol
        if y[-1] <= 0:
            t_touch_ground = t  # Enregistrer l'instant où la pomme touche le sol
            break  # Arrêter la simulation une fois la pomme au sol

    return time[:i+1], x, y, t_touch_ground

# Exécution de la simulation
r, x, y, t_touch_ground = simulate_trajectory()

# Afficher l'instant où la pomme touche le sol
if t_touch_ground is not None:
    print(f"La pomme touche le sol à t = {t_touch_ground:.2f} secondes.")

# Tracé des résultats
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title("Trajectoire du mobile")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.grid(True)
plt.show()
