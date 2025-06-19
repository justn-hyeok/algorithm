import sys

text = sys.stdin.read().replace("\n", "").replace(" ", "")
counts = [0] * 26
for char in text:
    if 'a' <= char <= 'z':
        counts[ord(char) - ord('a')] += 1

max_count = max(counts)

result = [chr(i + ord('a')) for i in range(26) if counts[i] == max_count]

print(''.join(result))
