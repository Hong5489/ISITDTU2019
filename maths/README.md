# Do you like math?
```
nc 104.154.120.223 8083
```
Netcat into it:
```
# nc 104.154.120.223 8083

#        #####         #####           
#    #  #     #   #   #     #          
#    #  #         #   #     #    ##### 
#    #  ######  #####  #####           
####### #     #   #   #     #    ##### 
     #  #     #   #   #     #          
     #   #####         #####           
                                       
>>> 
```
It's just a Maths question to answer

Answer one got another question appear:
```
# nc 104.154.120.223 8083

 #####         #####           
#     #       #     #          
      #       #     #    ##### 
 #####  #####  ######          
#                   #    ##### 
#             #     #          
#######        #####           
                               
>>> -7

 #####   #####         #####           
#     # #     #   #   #     #          
      # #     #   #   #     #    ##### 
 #####   #####  #####  #####           
#       #     #   #   #     #    ##### 
#       #     #   #   #     #          
#######  #####         #####           
                                       
>>>
```
The hard part is the **connection timeout very quickly** (about 1 seconds)

So we need to write a script to auto answer all these questions 

After few testing we know that:

-> Every numbers and operator got 7 character height

-> Every numbers and operator is seperated with one line

-> Maximum total got 4 number and one operator

First, we need to find a way to seperate these equation first:

My way is find the index is all spaces and split them:
```
Index:
0123456789...
 ##### | ##### |     | #####           
#     #|#     #|  #  |#     #          
      #|#     #|  #  |#     #    ##### 
 ##### | ##### |#####| #####           
#      |#     #|  #  |#     #    ##### 
#      |#     #|  #  |#     #          
#######| ##### |     | #####           
```

Use pwntools and Python to script it:
```python
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
	print '\n'.join([l[:index] for l in lines]) # Combine with newline print it out
	for i in range(len(lines)):			
		lines[i] = lines[i][index+1:]
```

Next, we need to collect all numbers and operator in `#` form:

Print it using `repr` function and store all possible numbers in a dictionary:
```python
num = '\n'.join([l[:index] for l in lines])
print num,repr(num)
```
Output:
```
  #  
 ##  
# #  
  #  
  #  
  #  
#####
      '  #  \n ##  \n# #  \n  #  \n  #  \n  #  \n#####\n     '
```
After collected all numbers, put it in a dictionary:
```python
'0' : '  ###  \n #   # \n#     #\n#     #\n#     #\n #   # \n  ###  \n       ',
'1' : '  #  \n ##  \n# #  \n  #  \n  #  \n  #  \n#####\n     ',
'2' : ' ##### \n#     #\n      #\n ##### \n#      \n#      \n#######\n       ',
'3' : ' ##### \n#     #\n      #\n ##### \n      #\n#     #\n ##### \n       ',
'4' : '#      \n#    # \n#    # \n#    # \n#######\n     # \n     # \n       ',
'5' : '#######\n#      \n#      \n###### \n      #\n#     #\n ##### \n       ',
'6' : ' ##### \n#     #\n#      \n###### \n#     #\n#     #\n ##### \n       ',
'7' : '#######\n#    # \n    #  \n   #   \n  #    \n  #    \n  #    \n       ',
'8' : ' ##### \n#     #\n#     #\n ##### \n#     #\n#     #\n ##### \n       ',
'9' : ' ##### \n#     #\n#     #\n ######\n      #\n#     #\n ##### \n       ',
'*' :'       \n #   # \n  # #  \n#######\n  # #  \n #   # \n       \n       ',
'-' :'     \n     \n     \n#####\n     \n     \n     \n     ',
'+' :'     \n  #  \n  #  \n#####\n  #  \n  #  \n     \n     '
```
Then we can find the numbers based on the value in the dictionary:
```python
for key,value in num_dict.iteritems():
	if value == num:
		equation += key
```
After we collected all characters, we can use `eval()` function in python to calculate the answer for us:
```python
eval('2*2') # 4
```
Using my [full script](solve.py), solved it in couple minutes =)
```
...
...
...
 #####    #          #####  #######          
#     #  ##     #   #     # #                
      # # #     #         # #          ##### 
 #####    #   #####  #####  ######           
#         #     #   #             #    ##### 
#         #     #   #       #     #          
####### #####       #######  #####           
                                             

46

Good job, this is your flag:   ISITDTU{sub5cr1b3_b4_t4n_vl0g_4nd_p3wd13p13}
```

# Flag 
> ISITDTU{sub5cr1b3_b4_t4n_vl0g_4nd_p3wd13p13}