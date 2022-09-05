n = int(input())
for i in range(n):
    str = input()
    score = 0
    combo = 0
    for s in str:
        if s == 'O':
            score += 1 + combo
            combo += 1
        else:
            combo = 0
    print(score)
