import random

# Function to display the room
def display(room):
    for row in room:
        print(row)

# Initialize the room as a 4x4 grid, all elements set to 1 (dirty)
room = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]

print("All the rooms are dirty")
display(room)

# Randomly dirty some rooms (0 = clean, 1 = dirty)
x = 0
y = 0

while x < 4:
    while y < 4:
        room[x][y] = random.choice([0, 1])
        y += 1
    x += 1
    y = 0

print("\nBefore cleaning, the room has random dirt:")
display(room)

# Initialize counters
x = 0
y = 0
z = 0  # Number of cleaned cells

# Cleaning process
while x < 4:
    while y < 4:
        if room[x][y] == 1:
            print(f"Vacuum in this location now: ({x}, {y})")
            room[x][y] = 0
            print(f"Cleaned: ({x}, {y})")
            z += 1
        y += 1
    x += 1
    y = 0

# Calculate performance
performance = (100 - ((z / 16) * 100))

print("\nRoom is clean now. Thanks for using the Robot Vacuum Cleaner!")
display(room)
print("Performance =", performance, "%")
