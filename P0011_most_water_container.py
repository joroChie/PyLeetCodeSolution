'''
    Project Description
'''


def maxArea(height : [int]) -> [int]:
    if len(height) == 0:
        return 0
    if len(height) == 1:
        return height[0]

    max_area = 0
    curr_h = 0

    while curr_h < (len(height) - 1):
        movn_h = curr_h + 1
        while movn_h < len(height):
            area = min(height[curr_h], height[movn_h]) * (movn_h - curr_h)
            max_area = max(max_area, area)
            movn_h += 1
        curr_h += 1

    return max_area


def maxArea2(height : [int]) -> [int]:
    if len(height) == 0:
        return 0
    if len(height) == 1:
        return height[0]

    max_area = 0
    li = 0
    ri = len(height) - 1
    while li != ri:

        lh, rh = height[li], height[ri]

        if lh > rh:
            area = (ri - li) * rh
            ri -= 1
        else:
            area = (ri - li) * lh
            li += 1

        max_area = max(max_area, area)

    return max_area


if __name__ == '__main__':
    print(maxArea([1,8,6,2,3,4,8,3,7]))             # bruteforce
    print(maxArea2([1, 8, 6, 2, 3, 4, 8, 3, 7]))    # sliding window
    pass






