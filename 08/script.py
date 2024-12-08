def print_map(area):
	for line in area:
		print(''.join(line))


def is_in_area(area, row, col):
	if row >= 0 and row < len(area) and col >= 0 and col < len(area[0]):
		return True
	else:
		return False

def part_one(area):
	"""
	- List all different types of antennas, ie. different characters in the area.
	- For each type of antenna, find all pairs.
	- For each pair, compute the distance (deltaX, deltaY), and compute the antinodes.
		- if the result coordinate is out-of-bounds, drop it.
		- if the result coordinate overlaps an antenna, drop it.
		- the position of the antinode is a manipulation of deltaX and deltaY with some +/- signs.
	"""
	# List all antenna types
	antennas_types = set()
	for row in area:
		for col in row:
			antennas_types.add(col)
	antennas_types.remove('.')

	# Find coordinates of all atennas
	antennas_coordinates = {}
	for antenna in antennas_types:
		antennas_coordinates[antenna] = []
	for i, row in enumerate(area):
		for j, col in enumerate(row):
			if col in antennas_types:
				antennas_coordinates[col].append((i, j))

	antinodes_coordinates = set()
	for antenna in antennas_coordinates.keys():
		for k in range(len(antennas_coordinates[antenna])-1):
			for l in range(k+1, len(antennas_coordinates[antenna])):
				# Fetch coordinates of both antennas
				row_a = antennas_coordinates[antenna][k][0]
				col_a = antennas_coordinates[antenna][k][1]
				row_b = antennas_coordinates[antenna][l][0]
				col_b = antennas_coordinates[antenna][l][1]
				# print(f"Antennas {antenna}: ({row_a},{col_a}) and ({row_b},{col_b})")
				# Compute Manhattan's ditance between antennas
				delta_row = row_b - row_a
				delta_col = col_b - col_a
				# Compute position of both antinodes
				row_antinode_a = row_a - delta_row
				col_antinode_a = col_a - delta_col
				row_antinode_b = row_b + delta_row
				col_antinode_b = col_b + delta_col
				# print(f"Antinodes: ({row_antinode_a},{col_antinode_a}) and ({row_antinode_b},{col_antinode_b})")
				if is_in_area(area, row_antinode_a, col_antinode_a):
					antinodes_coordinates.add((row_antinode_a, col_antinode_a))
					if area[row_antinode_a][col_antinode_a] not in antennas_types:
						area[row_antinode_a][col_antinode_a] = '#'
				if is_in_area(area, row_antinode_b, col_antinode_b):
					antinodes_coordinates.add((row_antinode_b, col_antinode_b))
					if area[row_antinode_b][col_antinode_b] not in antennas_types:
						area[row_antinode_b][col_antinode_b] = '#'
	print(len(antinodes_coordinates))


def part_two(area):
	"""
	- List all different types of antennas, ie. different characters in the area.
	- For each type of antenna, find all pairs.
	- For each pair, compute the distance (deltaX, deltaY), and compute the antinodes.
		- if the result coordinate is out-of-bounds, drop it.
		- if the result coordinate overlaps an antenna, drop it.
		- the position of the antinode is a manipulation of deltaX and deltaY with some +/- signs.
		- keep going in a given direction while antinodes are in the map
	"""
	# List all antenna types
	antennas_types = set()
	for row in area:
		for col in row:
			antennas_types.add(col)
	antennas_types.remove('.')

	# Find coordinates of all atennas
	antennas_coordinates = {}
	for antenna in antennas_types:
		antennas_coordinates[antenna] = []
	for i, row in enumerate(area):
		for j, col in enumerate(row):
			if col in antennas_types:
				antennas_coordinates[col].append((i, j))

	# Each antenna is now an antinode spot as well
	antinodes_coordinates = set()
	for antenna in antennas_coordinates:
		for coord in antennas_coordinates[antenna]:
			antinodes_coordinates.add(coord)

	for antenna in antennas_coordinates.keys():
		for k in range(len(antennas_coordinates[antenna])-1):
			for l in range(k+1, len(antennas_coordinates[antenna])):
				# Fetch coordinates of both antennas
				row_a = antennas_coordinates[antenna][k][0]
				col_a = antennas_coordinates[antenna][k][1]
				row_b = antennas_coordinates[antenna][l][0]
				col_b = antennas_coordinates[antenna][l][1]
				# Compute Manhattan's ditance between antennas
				delta_row = row_b - row_a
				delta_col = col_b - col_a

				# First antinodes line
				while True:
					row_antinode_a = row_a - delta_row
					col_antinode_a = col_a - delta_col
					if is_in_area(area, row_antinode_a, col_antinode_a):
						antinodes_coordinates.add((row_antinode_a, col_antinode_a))
						if area[row_antinode_a][col_antinode_a] not in antennas_types:
							area[row_antinode_a][col_antinode_a] = '#'
					else:
						break
					row_a = row_antinode_a
					col_a = col_antinode_a

				# Second antinodes line
				while True:
					row_antinode_b = row_b + delta_row
					col_antinode_b = col_b + delta_col
					if is_in_area(area, row_antinode_b, col_antinode_b):
						antinodes_coordinates.add((row_antinode_b, col_antinode_b))
						if area[row_antinode_b][col_antinode_b] not in antennas_types:
							area[row_antinode_b][col_antinode_b] = '#'
					else:
						break
					row_b = row_antinode_b
					col_b = col_antinode_b
	print(len(antinodes_coordinates))
	print_map(area)




with open('input', 'r') as f:
	lines = f.readlines()
	lines = [list(line.strip()) for line in lines]

print_map(lines)
# part_one(lines)
part_two(lines)