#Caret(^) and Dollar($) meta character
import re 
pattern = r"^gr.y$"# Caret specifies the start of the string and Dollar specifies the end of the string.
if re.match(pattern, "gray"):
    print("Match Found.")