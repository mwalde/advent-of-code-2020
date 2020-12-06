file = open("./puzzles/input_01.txt")
numbers = file.read()
file.close()

numbers = numbers.strip()
numbers = numbers.split("\n")

from itertools import combinations

list_2020 = []
for num in combinations(numbers,3):
	if int(num[0]) + int(num[1])+ int(num[2]) == 2020:
		list_2020.append(num)
		
print(list_2020)
print(int(list_2020[0][0]) * int(list_2020[0][1]) * int(list_2020[0][2]))
