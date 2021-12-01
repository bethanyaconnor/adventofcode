
def parseInput(input)
  regex = /(\d+)-(\d+) ([a-z]): ([a-z]+)/
  match = regex.match(input)
  {first: match[1].to_i, second: match[2].to_i, letter: match[3], password: match[4]}
end

def checkPassword(params)
  matches_first = 
  (params[:password][params[:first] - 1] == params[:letter]) ^ (params[:password][params[:second] - 1] == params[:letter])
end

valid_passwords = 0
File.readlines('input.txt').each do |line|
  params = parseInput(line)
  valid_passwords += 1 if checkPassword(params)
end
puts valid_passwords
