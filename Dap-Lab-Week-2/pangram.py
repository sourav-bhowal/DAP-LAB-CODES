import string

def is_pangram(s):
    return set(string.ascii_lowercase).issubset(set(s.lower()))


text = "The quick brown fox jumps over the lazy dog"
print(is_pangram(text)) 
