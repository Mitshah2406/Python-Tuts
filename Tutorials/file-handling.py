#file opening and writing(adding)

# file = open("file.txt", 'w')
# file.write("This is the text written in the file.")
# file.close()  #---closing the file is very important
 

#file reading

file=open("file.txt",'r')
content = file.read()
print(content)
file.close()

#append mode(adding new content without deleting previous content)

file = open("demo.txt", 'a')
file.write("\n this is the new line")
file.close()
 
file = open("demo.txt", 'r')
content = file.read()
print(content)
file.close()