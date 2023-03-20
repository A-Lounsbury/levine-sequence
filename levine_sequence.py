# levine_sequence.py
# Andrew Lounsbury
# 20/2/23
# Purpose: generate the levine sequence; https://www.youtube.com/watch?v=KNjPPFyEeLo
triangle = [[2]]
sequence = []

def generate_triangle(triangle, n):
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

def generate_sequence(triangle, sequence, n):
    generate_triangle(triangle, n)
    for level in triangle:
        total = 0
        for num in level:
            total += num
        sequence.append(total)

generate_sequence(triangle, sequence, 12)
print(sequence)