
f = open("text.txt","r")#as read mode see in pycharm for the keywords and applications
print(f.name)#prints file name
print(f.mode)#prints file mode 
f.close()#closes it
#simpler way than to explicitly close a file
with open("text.txt","r") as f:
	print(type(f))
# now, if we are  reading a large fie, we dont want to store it in memory.
#so,
with open("text.txt","r") as f:
	f_content=f.readline()#reads one line , cursor position is updated after execution
	print(f_content)
	print(f.tell())# prints position of cursor
	f_stuff=f.readlines()#reads multiple lines, in  a list form
	print(f_stuff)
	#to read a number of characters:
	size_to_read=10
	f_contents=f.read(size_to_read)

#to iterate over lines:
#as a generator
with open("text.txt","r") as f:
	size_to_read=10
	f_contents=f.read(size_to_read)
	while len(f_contents)>0:
		print(f_contents, end='*')
		print(f.tell)
		f_contents=f.read(size_to_read)
#if we need to reset cursor position,
with open("text.txt","r") as f:
	a=f.read(10)#reads 10 characters
	print(a)
	f.seek(0)#resets cursor position to specified position
	b=f.read(10)#prints the same

#writing to files
with open("text2.txt","w") as f:#in write mode , creates if file doesnt exist
	f.write("abcd")#overwrites it
	f.seek(3)#seek is usuable in write method too, overwrites if another character in the cursor
	f.write("rstuv")
#reading and writing simultaneously :
#method1:
with open("text.txt","r") as rf:
	with open("text_copy","w") as wf:#creates new file
	for line in rf:
		wf.write(line)#text is copied
#dealing with picture files:

with open("Welcome Scan.jpg","rb") as f:#binary read
	with open("copy.jpg",'wb') as wf:
		for line in f:
			wf.write(line)
			#creates a copy
#to get more control:
#read a chunk:
with open("Welcome Scan.jpg", "rb") as f:
	with open("Welcome Scan.jpg","wb") as wf:
		chunk_size=4096# not standard
		 q=f.read(chunk_size)#reads a piece
		#to write as a generator:
		while len(q)>0:#till the length of the readbits are not 0
			wf.write(q)#writes the data
			q=f.read(chunk_size)#reads from current cursor position

