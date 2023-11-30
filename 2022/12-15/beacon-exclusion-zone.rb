class Sensor
  attr_accessor :loc, :coverage_dist

  def initialize(loc, beacon_loc)
    @loc = loc
    @coverage_dist = (loc[0] - beacon_loc[0]).abs + (loc[1] - beacon_loc[1]).abs
    @beacon_loc = beacon_loc
  end

  def point_covered?(point)
    (@loc[0] - point[0]).abs + (@loc[1] - point[1]).abs <= coverage_dist
  end
end

beacons = []
sensors = []
sensor_positions = []

min_x_possibly_covered = Float::INFINITY
max_x_possibly_covered = 0
File.readlines(ARGV[0]).each do |line|
  split_line = line.strip.split(' ')
  sensor_x = split_line[2][0...-1].split('=')[1].to_i
  sensor_y = split_line[3][0...-1].split('=')[1].to_i
  beacon_x = split_line[8][0...-1].split('=')[1].to_i
  beacon_y = split_line[9].split('=')[1].to_i

  beacons.append([beacon_x, beacon_y])
  sensor = Sensor.new([sensor_x, sensor_y], [beacon_x, beacon_y])
  sensors.append(sensor)

  min_x_possibly_covered = [min_x_possibly_covered, beacon_x, sensor_x - sensor.coverage_dist].min
  max_x_possibly_covered = [max_x_possibly_covered, beacon_x, sensor_x + sensor.coverage_dist].max
end

beacons = beacons.uniq

y_value_to_inspect = 2000000
known_beaconless = 0
(min_x_possibly_covered..max_x_possibly_covered).each do |x|
  next if beacons.include?([x, y_value_to_inspect])
  sensors.each do |sensor|
    if sensor.point_covered?([x, y_value_to_inspect])
      #puts "#{x},#{y_value_to_inspect} is covered"
      known_beaconless += 1
      break
    end
  end
end
puts "Part 1: #{known_beaconless}"

def find_beacon(min_x, max_x, min_y, max_y, sensors, beacons)
  puts "Searching in #{min_x} to #{max_x}"
  (min_x..max_x).each do |x|
    (min_y..max_y).each do |y|
      next if beacons.include?([x, y])
      next if sensors.any? {|s| s.point_covered?([x, y]) }
      puts "Part 2: #{x * 4000000 + y}"
      return
    end
  end
  puts "Finished searching in #{min_x} to #{max_x}"
end

max_xy = 4000000
#max_xy = 20
num_threads = 100
chunk_size = max_xy/num_threads
threads = []

(1..num_threads).each do |thread_num|
  threads << Thread.new { find_beacon(((thread_num-1) * chunk_size), (thread_num * chunk_size), 0, max_xy, sensors, beacons) }
end

#threads << Thread.new { find_beacon(0, 500000, 0, max_xy, sensors, beacons) }
#threads << Thread.new { find_beacon(500001, 1000000, 0, max_xy, sensors, beacons) }
#threads << Thread.new { find_beacon(10000001, 1500000, 0, max_xy, sensors, beacons) }
#threads << Thread.new { find_beacon(1500001, 2000000, 0, max_xy, sensors, beacons) }
#threads << Thread.new { find_beacon(2000000, 2500000, 0, max_xy, sensors, beacons) }
#threads << Thread.new { find_beacon(2500001, 3000000, 0, max_xy, sensors, beacons) }
#threads << Thread.new { find_beacon(3000001, 3500000, 0, max_xy, sensors, beacons) }
#threads << Thread.new { find_beacon(3500001, 4000000, 0, max_xy, sensors, beacons) }
threads.each(&:join)
