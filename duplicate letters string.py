def duplicate_letters(s)
    for c in s:
        if s.count(c) > 1:
            if c not in result:
                result.append(c)
    return result

result = []
s = input("enter a string")

print("duplicate letters:",duplicate_letters(s))
