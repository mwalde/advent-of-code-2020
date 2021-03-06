test_sled_map = """..##.........##.........##.........##.........##.........##.......
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#"""

file = open("./puzzles/input_03.txt")
sled_map = file.read()
file.close()

sled_map = sled_map.strip()

#sled_map = test_sled_map

increments = [[1,1],
							[3,1],
							[5,1],
							[7,1],
							[1,2]]
							
#increments = [[3,1]]
trees_per_line = []

for increment in increments:
	line = 0
	trees = 0
	sideways = 0
	sideways_increment = increment[0]
	line_increment = increment[1]
	sled_map_array = sled_map.split("\n")
	while(line < len(sled_map_array)):
		#if line_count == len(line) + 5: break	
		if sled_map_array[line][sideways%len(sled_map_array[line])] == """#""":
			trees += 1
			#print(line_count+1, sideways, len(line))
	#	print(line[0:sideways%len(line)+1])
		sideways += sideways_increment
		line += line_increment
	trees_per_line.append(trees)
#print("Final", line_count+1, sideways, len(line))

mult = 1
for item in trees_per_line:
	mult = mult*item 
print(f"The number of trees in part 2 is {mult} and the line count is {line}")
		
		
