from typing import List


def countFrequency(n: int, m: int, edges: List[int]):
    # Initialize an array to store frequencies, initialized with zeros
    array = [0] * (m + 1)

    # Count the frequencies of elements in the edges list
    for edge in edges:
        if 1 <= edge <= m:  # Check if the value is within range
            array[edge] += 1

    # Initialize a list to store the frequencies of values up to n
    frequency = [0] * (n + 1)

    # Populate the frequencies for values up to n
    for i in range(1, n + 1):
        if i <= m:  # Check if the value is within range
            frequency[i] = array[i]

    return frequency[1:]


n, m = 6, 4
edges = [1, 3, 4, 3, 4, 1]
print(countFrequency(n, m, edges))  # [
