# ----------------------CHARACTER CLASS-----------------
# character classes are used to define a range to accept the input.
import re
pattern=r"[A-Z][A-Z][0-9]" #square brackets are used for defining character class and [A-Z][0-9] are the range.
#so, if user enters AS2 it matches range then input will be accepted or if user user enters A2S then it doesn't match the range specified then input will not be accepted.
if re.search(pattern,"MA2"):
    print("Match Found")

