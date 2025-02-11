import random
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Uniformly select an upper and lower bound between 1 and 100,000
lower_bound = 1
numbers =[]
for i in range(500):
    upper_bound = random.randint(lower_bound, 100000)

# Step 2: Generate 10,000 random numbers between the selected bounds
    numbers += [random.uniform(lower_bound, upper_bound) for _ in range(10000)]

# Step 3: Extract the first digit of each number
first_digits = [int(str(int(num))[0]) for num in numbers]

# Step 4: Plot the histogram of the first digits
plt.hist(first_digits, bins=np.arange(1, 11)-0.5, edgecolor='black', align='mid')
plt.xticks(range(1, 10))
plt.xlabel("First Digit")
plt.ylabel("Frequency")
plt.title(f"Histogram of First Digits for 10,000 Random Numbers\nRange: {lower_bound} to {upper_bound}")
plt.show()