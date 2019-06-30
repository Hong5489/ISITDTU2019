from pwn import *
s = remote("104.154.120.223", 8083)
text = s.recv()						# Receive output
lines = text.split('\n')[1:-1]		# Split with newline
for i in range(5):					# Repeat 5 times
	index = 0						# Starts with index 0
	text = ''
	while(1):
		for l in lines:
			text += l[index]			# Combine text vertically according the index
		if text != '        ':			# If its not space, move to next index
			index += 1
			text = ''
		else:
			break						# Found index
	num = '\n'.join([l[:index] for l in lines])
	print num,repr(num) 				# Combine with newline print it out
	for i in range(len(lines)):			
		lines[i] = lines[i][index+1:]	# Split the found and remain numbers