"""
Kairu Cyrus
SCT211-0024/2021
"""
import random
from tabulate import tabulate

# Number of rolls
num_rolls = 1000

# Initialize face counts
face_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
"""
Initialize a dictionary face_counts to keep track of 
the counts of each face of the die. Each face is represented by a 
number from 1 to 6, and initially, all counts are set to 0.
"""

for i in range(num_rolls):
    # Generate a random value between 0 and 1
    x = random.random()

    # Determine which face the value corresponds to
    #lower bound not included
    if 0 <= x < 1/6:
        face_counts[1] += 1
    elif 1/6 <= x < 2/6:
        face_counts[2] += 1
    elif 2/6 <= x < 3/6:
        face_counts[3] += 1
    elif 3/6 <= x < 4/6:
        face_counts[4] += 1
    elif 4/6 <= x < 5/6:
        face_counts[5] += 1
    else:
        face_counts[6] += 1

# Calculate percentages
percentages = [count / num_rolls * 100 for count in face_counts.values()]

# Prepare data for tabulate
table_data = zip(face_counts.keys(), face_counts.values(), percentages)

# Print tabulated data
print(tabulate(table_data, headers=["Face", "Rolls", "Percentage"], floatfmt=".2f", tablefmt="grid"))


