import re as regex

text = "What an excellent  example of the power of dress, young Oliver Twist was"

print('\n-- break text by whitespace --\n')
compiled_regex_whitespace = regex.compile('[\s,]' )
split_text = compiled_regex_whitespace.split(text);
print(split_text)



print('\n-- break longer text by occurence of word "the" --\n')
text = """What an excellent example of the power of dress, young Oliver Twist was! 
Wrapped in the blanket which had hitherto formed his only covering, he might have been the child of a nobleman or a beggar; it would have been hard for the haughtiest stranger to have assigned him his proper station in society. But now that he was enveloped in the old calico robes which had grown yellow in the same service, he was badged and ticketed, and fell into his place at once—a parish child—the orphan of a workhouse—the humble, 
half-starved drudge—to be cuffed and buffeted through the world—despised by all, and pitied by none."""

pieces = [x.strip()  for x in regex.split( ' the ' , text)]

# for fragment in pieces:
print(pieces)

print('\n-- Extract matching fragments from string  - -all substring matching [3 digits][any number of alphabets][3 digits]      --\n')
string_with_numbers = "hi ny 555name888 is something to 320remember324 forever"
print(
    regex.findall('[\d]{3}[a-zA-z]*[\d]{3}' , string_with_numbers)
)


print('\n-- All done --\n')
print('\n--  --\n')