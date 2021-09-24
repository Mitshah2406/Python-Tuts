# Write Python code to open a file named demo.txt and write some random data into it.

# 2. Open the file, read the contents and display them as output.

# 3. Write python code to add additional text to the existing file on a new line without deleting the previous contents.
file=open("demo.txt",'w')
file.write('Google LLC is an American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, a search engine, cloud computing, software, and hardware. It is considered one of the big four Internet stocks along with Amazon, Facebook, and Apple.')
file.close()


file= open("demo.txt",'r')
content= file.read()
print(content)
file.close()

file= open("demo.txt",'a')
file.write('\nthis is new line')
file.close()

file= open("demo.txt",'r')
content= file.read()
print(content)
file.close()