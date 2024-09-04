def robotSim(commands, obstacles):
    # Directions: north, east, south, west
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = 0  # initially facing north
    x, y = 0, 0  # starting position

    # Convert obstacles list to a set of tuples
    obstacle_set = set(tuple(obs) for obs in obstacles)

    max_distance_squared = 0

    for command in commands:
        if command == -2:  # Turn left
            direction = (direction + 3) % 4
        elif command == -1:  # Turn right
            direction = (direction + 1) % 4
        else:  # Move forward
            for _ in range(command):
                next_x = x + directions[direction][0]
                next_y = y + directions[direction][1]

                # Check if next position is not an obstacle
                if (next_x, next_y) not in obstacle_set:
                    x, y = next_x, next_y

                # Update max distance squared
                max_distance_squared = max(max_distance_squared, x * x + y * y)

    return max_distance_squared


# Example Usage
commands = [4, -1, 3]
obstacles = []
print(robotSim(commands, obstacles))  # Output: 25

commands = [4, -1, 4, -2, 4]
obstacles = [[2, 4]]
print(robotSim(commands, obstacles))  # Output: 65

commands = [6, -1, -1, 6]
obstacles = []
print(robotSim(commands, obstacles))  # Output: 36
