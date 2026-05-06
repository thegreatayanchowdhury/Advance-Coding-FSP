s = input()
n = len(s)
s = s + s
maxsum = 0
for i in range(n):
    used = set()
    tsum = 0
    for j in range(i, i + n):
        if s[j] in used:
            break
        used.add(s[j])
        tsum += ord(s[j]) - 96
        maxsum = max(maxsum, tsum)
print(maxsum)