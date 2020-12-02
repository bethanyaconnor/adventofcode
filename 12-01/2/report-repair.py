def find_2020_pair(numbers):
    for x in range(0, len(numbers)):
        for y in range(x+1, len(numbers)):
            for z in range(len(numbers) - 1, y, -1):
                if numbers[x] + numbers[y] + numbers[z] == 2020:
                    print(numbers[x], numbers[y], numbers[z])
                    return numbers[x] * numbers[y] * numbers[z]
                if numbers[x] + numbers[y] + numbers[z] < 2020:
                    break

f = open("input.txt", "r")
numbers = []
for x in f:
    numbers.append(int(x))
numbers.sort()
print(find_2020_pair(numbers))
