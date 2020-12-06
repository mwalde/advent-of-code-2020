file = open("./puzzles/input_05.txt")
seat_codes = file.read()
file.close()


seat_code_list = []

def f(rows_list):
	return rows_list[:int(len(rows_list)/2)]
	
def b(rows_list):
	return rows_list[int(len(rows_list)/2):]

def r(col_list):
	return col_list[int(len(col_list)/2):]
	
def l(col_list):
	return col_list[:int(len(col_list)/2)]

def scode(row,col):
	return row*8+col
	
for seat_code in seat_codes.split("\n"):
	rows = list(range(0,128))
	cols = list(range(0,8))
	for code in seat_code:
		if code == "F": rows = f(rows)
		elif code == "B": rows = b(rows)
		elif code == "R": cols = r(cols)
		elif code == "L": cols = l(cols)
	seat_code_list.append(scode(rows[0],cols[0]))
	
print(max(seat_code_list))

seat_code_list.sort()
for i,seat in enumerate(seat_code_list):
	if i == 0: continue
	if seat-seat_code_list[i-1] == 2: print(seat_code_list[i]-1)

#import itertools

#my_rows = list(range(1,127))
#my_cols = list(range(1,7))
#my_seat = []

#for combo in itertools.product(my_rows, my_cols):
#	my_seat_code = scode(list(combo)[0],list(combo)[1])
#	my_seat.append(my_seat_code)
	
##my_seat = my_seat.sort()

#for i,seat in enumerate(my_seat):
#	if i == 0: continue
#	if seat-my_seat[i-1] == 2: print(seat, my_seat[i-1])
