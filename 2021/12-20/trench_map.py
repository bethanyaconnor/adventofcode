import sys

def process_image(algorithm, prev_image, iteration):
    default = '.'
    if algorithm[0] == '#' and algorithm[-1] == '.':
        if iteration % 2 == 1:
            default = '#'
    padded_image = []
    padded_image.append([default]*(len(prev_image[0]) + 2))
    for i in range(len(prev_image)):
        row = prev_image[i].copy()
        row.insert(0, default)
        row.append(default)
        padded_image.append(row)
    padded_image.append([default]*(len(prev_image[0]) + 2))
    processed_image = []
    for i in range(len(padded_image)):
        processed_row = []
        for j in range(len(padded_image[0])):
            binary_index = []
            binary_index.append(padded_image[i - 1][j - 1] if i > 0 and j > 0 else default)
            binary_index.append(padded_image[i - 1][j] if i > 0 else default)
            binary_index.append(padded_image[i - 1][j + 1] if i > 0 and j < len(padded_image[0]) - 1 else default)
            binary_index.append(padded_image[i][j - 1] if j > 0 else default)
            binary_index.append(padded_image[i][j])
            binary_index.append(padded_image[i][j + 1] if j < len(padded_image[0]) - 1 else default)
            binary_index.append(padded_image[i + 1][j - 1] if i < len(padded_image) - 1 and j > 0 else default)
            binary_index.append(padded_image[i + 1][j] if i < len(padded_image) - 1 else default)
            binary_index.append(padded_image[i + 1][j + 1] if i < len(padded_image) - 1 and j < len(padded_image[0]) - 1 else default)
            for c in range(len(binary_index)):
                if binary_index[c] == '.':
                    binary_index[c] = '0'
                else:
                    binary_index[c] = '1'
            processed_row.append(algorithm[int(''.join(binary_index), 2)])
        processed_image.append(processed_row)
    return processed_image

def part_1(algorithm, start_image):
    image = start_image
    for i in range(2):
        image = process_image(algorithm, image, i)
    lit_pixels = 0
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == '#':
                lit_pixels += 1
    return lit_pixels

def part_2(algorithm, start_image):
    image = start_image
    for i in range(50):
        image = process_image(algorithm, image, i)
    lit_pixels = 0
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == '#':
                lit_pixels += 1
    return lit_pixels



f = open(sys.argv[1], 'r')
algorithm = f.readline().strip()
f.readline()
image = []
for x in f:
    image.append(list(x.strip()))

print("Part 1: " + str(part_1(algorithm, image)))
print("Part 2: " + str(part_2(algorithm, image)))
