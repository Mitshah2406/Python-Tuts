#Dot Meta Character
import re 
pattern = r"gr.y"#here, . meta character means that it can contain any letter from a to z. 
#applications:  for eg:: gray color has two spellings gray or grey. So,if user enters any one of them then if condition should match.that's why it is used.
if re.match(pattern, "gray"):
    print("Match Found.")