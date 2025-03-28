from collections import Counter

with open("26_18541.txt") as f:
    # with open("test") as f:
    n, m = map(int, f.readline().split())
    data = [int(i) for i in f]

balls = data[:n]
mens = data[-m:]

roundedMens = [min(balls, key=lambda x: i - x \
    if i - x > 0 else float("inf")) for i in mens]

midBall = sum(roundedMens) // len(roundedMens)
popularBall = Counter(roundedMens).most_common()[0][0]

print(midBall, popularBall)
