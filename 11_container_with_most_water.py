# 11. Container With Most Water

# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, 
# such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.


def containerWithMostWater(height):
    n = len(height)
    l = 0
    r = n - 1
    max_width = n - 1
    area = 0

    for width in range(max_width, 0, -1):
        if height[l] < height[r]:
            area = max(area, width * height[l])
            l += 1
        else:
            area = max(area, width * height[r])
            r -= 1

    return area


def maxArea_brute_force(height):
    n = len(height)
    area = 0
    for l in range(0,n - 1):
        for r in range(l + 1, n):
            area = max(area, (r - l) * min(height[l], height[r]))

    return area
    