import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Constants
g = 9.81
ROPE_LENGTH = 80
BUILDING_1_HEIGHT = 226
BUILDING_2_HEIGHT = 166.55
initial_velocity = 10  #m/s
initial_position = [-30, BUILDING_1_HEIGHT]  # Starting point of the throw
def distance(point1, point2):
    """calculate length of hypotenuse to determine distance to circle center"""
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def parabolic_trajectory(v0, g, x0, y0, t): # waagerechter Wurf
    x = x0 + v0 * t
    y = y0 - 0.5 * g * t**2
    return x, y

def parabolic_curve(x, v0, g, x0, y0):
    """Calculate the y-coordinate for a given x-coordinate."""
    return y0 - (g / (2 * v0**2)) * (x - x0)**2

def setup():
    fig, ax = plt.subplots()
    rect1 = patches.Rectangle((-30, 0), 30, BUILDING_1_HEIGHT, linewidth=1, edgecolor='r', facecolor='r', alpha=0.5)
    rect2 = patches.Rectangle((44.25, 0), 44.25 - 56.75, BUILDING_2_HEIGHT, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
    point = patches.Circle((initial_position[0], initial_position[1]), 2, linewidth=3, edgecolor='g', facecolor='g', alpha=1)
    circle = patches.Circle((initial_position[0], initial_position[1]), ROPE_LENGTH, linewidth=1, edgecolor='g', facecolor='none', alpha=1)

    ax.add_patch(point)
    ax.add_patch(circle)
    ax.add_patch(rect1)
    ax.add_patch(rect2)

    """# Calculate the parabolic trajectory
    t_values = np.linspace(0, 5, num=500)  # Time values
    trajectory = [parabolic_trajectory(initial_velocity, g, initial_position[0], initial_position[1], t) for t in t_values]
    x_values, y_values = zip(*trajectory)
    """
    # Calculate the parabolic trajectory
    x_values = []
    y_values = []

    """ 
   #plot parabolic trajectory
   t_values = np.linspace(0, 5, num=500)  # Time values
    for t in t_values:
        x, y = parabolic_trajectory(initial_velocity, g, initial_position[0], initial_position[1], t)
        if distance((x, y), initial_position) <= ROPE_LENGTH:
            x_values.append(x)
            y_values.append(y)
        else:
            break
    """

   #plot parabolic curve
    x = initial_position[0]
    x_step = -0.1  # Step size for x
    while True:
        y = parabolic_curve(x, initial_velocity, g, initial_position[0], initial_position[1])
        if distance((x, y), initial_position) <= ROPE_LENGTH:
            x_values.append(x)
            y_values.append(y)
        else:
            break
        x += x_step

    # Plot the parabolic trajectory
    ax.plot(x_values, y_values, color='purple')

    # Set the plot limits
    ax.set_xlim(-100, 150)
    ax.set_ylim(20, 270)

    # Add labels and title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Mission Impossible 3')
    #plt.legend()

setup()
plt.show()
