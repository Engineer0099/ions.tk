import sensors
import math

sensors.start_magnetometer()
magnetic_field = sensors.get_magnetometer_data()
sensors.stop_magnetometer()

print(f"Magnetic field: {magnetic_field}")


def get_cardinal_direction(angle):
    directions = ["North", "North-East", "East", "South-East", "South", "South-West", "West", "North-West"]
    index = round(angle / 45) % 8
    return directions[index]


direction = get_cardinal_direction(magnetic_field)
print(f"User is facing {direction}")