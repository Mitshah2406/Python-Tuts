# ------------------------
#                         Done Using Lhun's Algorithm
#                             Check for more info: https://www.geeksforgeeks.org/luhn-algorithm/
#                                                                                             ----------------------------------------


card_no = "56105910810182504"
number = list(card_no)
odd_sum = 0
even_sum = 0
double_list = []


for (index, value) in enumerate(number):  # Here, enumerate fn allows us to also access the index no of list
    if index % 2 != 0:  # if index is odd value will be stored odd_sum and will get added
        odd_sum += int(value)  # Here int is used to convert str in int
    else:
        # here values of even index are remaining so we took them and doubled them i.e (+2)
        double_list.append(int(value)*2)

# seperating values

# cnv list to str
double_string = ""
for x in double_list:
    double_string += str(x)

# cnv str back to list

double_list = list(double_string)

# seperating values
# adding the seperated values

for x in double_list:
    even_sum += int(x)

total = even_sum + odd_sum

if total % 4 == 0:
    print("Credit Card Number is Correct")
else:
    print("Credit Card Number is Incorrect")
