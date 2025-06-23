# Capitalize the first letter in each word 

s = input()
words = s.split()
capitalized_words = [word.capitalize() for word in words]
print(' '.join(capitalized_words))

