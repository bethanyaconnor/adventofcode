
@opponent_play_map = {
  'A' => 'rock',
  'B' => 'paper',
  'C' => 'scissors'
}

@my_play_map = {
  'X' => 'rock',
  'Y' => 'paper',
  'Z' => 'scissors'
}

@result_map = {
  'X' => 'lose',
  'Y' => 'draw',
  'Z' => 'win'
}

@move_score_map = {
  'rock' => 1,
  'paper' => 2,
  'scissors' => 3
}

def calculate_match_points(player1_play, player2_play)
  return [3, 3] if player1_play == player2_play
  if player1_play == 'rock'
    return [0,6] if player2_play == 'paper'
    return [6, 0]
  elsif player1_play == 'paper'
    return [0,6] if player2_play == 'scissors'
    return [6, 0]
  else
    return [0, 6] if player2_play == 'rock'
    return [6, 0]
  end
end

def determine_play_for_result(opponent_play, desired_result)
  return opponent_play if desired_result == 'draw'
  if desired_result == 'win'
    return 'scissors' if opponent_play == 'paper'
    return 'paper' if opponent_play == 'rock'
    return 'rock' if opponent_play == 'scissors'
  else
    return 'rock' if opponent_play == 'paper'
    return 'paper' if opponent_play == 'scissors'
    return 'scissors' if opponent_play == 'rock'
  end
end

def part_1
  my_points = 0
  File.foreach(ARGV[0]) do |line|
    split_string = line.strip.split(' ')
    opponent_play = @opponent_play_map[split_string[0]]
    my_play = @my_play_map[split_string[1]]
    my_points += @move_score_map[my_play]
    my_points += calculate_match_points(opponent_play, my_play)[1] 
  end
  my_points
end

def part_2
  my_points = 0
  File.foreach(ARGV[0]) do |line|
    split_string = line.strip.split(' ')
    opponent_play = @opponent_play_map[split_string[0]]
    my_play = determine_play_for_result(opponent_play, @result_map[split_string[1]])
    my_points += @move_score_map[my_play]
    my_points += calculate_match_points(opponent_play, my_play)[1]
  end
  my_points
end



puts "Part 1: #{part_1}"
puts "Part 2: #{part_2}"
