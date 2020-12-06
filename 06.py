file = open("./puzzles/input_06.txt")
customs = file.read()
file.close()


def unique(clist):
	un = []
	for item in clist:
		if item not in un: un.append(item)
	return un

csum = 0
for group in customs.split('\n\n'):
	group = group.replace('\r','').replace('\n','')
	group = ''.join(group)
	csum += len(unique(group))

print("part 1: ", csum)		

def comm_ans(clist):
	first_answer = [*clist[0]]
	common_answers = []
	count = 0
	for ans in first_answer:
		ans_count = 1
		for item in clist[1:]:
			if ans in unique(item): ans_count += 1
			#print(count, ans_count, ans, item)
		if ans_count == len(clist): count +=1
		#print(ans_count, count, len(clist))
	return count


csum2 = 0
for group in customs.split('\n\n'):
	group = group.replace('\r',' ').replace('\n',' ')
	csum2 += comm_ans(group.split(' '))
	
print("part 2: ", csum2)		

