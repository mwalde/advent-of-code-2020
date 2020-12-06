with open("./puzzles/input_02.txt", 'r') as passwords:

	good_passwords = 0
	part_two = 0
	
	for line in passwords:
		count = 0
		
		range = line.split(" ")[0]
		letter = line.split(" ")[1]
		password = line.split(" ")[2]
		
		lower = int(range.split("-")[0])
		upper = int(range.split("-")[1])
		
		letter = letter.split(":")[0]
		
		for alpha in password:
			if alpha == letter:
				count += 1 
				
		if lower <= count <= upper: 
			good_passwords += 1
			
		if (password[lower-1] == letter) != (password[upper-1] == letter):
			part_two += 1
			
		
print(f"Number of valid passwords: {good_passwords}")
print(f"Number of valid passwords, part two: {part_two}")

#print(password[lower-1], password[upper-1], password[lower-1] == letter and password[upper-1] != letter)
