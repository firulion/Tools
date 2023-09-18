#file = 'test.txt'

Pstring = 'Passed 8'
i = 0

with open(file, 'r+') as f:
	f_2 = open("test.txt", 'w+')
	f_2.seek(0)
	for lines in f:
		if Pstring in lines:
			i = 0
			for word in lines.split(" "):
				f_2.write(word + ' ')
				i = i+1
				if i == 5:
					print(word)
					f_2.write('\n')
					i = 0 
		else:
			f_2.write(lines)

	f_2.close()