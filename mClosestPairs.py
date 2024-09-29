import math

def calculateDist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def findDistance(Px):
    pairs = []
    for i in range(len(Px)):
        for j in range (i + 1, (len(Px))):
            distance = calculateDist(Px[i], Px[j])
            pairs.append((Px[i], Px[j], distance))
    return pairs

def combineSort(left, right, center, m):
    combined = left + right + center

    # Sort by distance
    combined.sort(key=lambda x: x[2])

    return combined[:m]

def findDistanceAcrossLines(left, right):
    pairs = []
    for l in left:
        for r in right:
            distance = calculateDist(l, r)
            pairs.append((l, r, distance))
    return pairs

def getPossibleMidPoints(left, right, midPoint, delta):
    leftPossible = [point for point in left if abs(point[0] - midPoint[0]) < delta]
    rightPossible = [point for point in right if abs(point[0] - midPoint[0]) < delta]

    possible = findDistanceAcrossLines(leftPossible, rightPossible)

    return possible

def closestRecursive(Px, m):
    lenPx = len(Px)

    # Base case if all possible pair nums less than or euql to m, all possible are closest m pairs
    if math.comb(lenPx, 2) <= m:
        return findDistance(Px)

    # Recursive
    # Split left and right
    mid = lenPx // 2
    left = Px[:mid]
    right = Px[mid:]

    # find closest m pairs on left and right side
    leftPairs = closestRecursive(left, m)
    rightPairs = closestRecursive(right, m)

    combined = combineSort(leftPairs, rightPairs, [], m)

    # get points that are close enought to center, there may be closer points across midpoint line
    delta = combined[-1][-1]
    midPoint = Px[mid]
    midPairs = getPossibleMidPoints(left, right, midPoint, delta)

    combined = combineSort(leftPairs, rightPairs, midPairs, m)

    return combined

def closestPairs(P, m):
    # Sort points by x-coordinate
    Px = sorted(P, key=lambda p: p[0])  

    return closestRecursive(Px, m)

if __name__ == "__main__":
    # Define a set of points in the 2D plane
    points = [(0, 0), (12, 30), (40, 50), (1, 2), (2, 5), (3, 4), (5, 2), (3, 7)]
    m = 7  # Number of closest pairs to find
    print(f"Total possible pairs with {len(points)} points: {math.comb(len(points), 2)}")

    result = closestPairs(points, m)
    
    # Print the m closest pairs and their distances
    for p1, p2, dist in result:
        print(f"Pair: {p1}, {p2}, Distance: {dist:.4f}")