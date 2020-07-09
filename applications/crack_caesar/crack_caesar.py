# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
from collections import Counter

# Your code here
common_letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

with open("./ciphertext.txt", "r") as r:
    contents = r.read()

count = Counter(filter(str.isalnum, contents))

mapping = {k:v for (k, v) in zip([i[0] for i in count.most_common()], common_letters)}
end_text = ""
for char in contents:
    end_text_chars = char
    if char in mapping.keys():
        end_text_chars = mapping[char]
    end_text += end_text_chars

print(end_text)