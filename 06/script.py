from itertools import cycle

def print_map(area):
	for line in area:
		print(''.join(line))

def find_guard(area):
	for i in range(len(area)):
		for j in range(len(area[0])):
			if area[i][j] == "^":
				return (i, j)

def move_guard(position, direction):
	if direction == "up":
		return position[0]-1, position[1]
	elif direction == "right":
		return position[0], position[1]+1
	elif direction == "down":
		return position[0]+1, position[1]
	elif direction == "left":
		return position[0], position[1]-1
	else:
		print(f"Unsupported direction '{direction}'")

def is_guard_in_map(position, area):
	"""
	Check if the guard is still within the boundaries of the map.
	"""
	if position[0] >= 0 and position[0] < len(area) and position[1] >= 0 and position[1] < len(area[0]):
		return True
	else:
		return False

def part_one(area):
	x, y = find_guard(area)
	# print(x, y)
	lst = ["up", "right", "down", "left"]
	directions = cycle(lst)
	# The guard starts facing up
	cur_dir = next(directions)
	guard_position = find_guard(area)
	while True:
		area[guard_position[0]][guard_position[1]] = "X"
		new_position = move_guard(guard_position, cur_dir)
		if not is_guard_in_map(new_position, area):
			break
		if area[new_position[0]][new_position[1]] == "#":
			cur_dir = next(directions)
		else:
			guard_position = new_position
	# print_map(area)
	count = 0
	for line in area:
		count += line.count('X')
	return count, area

def extract_candidates(area):
	candidates = []
	for i in range(len(area)):
		for j in range(len(area[0])):
			if area[i][j] == 'X':
				candidates.append((i,j))
	return candidates

def reset_area(area, guard):
	for i in range(len(area)):
		for j in range(len(area[0])):
			if area[i][j] == 'X' or area[i][j] == 'O':
				area[i][j] = '.'
	area[guard[0]][guard[1]] = '^'
	return area

def obstacle_causes_loop(area):
	"""
	If we loop, return True, False otherwise.
	"""
	max_steps = len(area)*len(area[0])
	lst = ["up", "right", "down", "left"]
	directions = cycle(lst)
	# The guard starts facing up
	cur_dir = next(directions)
	guard_position = find_guard(area)
	steps = 0
	while steps < max_steps:
		area[guard_position[0]][guard_position[1]] = "X"
		new_position = move_guard(guard_position, cur_dir)
		if not is_guard_in_map(new_position, area):
			return False
		if area[new_position[0]][new_position[1]] in ['#', 'O']:
			cur_dir = next(directions)
		else:
			guard_position = new_position
			steps += 1
	return True



def part_two(area):
	"""
	Run part one to generate the path of the guard.
	Obstacle should only be tested on his path, they do not make any sense
	where they do not walk -> only 4602 possibilities.

	To detect a loop, I'll just count the steps taken.
	If they're above a set threshold, we consider the guard must be walking
	in circles.
	Let's set this threshold to the amount of squares on the map: 17161
	"""
	guard_position_original = find_guard(area)
	candidates = extract_candidates(part_one(area)[1])
	# Remove the guard starting position from the list
	del candidates[candidates.index(guard_position_original)]
	count = 0
	for candidate in candidates:
		area = reset_area(area, guard_position_original)
		# Place the obstacle
		area[candidate[0]][candidate[1]] = 'O'
		if obstacle_causes_loop(area):
			count += 1
	print(count)
		
	


with open('input', 'r') as f:
	lines = f.readlines()
	lines = [list(line.strip()) for line in lines]

# print_map(lines)
# print(part_one(lines)[0])
part_two(lines)