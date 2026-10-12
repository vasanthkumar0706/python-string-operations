def find_substring(s,sub)
    if sub in s:
        return "substring found"
    else:
        return "substring not found"

s = input("enter a string: ")
sub = input("enter substring: ")

print(find_substring(s,sub))