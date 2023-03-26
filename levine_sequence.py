# levine_sequence.py
# Andrew Lounsbury
# 20/2/23
# Purpose: generate the levine sequence; https://www.youtube.com/watch?v=KNjPPFyEeLo

import math
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def generate_triangle(n):
    triangle = [[2]]
    while len(triangle) < n:
        new_level = []
        curLevel = triangle[len(triangle) - 1]
        curLevel.reverse()
        val = 1
        for num in curLevel:
            for i in range(num):
                new_level.append(val)
            val += 1
        triangle.append(new_level)
        curLevel.reverse()
    return triangle

def generate_levine(n):
    triangle = []
    triangle = generate_triangle(n)
    sequence = []
    for level in triangle:
        total = 0
        for num in level:
            total += num
        sequence.append(total)
    return sequence

n = 12
sequence = generate_levine(n)
print(sequence)
log_sequence = []
for s in sequence:
    log_sequence.append(math.log(s))
print(log_sequence)
df = pd.DataFrame(log_sequence, columns=["Number"]) 
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y="Number", data=df)
plt.show()
