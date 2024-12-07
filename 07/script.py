from itertools import product



def part_one(lines):
	operators = ['*', '+']
	code = 0
	for line in lines:
		target = int(line.split(':')[0])
		values = [int(i) for i in line.split(':')[1].split()]
		combinations = list(product(operators, repeat=len(values)-1))
		combinations = [list(comb) for comb in combinations]
		for comb in combinations:
			valid = False
			res = values[0]
			for i in range(len(comb)):
				op = comb[i]
				if op == '*':
					res *= values[i+1]
				elif op == '+':
					res += values[i+1]
			if res == target:
				valid = True
				break
		if valid:
			code += target
	print(code)

def part_two(lines):
	operators = ['*', '+', '||']
	code = 0
	for line in lines:
		target = int(line.split(':')[0])
		values = [int(i) for i in line.split(':')[1].split()]
		combinations = list(product(operators, repeat=len(values)-1))
		combinations = [list(comb) for comb in combinations]
		for comb in combinations:
			valid = False
			res = values[0]
			for i in range(len(comb)):
				op = comb[i]
				if op == '*':
					res *= values[i+1]
				elif op == '+':
					res += values[i+1]
				elif op == '||':
					res = int(str(res) + str(values[i+1]))
			if res == target:
				valid = True
				break
		if valid:
			code += target
	print(code)



with open('input', 'r') as f:
	lines = f.readlines()
	lines = [line.strip() for line in lines]

# part_one(lines)
part_two(lines)