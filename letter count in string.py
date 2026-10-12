def letter_count(s):
    count = {}

    for ch in s:
        if ch . isalpha():
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

s = input("enter a string:")

print("letter count:",letter_count(s))