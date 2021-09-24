#To perform Find & Replace in python

#for this, we use sub function from re module. sub means substitute.

import re 
string = "Hi,I am Aditya.Hello Aditya."
pattern =r"Aditya"
newstring = re.sub(pattern, "Mit", string)
print(newstring)