##### Part 1
with open('input', 'r') as f:
	lines = f.readlines()

l = []
r = []
for line in lines:
	l.append(int(line.split()[0]))
	r.append(int(line.split()[1]))

l.sort()
r.sort()

dist = 0
for i in range(len(l)):
	dist += abs(l[i] - r[i])

print(dist)


##### Part 2
with open('input', 'r') as f:
	lines = f.readlines()

l = []
r = []
for line in lines:
	l.append(int(line.split()[0]))
	r.append(int(line.split()[1]))

dict_r = {}
for el in set(r):
	dict_r[el] = r.count(el)

sim_score = 0
for el in l:
	if el in dict_r:
		sim_score += el*dict_r[el]

print(sim_score)