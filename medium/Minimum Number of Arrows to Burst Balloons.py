# Alogrithm
"""
    1- Sort ballons' points due to end coordinate.
    2- Intialize arrows value to 1 and keep track of the number.
    3- Intialize end value to the first ballon end coordinate.
    4- Looping on ballons starting from the second one
        A- Check if the current ballon start coordinate is greater than the last one end
        B- If (True) this means that this ballon is not overlapping the last one
            so we need a new arrow
        C- Upate the end to the current ballon end coordinate 
"""

# Implementation
def findMinArrowShots(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    points.sort(key=lambda p: p[1])
    arrows = 1
    end = points[0][1]

    for ballon in points[1:]:
        if ballon[0] > end:
            arrows += 1
            end = ballon[1]

    return arrows

# Test Cases
t1 = [[10,16],[2,8],[1,6],[7,12]] # res = 2
t2 = [[1,2],[3,4],[5,6],[7,8]] # res = 4
t3 = [[1,2],[2,3],[3,4],[4,5]] # res = 2
t4 = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]] # res = 2

print(findMinArrowShots(t1))
print(findMinArrowShots(t2))
print(findMinArrowShots(t3))
print(findMinArrowShots(t4))