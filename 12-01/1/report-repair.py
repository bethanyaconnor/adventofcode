def find_2020_pair(numbers):
    for x in range(0, len(numbers)):
        for y in range(len(numbers) - 1, x, -1):
            if numbers[x] + numbers[y] == 2020:
                print(numbers[x], numbers[y])
                return numbers[x] * numbers[y]
            if numbers[x] + numbers[y] < 2020:
                break

f = open("input.txt", "r")
numbers = []
for x in f:
    numbers.append(int(x))
numbers.sort()
print(find_2020_pair(numbers))
