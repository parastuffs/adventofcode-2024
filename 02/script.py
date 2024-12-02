def part_one():
	with open('input', 'r') as f:
		lines = f.readlines()

	reports = []
	for line in lines:
		reports.append(list(map(int, line.split())))

	safe_reports = 0

	for report in reports:
		increasing = False
		decreasing = False
		safe_reports += 1
		# print(report)
		for i in range(len(report)-1):
			# print(report[i], report[i+1])
			if not increasing and not decreasing:
				if report[i] < report[i+1]:
					increasing = True
				elif report[i] > report[i+1]:
					decreasing = True
				else:
					safe_reports -= 1
					break
			elif decreasing:
				if report[i] < report[i+1]:
					safe_reports -= 1
					break
			elif increasing:
				if report[i] > report[i+1]:
					safe_reports -= 1
					break
			if report[i] == report[i+1]:
				safe_reports -= 1
				break

			if increasing or decreasing:
				if abs(report[i] - report[i+1]) > 3:
					safe_reports -= 1
					break

	print(safe_reports)



def isSafe(report):
	"""
	Return -1 if the report is safe
	Return the index of the problematic element otherwise
	"""
	error_index = -1
	increasing = False
	decreasing = False
	# print(report)
	for i in range(len(report)-1):
		# print(report[i], report[i+1])
		# Determine the sequence progression: increasing or decreasing
		if not increasing and not decreasing:
			if report[i] < report[i+1]:
				increasing = True
			elif report[i] > report[i+1]:
				decreasing = True
			else:
				error_index = i
				break
		# Check if we follow a monotonic progression
		elif decreasing:
			if report[i] < report[i+1]:
				error_index = i
				break
		elif increasing:
			if report[i] > report[i+1]:
				error_index = i
				break
		if report[i] == report[i+1]:
			error_index = i
			break

		# Check that the distance is not larger than 3
		if increasing or decreasing:
			if abs(report[i] - report[i+1]) > 3:
				error_index = i
				break
	return error_index

def part_two():
	with open('input', 'r') as f:
		lines = f.readlines()

	reports = []
	for line in lines:
		reports.append(list(map(int, line.split())))

	safe_reports = 0

	for report in reports:
		# print(f"Considering report {report}")
		report_status = isSafe(report)
		# print(f"status: {report_status}")
		if report_status == -1:
			safe_reports += 1
		else:
			# If there was a problem with the report, try again by removing
			# the problematic element, the one before, and the one after.
			for k in range(max([report_status-1,0]), min([report_status+1,len(report)])+1):
				testing_report = [report[i] for i in range(len(report)) if i != k]
				# print(f"Testing the report {testing_report}")
				updated_status = isSafe(testing_report)
				# print(f"Updated status: {updated_status}")
				if updated_status == -1:
					safe_reports += 1
					break
	print(safe_reports)

part_two()