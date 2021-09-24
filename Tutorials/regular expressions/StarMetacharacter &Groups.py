#------------------Star(*) Meta character and Groups-------------
# star meta charater allows zero or one or two or multiple repititions of any group,character class or string.
import re
pattern = r"eggs(bacon)*"#here, parenthesis are used for defining groups and star means bacon can be repeated in the string multiple times or cannot be repeated also,but star is only for bacon not for eggs so eggs should exist in the string.
if re.match(pattern,"eggsbaconbacon"):
    print("Match Found.")