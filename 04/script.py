XMAS = "XMAS"
XMAS_cnt = 0
directions = ["NW", "N", "NE", "W", "C", "E", "SW", "S", "SE"]
dir_shift = {	"NW":(-1,-1), "N":(-1,0), "NE":(-1,1),
				"W":(0,-1), "C":(0,0), "E":(0,1),
				"SW":(1,-1), "S":(1,0), "SE":(1,1)}

cross_directions = ["NW", "NE", "SW", "SE"]
dir_opposite = {"NW":"SE", "NE":"SW", "SW":"NE", "SE":"NW"}

def lookaround(lines, letter, i, j, xmas_idx, direction=""):
	"""
	Look all around the 'X', if we find an 'M', start looking
	for the next one in the same direction.
	"""
	global XMAS_cnt
	# print(f"Looking around for letter {letter}")
	if letter == "M":
		d = 0
		for k in range(i-1, i+2):
			for l in range(j-1, j+2):
				# print(f"Looking at coordinates ({k},{l})")
				if k >= 0 and k < len(lines) and l >= 0 and l < len(lines[0]):
					# print(f"Checking letter {lines[k][l]}")
					if lines[k][l] == XMAS[xmas_idx]:
						# print(f"Found M on ({k},{l}), going {directions[d]}")
						lookaround(lines, XMAS[xmas_idx+1], k, l, xmas_idx+1, directions[d])
				d += 1
	else:
		k = i+dir_shift[direction][0]
		l = j+dir_shift[direction][1]
		if k >= 0 and k < len(lines) and l >= 0 and l < len(lines[0]):
			if lines[k][l] == letter:
				# print(f"Found {letter} on ({k},{l}), going {direction}")
				if xmas_idx == len(XMAS)-1:
					XMAS_cnt += 1
					# print("Found XMAS :)")
				else:
					lookaround(lines, XMAS[xmas_idx+1], k, l, xmas_idx+1, direction)


def part_one(lines):
	for i in range(len(lines)):
		for j in range(len(lines[0])):
			if lines[i][j] == 'X':
				# print(f"Found X on ({i}, {j})")
				lookaround(lines, 'M', i, j, 1)

def find_mas(lines, i, j):
	"""
	Look for an 'M'. If found, check if an 'S' is on the opposite direction.
	We need two matches to find a cross.
	"""
	cross = 0
	for direction in cross_directions:
		k = i + dir_shift[direction][0]
		l = j + dir_shift[direction][1]
		if k >= 0 and k < len(lines) and l >= 0 and l < len(lines[0]):
			if lines[k][l] == 'M':
				k = i + dir_shift[dir_opposite[direction]][0]
				l = j + dir_shift[dir_opposite[direction]][1]
				if k >= 0 and k < len(lines) and l >= 0 and l < len(lines[0]):
					if lines[k][l] == 'S':
						cross += 1
	if cross == 2:
		return True
	else:
		return False



def part_two(lines):
	global XMAS_cnt
	for i in range(len(lines)):
		for j in range(len(lines[0])):
			if lines[i][j] == 'A':
				if find_mas(lines, i, j):
					XMAS_cnt += 1


with open('input', 'r') as f:
	lines = f.readlines()
	lines = [line.strip() for line in lines]

# part_one(lines)
part_two(lines)
print(XMAS_cnt)