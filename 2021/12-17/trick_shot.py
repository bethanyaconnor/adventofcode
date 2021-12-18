import sys

def process_tracectory(initialXVelocity, initialYVelocity, xMin, xMax, yMin, yMax):
    currentX = 0
    currentY = 0
    currentXVelocity = initialXVelocity
    currentYVelocity = initialYVelocity
    heighestHeight = 0
    while True:
        if currentX > xMax and currentXVelocity >= 0:
            return None
        if currentX < xMin and currentXVelocity <= 0:
            return None
        if currentY < yMin and currentYVelocity < 0:
            return None
        currentX += currentXVelocity
        currentY += currentYVelocity
        if currentXVelocity > 0:
            currentXVelocity -= 1
        elif currentXVelocity < 0:
            currentXVelocity += 1
        currentYVelocity -= 1
        if currentY > heighestHeight:
            heighestHeight = currentY
        if currentX >= xMin and currentX <= xMax and currentY >= yMin and currentY <= yMax:
           return heighestHeight
    return None

def part_1(xMin, xMax, yMin, yMax):
    maxHeight = 0
    for xVelocity in range(-2 * abs(xMax), 2 * abs(xMax)):
        for yVelocity in range(-2 * abs(yMax), 2 * abs(yMax)):
            height = process_tracectory(xVelocity, yVelocity, xMin, xMax, yMin, yMax)
            if height and height > maxHeight:
                maxHeight = height
    return maxHeight

def part_2(xMin, xMax, yMin, yMax):
    count = 0
    for xVelocity in range(-2 * abs(xMax), 2 * abs(xMax)):
        for yVelocity in range(-2 * abs(yMax), 2 * abs(yMax)):
            height = process_tracectory(xVelocity, yVelocity, xMin, xMax, yMin, yMax)
            if height != None:
                count += 1
    return count



xMin = int(sys.argv[1])
xMax = int(sys.argv[2])
yMin = int(sys.argv[3])
yMax = int(sys.argv[4])
if xMin > xMax:
    tmp = xMin
    xMin = xMax
    xMax = tmp
if yMin > yMax:
    tmp = yMin
    yMin = yMax
    yMax = yMin

print("Part 1: " + str(part_1(xMin, xMax, yMin, yMax)))
print("Part 2: " + str(part_2(xMin, xMax, yMin, yMax)))
