import re

def part_one(lines):
	pattern = "mul\([\d]+,[\d]+\)"
	matches = []
	total = 0
	for line in lines:
		matches += re.findall(pattern, line)
		print(matches)
	for match in matches:
		total += int(match.split(',')[0].split('(')[1]) * int(match.split(',')[1].split(')')[0])
	print(total)

def part_two(lines):
	pattern = "(mul\([\d]+,[\d]+\))|(do\(\))|(don't\(\))"
	matches = []
	total = 0
	for line in lines:
		matches += re.findall(pattern, line)
	# Clean up
	matches = [match[i] for match in matches for i in range(len(match)) if match[i] != '']
	do = True
	for match in matches:
		if "don't" in match:
			do = False
		elif "do" in match:
			do = True
			continue
		if do:
			total += int(match.split(',')[0].split('(')[1]) * int(match.split(',')[1].split(')')[0])
	print(total)




with open('input', 'r') as f:
	lines = f.readlines()
# part_one(lines)
part_two(lines)