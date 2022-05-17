# 1762. Buildings With an Ocean View


# There are n buildings in a line. You are given an integer array heights of size n 
# that represents the heights of the buildings in the line.
# The ocean is to the right of the buildings. 
# A building has an ocean view if the building can see the ocean without obstructions. 
# Formally, a building has an ocean view if all the buildings to its right have a smaller height.
# Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.


def findBuildings(heights):
    n = len(heights)
    answer = []

    for current in range(n):
        # If the current building is taller, 
        # it will block the shorter building's ocean view to its left.
        # So we pop all the shorter buildings that have been added before.
        while answer and heights[answer[-1]] <= heights[current]:
            answer.pop()
        answer.append(current)
        
    return answer
    