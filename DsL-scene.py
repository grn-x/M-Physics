import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Constants
distance_between_borders = 4  # Distance between the two street borders
car_angle = -130  # Angle of intersection for Dom's car (in degrees)
tank_angle = -80  # Angle of intersection for the tank (in degrees)
car_x_distance = 9  # Distance of car from the street origin (x-axis)
tank_x_distance = 10  # Distance of tank from the street origin (x-axis)

# Physics
mass_d = 110
mass_l = 70
speed_d = 120
speed_l = 100

def distance(point1, point2):
    """Calculate the distance between two points."""
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

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

        # Calculate distances
        car_distance = distance(car_border_intersection, (intersect_x, intersect_y))
        tank_distance = distance(tank_border_intersection, (intersect_x, intersect_y))

        # Calculate time traveled
        car_time = car_distance / speed_d
        tank_time = tank_distance / speed_l

        print(f"Car distance to intersection: {car_distance:.2f} units, Time traveled: {car_time:.2f} seconds")
        print(f"Tank distance to intersection: {tank_distance:.2f} units, Time traveled: {tank_time:.2f} seconds")

        # Calculate resulting vector using impulse-momentum theorem
        car_momentum = mass_d * speed_d
        tank_momentum = mass_l * speed_l

        total_momentum_x = car_momentum * np.cos(car_angle_rad) + tank_momentum * np.cos(tank_angle_rad)
        total_momentum_y = car_momentum * np.sin(car_angle_rad) + tank_momentum * np.sin(tank_angle_rad)

        resulting_speed = np.sqrt(total_momentum_x**2 + total_momentum_y**2) / (mass_d + mass_l)
        resulting_angle = np.degrees(np.arctan2(total_momentum_y, total_momentum_x))

        print(f"Resulting speed: {resulting_speed:.2f} units/s, Resulting angle: {resulting_angle:.2f} degrees")

        # Draw the resulting vector
        resulting_vector_x = [intersect_x, intersect_x + resulting_speed * np.cos(np.radians(resulting_angle))]
        resulting_vector_y = [intersect_y, intersect_y + resulting_speed * np.sin(np.radians(resulting_angle))]
        ax.plot(resulting_vector_x, resulting_vector_y, 'g-', linewidth=2, label="Resulting Vector")

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
    ax.plot(tank_perp_x, tank_perp_y, 'y-', linewidth=2, label="Tank Perpendicular")

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