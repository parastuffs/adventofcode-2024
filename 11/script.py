
def part_one(line):
	blinks = 25
	for blink in range(blinks):
		# print(line)
		i = 0
		while i < len(line):
			# print(line)
			stone = line[i]
			# print(f"Check stone {stone}")
			# print(i)
			if stone == '0':
				# print("Stone '0'")
				line[i] = '1'
			elif len(stone)%2 == 0:
				# print("Even stone")
				stone_lst = list(stone)
				line[i] = ''.join(stone_lst[:int(len(stone_lst)/2)])
				# str(int()) to remove leading 0's, then convert back to str
				line.insert(i+1, str(int(''.join(stone_lst[int(len(stone_lst)/2):]))))
				i += 1
			else:
				# print("Other stone")
				line[i] = str(int(stone)*2024)
			i += 1
	print(len(line))


def part_two(line):
	blinks = 75
	stones = {}
	# Dictionnary initialisation
	for stone in line:
		if stone not in stones:
			stones[stone] = 1
		else:
			stones[stone] += 1
	for blink in range(blinks):
		print(f"blink: {blink}")
		# print(f"Stones: {stones}")
		stones_update = stones.copy()
		for stone in stones:
			stone_amount = stones[stone]
			if stone == '0':
				if '1' in stones_update:
					stones_update['1'] += stone_amount
				else:
					stones_update['1'] = stone_amount
			elif len(stone)%2 == 0:
				stone_lst = list(stone)
				left_stone = ''.join(stone_lst[:int(len(stone_lst)/2)])
				right_stone = str(int(''.join(stone_lst[int(len(stone_lst)/2):])))
				if left_stone in stones_update:
					stones_update[left_stone] += stone_amount
				else:
					stones_update[left_stone] = stone_amount
				if right_stone in stones_update:
					stones_update[right_stone] += stone_amount
				else:
					stones_update[right_stone] = stone_amount
			else:
				new_stone = str(int(stone)*2024)
				if new_stone in stones_update:
					stones_update[new_stone] += stone_amount
				else:
					stones_update[new_stone] = stone_amount
			stones_update[stone] -= stone_amount
			if stones_update[stone] == 0:
				del stones_update[stone]
		stones = stones_update.copy()
	score = 0
	for stone in stones:
		score += stones[stone]
	print(score)
	# print(stones)


with open('input', 'r') as f:
	lines = f.readlines()
	lines = [line.strip().split() for line in lines]

# part_one(lines[0])
part_two(lines[0])