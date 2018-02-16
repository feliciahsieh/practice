# hackerrank: pangrams

phrase = input().strip().replace(" ", "").lower()
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
#print(sorted(set(ALPHABET)))
#print(sorted(set(phrase)))
if not (set(ALPHABET) - set(phrase)):
    print("pangram")
else:
    print("not pangram")
