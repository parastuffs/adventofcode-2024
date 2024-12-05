rules = {}
updates = []

def part_one(rules, updates):
	total = 0
	for update in updates:
		invalid = False
		for i in range(len(update)):
			# I consider a page in the update sequence
			page = update[i]
			# If the page has a rule associated
			if page in rules:
				# Check that not page number comming before are part of the rule
				for j in range(i):
					if update[j] in rules[page]:
						invalid = True
						break
		if not invalid:
			total += int(update[int((len(update)-1)/2)])
	return total

def part_two(rules, updates):
	total = 0
	for update in updates:
		invalid = False
		i = 0
		while i < len(update):
			# I consider a page in the update sequence
			page = update[i]
			# If the page has a rule associated
			if page in rules:
				# Check that not page number comming before are part of the rule
				j = 0
				while j < i:
					# If it does, send it to the end of the array
					if update[j] in rules[page]:
						update.append(update[j])
						del update[j]
						i = 0
						invalid = True
					else:
						j += 1
			i += 1						
		if invalid:
			total += int(update[int((len(update)-1)/2)])
	return total


with open('input', 'r') as f:
	lines = f.readlines()
	lines = [line.strip() for line in lines]

# Parse the ordering rules
for line in lines:
	if '|' in line:
		left = line.split('|')[0]
		right = line.split('|')[1]
		if not left in rules:
			rules[left] = [right]
		else:
			rules[left].append(right)
	elif ',' in line:
		updates.append(line.split(','))
# print(rules)
# print(updates)
# print(part_one(rules, updates))
print(part_two(rules, updates))

