def print_disk(disk):
	print(''.join(list(map(str,disk))))

def part_one(disk_map):
	"""
	Create disk image
	- Alternate between free_space and not free_space
	- Get the value, cast it to int()
	- Increment ID
	- Create entry in a dictionnary {ID: size}
	- Create a disk image (with the dots and all)

	Defragment
	- Go through the disk in reverse order
	"""
	block_sizes = {}
	free_space = False
	block_id = 0
	disk = []
	for space in disk_map:
		if not free_space:
			block_sizes[block_id] = int(space)
			disk += [block_id] * int(space)
			block_id += 1
		elif free_space:
			disk += ['.'] * int(space)
		free_space = not free_space
	# print_disk(disk)

	idx = len(disk)-1
	while idx > 0:
		# If there is still free space on the left part of the disk
		if '.' in disk[:idx]:
			if disk[idx] != '.':
				moving_block = disk[idx]
				for i in range(idx):
					if disk[i] == '.':
						disk[i] = moving_block
						disk[idx] = '.'
						break
			idx -= 1
		else:
			break
	# print_disk(disk)

	# Compute checksum
	checksum = 0
	for i in range(len(disk)):
		block = disk[i]
		if block == '.':
			break
		checksum += i*block
	print(checksum)


def part_two(disk_map):
	block_sizes = {}
	free_space = False
	block_id = 0
	disk = []
	free_spaces =  [] # [[free space size, position],...]
	position = 0
	for space in disk_map:
		if not free_space:
			block_sizes[block_id] = int(space)
			disk += [block_id] * int(space)
			block_id += 1
		elif free_space:
			disk += ['.'] * int(space)
			free_spaces.append([int(space), position])
		position += int(space)
		free_space = not free_space
	# print_disk(disk)

	# Defragment
	idx = len(disk)-1
	while idx > 0:
		# If there is still free space on the left part of the disk
		if '.' in disk[:idx]:
			shift = 1
			if disk[idx] != '.':
				moving_block = disk[idx]
				moving_size = block_sizes[moving_block]
				for j, free_space in enumerate(free_spaces):
					# make sure it's large enough AND to the left
					if free_space[0] >= moving_size and free_space[1] < idx - moving_size:
						for i in range(moving_size):
							disk[free_space[1]+i] = moving_block
							disk[idx-i] = '.'
						free_spaces[j] = [free_space[0] - moving_size, free_space[1] + moving_size]
						break
				shift = moving_size
			idx -= shift
		else:
			break
	# print_disk(disk)

	# Compute checksum
	checksum = 0
	for i in range(len(disk)):
		block = disk[i]
		if block == '.':
			block = 0
		checksum += i*block
	print(checksum)


with open('input', 'r') as f:
	lines = f.readlines()
	lines = [list(line.strip()) for line in lines]

# part_one(lines[0])
part_two(lines[0])