trail_values = [i for i in range(10)]
direction_shifts = [(-1,0), (0,1), (1,0), (0,-1)]

def print_map(lines):
	for line in lines:
		print(''.join([str(i) for i in line]))

def is_within_bounds(row, col, area):
	return row >= 0 and row < len(area) and col >= 0 and col < len(area[0])

def advance_trail(start, area, trail_ends, previous_val=-1):
	"""
	- Check the current value
	- Look around for the next value in trail_values
	- If available, return a call to advance_trail at that position
	- If end of trail, return True and add coordinates to trail_ends
	"""
	row = start[0]
	col = start[1]
	# print(f"Set: {trail_ends}")
	if is_within_bounds(row, col, area):
		value = area[row][col]
		if value == previous_val + 1:
			# print(f"At ({row},{col}), value: {value}")
			if value == trail_values[-1]:
				trail_ends.add((row, col))
				# print(f"Set: {trail_ends}")
				return 

			for dir_shift in direction_shifts:
				next_row = row + dir_shift[0]
				next_col = col + dir_shift[1]
				# print(f"Look at ({next_row},{next_col})")
				advance_trail((next_row, next_col), area, trail_ends, value)
		else:
			return 
	else:
		return 



def part_one(area):
	"""
	- Locate each trail head.
	- For each trail head, look in each of the four directions if the next step is available.
		-> This calls a function looking for the next step, returning True for a complete trail
	"""
	score = 0
	for row in range(len(area)):
		for col in range(len(area[0])):
			value = area[row][col]
			if value == 0:
				trail_ends = set()
				advance_trail((row, col), area, trail_ends)
				score += len(trail_ends)
	print(f"Score: {score}")

def advance_trail_rating(start, area, rating, previous_val=-1):
	row = start[0]
	col = start[1]
	if is_within_bounds(row, col, area):
		value = area[row][col]
		if value == previous_val + 1:
			if value == trail_values[-1]:
				rating += 1
				# print(f"End of trail, current rating: {rating}")
				return rating

			for dir_shift in direction_shifts:
				next_row = row + dir_shift[0]
				next_col = col + dir_shift[1]
				rating = advance_trail_rating((next_row, next_col), area, rating, value)
				# print(f"Next dir. Rating: {rating}")
		else:
			# print(f"Wrong slope, stop. Rating: {rating}")
			return rating
	else:
		# print(f"Out of bound, stop. Rating: {rating}")
		return rating
	return rating


def part_two(area):
	score = 0
	for row in range(len(area)):
		for col in range(len(area[0])):
			value = area[row][col]
			if value == 0:
				rating = 0
				rating = advance_trail_rating((row, col), area, rating)
				# print(f"start at ({row},{col}), rating {rating}")
				score += rating
	print(f"Score: {score}")



with open('input', 'r') as f:
	lines = f.readlines()
	lines = [list(map(int,list(line.strip()))) for line in lines]

print_map(lines)
# part_one(lines)
part_two(lines)
