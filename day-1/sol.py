nums = [int(x.strip()) for x in open("input.txt", "r").readlines()]
n = len(nums)

# Basic brute force is fast enough for this problem

# Part 1
def part1():
	for i in range(n):
		i_num = nums[i]
		for j in range(i + 1, n):
			j_num = nums[j]
			if i_num + j_num == 2020:
				print(i_num * j_num)
				return

# Part 
def part2():
	for i in range(n):
		i_num = nums[i]
		for j in range(i + 1, n):
			j_num = nums[j]
			for k in range(j + 1, n):
				k_num = nums[k]
				if i_num + j_num + k_num == 2020:
					print(i_num * j_num * k_num)
					return

part1()
part2()