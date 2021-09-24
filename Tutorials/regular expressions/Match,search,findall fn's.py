# --------------------Regular expressions-----------------
# It is a module whcih has some important functions.


# 1)To know that a string matches a particular pattern.(Match,search,findall)
import re  #re means Regular expressions


# ------------------------match function---------------------
pattern = r"mit" #Here, r means raw string.

# ------------------NOTE::Match is only found in start or end of string i,e, if string entered is adimitadi then no match will be found.
if re.match(pattern, "adimitadi"): #Here,actually pattern variable is the pattern which we are searching in mitadimit
    print("Match Found.")

else:
    print("Match not Found.")


    # -------------------------------Search function------------------
#search is also same as match
# ------------------NOTE::Match is found anywhere in the string 
if re.search(pattern, "adimitadi"): #Here,actually pattern variable is the pattern which we are searching in mitadimit
    print("Match Found.")

else:
    print("Match not Found.")

    #---------------------findall function-------------------
    #it does same work as search fn or it can used to know how many times a particular pattern is presnet in a string.

print(re.findall(pattern, "adimitadimit"))
