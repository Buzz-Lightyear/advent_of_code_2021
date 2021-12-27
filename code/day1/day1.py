def count_increases():
  prev = 10000
  result = 0
  with open("input.txt") as file:
      for line in file:
          reading = int(line.rstrip())
          if reading > prev:
            result += 1
          prev = reading

  return result

def sliding_window():
  prev1 = None
  prev2 = None
  prev3 = None
  result = 0
  index = 0
  
  with open("input.txt") as file:
    for line in file:
      reading = int(line.rstrip())
      if index == 0:
        prev1 = reading
      elif index == 1:
        prev2 = prev1
        prev1 = reading
      elif index == 2:
        prev3 = prev2
        prev2 = prev1
        prev1 = reading
      else:
          if reading > min(prev1, prev2, prev3):
            result += 1
          prev3 = prev2
          prev2 = prev1
          prev1 = reading
           
      index += 1
  return result

def sliding_window_inefficient():
	with open("input.txt", "r") as f:
		inp = [int(x.rstrip()) for x in f.readlines()]

	prev_sum = sum(inp[0:3])
	
	count = 0
	i = 1
	while i+2 < len(inp):
		curr_sum = sum(inp[i:i+3])
		if sum(inp[i:i+3]) > prev_sum:
			count += 1
		prev_sum = curr_sum
		i += 1
	return count

if __name__ == '__main__':
  print(sliding_window_inefficient())