import matplotlib.pyplot as plt
#dirty code, need to fix some stuff
hour_mL_map = {
    0: 50,
    1: 30,
    2: 20,
    3: 16,
    4: 13,
    5: 13,
    6: 13
}

hours = list(hour_mL_map.keys())
volumes = list(hour_mL_map.values())

start_hour = hours[0]
end_hour = hours[-1]
start_volume = volumes[0]
end_volume = volumes[-1]
mid_hour = hours[4]
mid_volume = volumes[4]

delta_v = mid_volume - start_volume
delta_t = mid_hour - start_hour

average_reaction_speed = delta_v / delta_t

constant = 1.5 # need to calculate the volume to mole ratio to

n_per_hour = average_reaction_speed * constant

print(f"Average reaction speed: {average_reaction_speed:.2f} mL/h")
print(f"n/h: {n_per_hour:.2f}")

plt.plot(hours, volumes, marker='o', label='Volume-Time Data')
plt.xlabel('Hour')
plt.ylabel('mL')
plt.title('Volume-Time Diagram')
plt.grid(True)

plt.plot([start_hour, end_hour], [start_volume, end_volume], 'r--', label='Secant Line')

plt.plot([start_hour, start_hour], [start_volume, end_volume], 'g-', label='Vertical Line')
plt.plot([start_hour, end_hour], [end_volume, end_volume], 'b-', label='Horizontal Line')

plt.text(start_hour, (start_volume + end_volume) / 2, f'ΔV = {delta_v}', verticalalignment='center', horizontalalignment='right')
plt.text((start_hour + end_hour) / 2, end_volume, f'Δt = {delta_t}', verticalalignment='top', horizontalalignment='center')

plt.legend()
plt.show()