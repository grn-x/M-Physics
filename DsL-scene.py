import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Constants
distance_between_borders = 4  # Distance between the two street borders
car_angle = -110  # Angle of intersection for Dom's car (in degrees)
tank_angle = -60  # Angle of intersection for the tank (in degrees)
car_x_distance = 2  # Distance of car from the street origin (x-axis)
tank_x_distance = 8  # Distance of tank from the street origin (x-axis)

def plot_scene():
    left_border_x = (10 - distance_between_borders) / 2
    right_border_x = left_border_x + distance_between_borders

    car_border_intersection = (right_border_x, car_x_distance)
    tank_border_intersection = (left_border_x, tank_x_distance)

    fig, ax = plt.subplots(figsize=(10, 6))

    street_y = [0, 10]
    ax.plot([left_border_x, left_border_x], street_y, 'k-', linewidth=2, label="Left Street Border")
    ax.plot([right_border_x, right_border_x], street_y, 'k-', linewidth=2, label="Right Street Border")

    car_angle_rad = np.radians(car_angle)
    tank_angle_rad = np.radians(tank_angle)
    car_slope = np.tan(car_angle_rad)
    tank_slope = np.tan(tank_angle_rad)

    car_traj_x = [car_border_intersection[0], car_border_intersection[0] + 5 * np.cos(car_angle_rad)]
    car_traj_y = [car_border_intersection[1], car_border_intersection[1] + 5 * np.sin(car_angle_rad)]

    tank_traj_x = [tank_border_intersection[0], tank_border_intersection[0] + 5 * np.cos(tank_angle_rad)]
    tank_traj_y = [tank_border_intersection[1], tank_border_intersection[1] + 5 * np.sin(tank_angle_rad)]

    ax.plot(car_traj_x, car_traj_y, 'b--', linewidth=1, label="Dom's Trajectory")
    ax.plot(tank_traj_x, tank_traj_y, 'r--', linewidth=1, label="Tank's Trajectory")

    car_border_exit_x = car_border_intersection[0] + 5 * np.cos(car_angle_rad)
    car_border_exit_y = car_border_intersection[1] + 5 * np.sin(car_angle_rad)

    tank_border_exit_x = tank_border_intersection[0] + 5 * np.cos(tank_angle_rad)
    tank_border_exit_y = tank_border_intersection[1] + 5 * np.sin(tank_angle_rad)

    ax.plot([car_border_intersection[0], car_border_exit_x], [car_border_intersection[1], car_border_exit_y], 'b-', linewidth=3)
    ax.plot([tank_border_intersection[0], tank_border_exit_x], [tank_border_intersection[1], tank_border_exit_y], 'r-', linewidth=3)

    car_intercept = car_border_intersection[1] - car_slope * car_border_intersection[0]
    tank_intercept = tank_border_intersection[1] - tank_slope * tank_border_intersection[0]

    if car_slope != tank_slope:
        intersect_x = (tank_intercept - car_intercept) / (car_slope - tank_slope)
        intersect_y = car_slope * intersect_x + car_intercept
        ax.plot(intersect_x, intersect_y, 'ko', markersize=10, label="Intersection")

    car_length, car_width = 1, 0.5
    car_perpendicular_slope = -1 / car_slope
    car_perpendicular_length = car_width / 2
    delta_x = car_perpendicular_length / np.sqrt(1 + car_perpendicular_slope ** 2)
    delta_y = car_perpendicular_slope * delta_x
    car_perp_x = [car_border_intersection[0], car_border_intersection[0] - delta_x]
    car_perp_y = [car_border_intersection[1], car_border_intersection[1] - delta_y]

    ax.plot(car_perp_x, car_perp_y, 'y-', linewidth=2, label="Car Perpendicular")


    car = patches.Rectangle(
        (car_border_intersection[0] - car_length / 2, car_border_intersection[1] - car_width / 2),
        car_length,
        car_width,
        angle=car_angle,
        color="blue",
        label="Dom's Car",
    )
    ax.add_patch(car)

    tank_length, tank_width = 2, 1
    tank_perpendicular_slope = -1 / tank_slope
    tank_perpendicular_length = tank_width / 2
    delta_x = tank_perpendicular_length / np.sqrt(1 + tank_perpendicular_slope ** 2)
    delta_y = tank_perpendicular_slope * delta_x
    tank_perp_x = [tank_border_intersection[0], tank_border_intersection[0] - delta_x]
    tank_perp_y = [tank_border_intersection[1], tank_border_intersection[1] - delta_y]
    ax.plot(tank_perp_x, tank_perp_y, 'y-', linewidth=2, label="tank Perpendicular")

    tank = patches.Rectangle(
        (tank_border_intersection[0] - tank_length / 2, tank_border_intersection[1] - tank_width / 2),
        tank_length,
        tank_width,
        angle=tank_angle,
        color="red",
        label="Tank",
    )
    ax.add_patch(tank)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal', adjustable='datalim')
    ax.legend()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Dom Saves Letty Scene")
    plt.grid(True)
    plt.show()

plot_scene()
