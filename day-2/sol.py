lines = [x.strip() for x in open("input.txt", "r").readlines()]

# Part 1
total_correct = 0
for line in lines:
	pieces = line.split(" ")
	[start, end] = [int(x) for x in pieces[0].split("-")]
	num = pieces[2].count(pieces[1][0])
	if start <= num <= end:
		total_correct += 1
print(total_correct)

# Part 2
total_correct = 0
for line in lines:
	pieces = line.split(" ")
	[start, end] = [int(x) for x in pieces[0].split("-")]
	letter = pieces[1][0]
	if (pieces[2][start-1] == letter) != (pieces[2][end-1] == letter):
		total_correct += 1
print(total_correct)