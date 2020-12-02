
def parseInput(input)
  regex = /(\d+)-(\d+) ([a-z]): ([a-z]+)/
  match = regex.match(input)
  {min: match[1].to_i, max: match[2].to_i, letter: match[3], password: match[4]}
end

def checkPassword(params)
  num_occurences = params[:password].scan(/#{params[:letter]}/).count
  return num_occurences >= params[:min] && num_occurences <= params[:max]
end

valid_passwords = 0
File.readlines('input.txt').each do |line|
  params = parseInput(line)
  valid_passwords += 1 if checkPassword(params)
end
puts valid_passwords
