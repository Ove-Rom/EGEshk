garph = {"a":"bcz", "b":"cd", "c":"bdz", # 2 вариант
         "d":"efz", "e":"dfz", "f":"ez",
         "z":"a"}

# garph = {"a":"bcz", "b":"cd", "c":"dz", # 1 вариант
#          "d":"efz", "e":"fz", "f":"ez",
#          "z":"a"}

def f(fn, p):
    global cnt
    if p[-1] == fn and len(p) >= 6:
        cnt += 1
        return
    for ch in garph[p[-1]]:
        if ch not in p:
            f(fn, p+[ch])

cnt = 0

f("z", ["a"])

print(cnt)