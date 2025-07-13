N = int(input())
S = input()
print(S[:-1] if S[-1] == 'G' else S + 'G')
