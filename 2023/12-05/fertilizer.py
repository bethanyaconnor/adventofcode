import sys
sys.path.append('2023')
from util import print_solution

def part_1(file_name):
  f = open(file_name, 'r')
  seeds = f.readline().strip()[6:].strip().split()
  print(str(seeds))
  f.readline() # skip blank line

  soil_numbers = []
  for seed in seeds:
    soil_numbers.append(int(seed))
  f.readline() # skip seed-to-soil map header
  next_line = f.readline().strip()
  while next_line != '':
    [dest_start, source_start, length] = next_line.split()
    for idx, seed in enumerate(seeds):
      if int(seed) >= int(source_start) and int(seed) < int(source_start) + int(length):
        soil_numbers[idx] = int(dest_start) + (int(seed) - int(source_start))
    next_line = f.readline().strip()
  print("soil: " + str(soil_numbers))

  fertilizer_values = []
  for soil_num in soil_numbers:
    fertilizer_values.append(soil_num)
  f.readline() # skip fertilizer-to-soil map header
  next_line = f.readline().strip()
  while next_line != '':
    [dest_start, source_start, length] = next_line.split()
    for idx, soil_num in enumerate(soil_numbers):
      if int(soil_num) >= int(source_start) and int(soil_num) < int(source_start) + int(length):
        fertilizer_values[idx] = int(dest_start) + (int(soil_num) - int(source_start))
    next_line = f.readline().strip()
  print("fertilizer: " + str(fertilizer_values))

  water_values = []
  for fertilizer_val in fertilizer_values:
    water_values.append(fertilizer_val)
  f.readline() # skip water-to-fertilizer map header
  next_line = f.readline().strip()
  while next_line != '':
    [dest_start, source_start, length] = next_line.split()
    for idx, soil_num in enumerate(fertilizer_values):
      if int(soil_num) >= int(source_start) and int(soil_num) < int(source_start) + int(length):
        water_values[idx] = int(dest_start) + (int(soil_num) - int(source_start))
    next_line = f.readline().strip()
  print("water: " + str(water_values))

  light_values = []
  for water_value in water_values:
    light_values.append(water_value)
  f.readline() # skip light-to-water map header
  next_line = f.readline().strip()
  while next_line != '':
    [dest_start, source_start, length] = next_line.split()
    for idx, water_value in enumerate(water_values):
      if int(water_value) >= int(source_start) and int(water_value) < int(source_start) + int(length):
        light_values[idx] = int(dest_start) + (int(water_value) - int(source_start))
    next_line = f.readline().strip()
  print(str(light_values))

  temperature_values = []
  for light_value in light_values:
    temperature_values.append(light_value)
  f.readline() # skip temperature-to-light map header
  next_line = f.readline().strip()
  while next_line != '':
    [dest_start, source_start, length] = next_line.split()
    for idx, light_value in enumerate(light_values):
      if int(light_value) >= int(source_start) and int(light_value) < int(source_start) + int(length):
        temperature_values[idx] = int(dest_start) + (int(light_value) - int(source_start))
    next_line = f.readline().strip()
  print(str(temperature_values))

  humidity_values = []
  for temperature_value in temperature_values:
    humidity_values.append(temperature_value)
  f.readline() # skip humidity-to-temperature map header
  next_line = f.readline().strip()
  while next_line != '':
    [dest_start, source_start, length] = next_line.split()
    for idx, temperature_value in enumerate(temperature_values):
      if int(temperature_value) >= int(source_start) and int(temperature_value) < int(source_start) + int(length):
        humidity_values[idx] = int(dest_start) + (int(temperature_value) - int(source_start))
    next_line = f.readline().strip()
  print(str(humidity_values))

  location_values = []
  for humidity_value in humidity_values:
    location_values.append(humidity_value)
  f.readline() # skip location-to-humidity map header
  next_line = f.readline().strip()
  while next_line != '':
    [dest_start, source_start, length] = next_line.split()
    for idx, humidity_value in enumerate(humidity_values):
      if int(humidity_value) >= int(source_start) and int(humidity_value) < int(source_start) + int(length):
        location_values[idx] = int(dest_start) + (int(humidity_value) - int(source_start))
    next_line = f.readline().strip()
  print(str(location_values))

  print_solution(1, min(location_values))
  
  

  

def part_2(file_name):
  f = open(file_name, 'r')
  seeds = f.readline().strip()[6:].strip().split()
  print(str(seeds))
  f.readline() # skip blank line

  soil_numbers = []
  for i in range(0, len(seeds),2):
    for j in range(int(seeds[i]), int(seeds[i]) + int(seeds[i+1])):
      soil_numbers.append(j)
  print("initial_soil: " + str(soil_numbers))
  f.readline() # skip seed-to-soil map header
  next_line = f.readline().strip()
  while next_line != '':
    [dest_start, source_start, length] = next_line.split()
    for idx, seed in enumerate(seeds):
      if int(seed) >= int(source_start) and int(seed) < int(source_start) + int(length):
        soil_numbers[idx] = int(dest_start) + (int(seed) - int(source_start))
    next_line = f.readline().strip()
  print("soil: " + str(soil_numbers))

  fertilizer_values = []
  for soil_num in soil_numbers:
    fertilizer_values.append(soil_num)
  f.readline() # skip fertilizer-to-soil map header
  next_line = f.readline().strip()
  while next_line != '':
    [dest_start, source_start, length] = next_line.split()
    for idx, soil_num in enumerate(soil_numbers):
      if int(soil_num) >= int(source_start) and int(soil_num) < int(source_start) + int(length):
        fertilizer_values[idx] = int(dest_start) + (int(soil_num) - int(source_start))
    next_line = f.readline().strip()
  print("fertilizer: " + str(fertilizer_values))

  water_values = []
  for fertilizer_val in fertilizer_values:
    water_values.append(fertilizer_val)
  f.readline() # skip water-to-fertilizer map header
  next_line = f.readline().strip()
  while next_line != '':
    [dest_start, source_start, length] = next_line.split()
    for idx, soil_num in enumerate(fertilizer_values):
      if int(soil_num) >= int(source_start) and int(soil_num) < int(source_start) + int(length):
        water_values[idx] = int(dest_start) + (int(soil_num) - int(source_start))
    next_line = f.readline().strip()
  print("water: " + str(water_values))

  light_values = []
  for water_value in water_values:
    light_values.append(water_value)
  f.readline() # skip light-to-water map header
  next_line = f.readline().strip()
  while next_line != '':
    [dest_start, source_start, length] = next_line.split()
    for idx, water_value in enumerate(water_values):
      if int(water_value) >= int(source_start) and int(water_value) < int(source_start) + int(length):
        light_values[idx] = int(dest_start) + (int(water_value) - int(source_start))
    next_line = f.readline().strip()
  print(str(light_values))

  temperature_values = []
  for light_value in light_values:
    temperature_values.append(light_value)
  f.readline() # skip temperature-to-light map header
  next_line = f.readline().strip()
  while next_line != '':
    [dest_start, source_start, length] = next_line.split()
    for idx, light_value in enumerate(light_values):
      if int(light_value) >= int(source_start) and int(light_value) < int(source_start) + int(length):
        temperature_values[idx] = int(dest_start) + (int(light_value) - int(source_start))
    next_line = f.readline().strip()
  print(str(temperature_values))

  humidity_values = []
  for temperature_value in temperature_values:
    humidity_values.append(temperature_value)
  f.readline() # skip humidity-to-temperature map header
  next_line = f.readline().strip()
  while next_line != '':
    [dest_start, source_start, length] = next_line.split()
    for idx, temperature_value in enumerate(temperature_values):
      if int(temperature_value) >= int(source_start) and int(temperature_value) < int(source_start) + int(length):
        humidity_values[idx] = int(dest_start) + (int(temperature_value) - int(source_start))
    next_line = f.readline().strip()
  print(str(humidity_values))

  location_values = []
  for humidity_value in humidity_values:
    location_values.append(humidity_value)
  f.readline() # skip location-to-humidity map header
  next_line = f.readline().strip()
  while next_line != '':
    [dest_start, source_start, length] = next_line.split()
    for idx, humidity_value in enumerate(humidity_values):
      if int(humidity_value) >= int(source_start) and int(humidity_value) < int(source_start) + int(length):
        location_values[idx] = int(dest_start) + (int(humidity_value) - int(source_start))
    next_line = f.readline().strip()
  print(str(location_values))

  print_solution(1, min(location_values))
 

  pass

file_name = sys.argv[1]
part_1(file_name)
part_2(file_name)