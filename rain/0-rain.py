#!/usr/bin/python3
"""
rainwater module

This module provides a method to calculate the total amount
of rainwater retained based on the heights of walls in a relief map.

"""


def rain(walls):
    """
    Calculates the total amount of rainwater retained based on the heights
    of walls.

    Parameters:
        walls (list): A list of non-negative integers representing the
        heights of walls.

    Returns:
        int: The total amount of rainwater retained.

    """

    if not walls:
        return 0

    total_water = 0
    left_max = [0] * len(walls)
    right_max = [0] * len(walls)

    # Calculate the maximum height of walls to the left of each wall
    left_max[0] = walls[0]
    for i in range(1, len(walls)):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Calculate the maximum height of walls to the right of each wall
    right_max[-1] = walls[-1]
    for i in range(len(walls) - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate the amount of water retained at each wall
    for i in range(len(walls)):
        water_height = min(left_max[i], right_max[i]) - walls[i]
        total_water += max(water_height, 0)

    return total_water
