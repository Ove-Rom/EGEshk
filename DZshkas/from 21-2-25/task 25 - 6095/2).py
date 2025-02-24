from itertools import product

for fir in range(3):
    for sec in range(3):
        if fir + sec < 3:
            for z1 in product("123456789", repeat = fir):
                for z2 in product("0123456789", repeat = sec):
                    num = int(f"{''.join(z1)}15{''.join(z2)}7424")
                    match (num % 111 == 0, num % 113 == 0, num % 127 == 0):
                        case (True, False, False):
                            print(num, num // 111)
                        case (False, True, False):
                            print(num, num // 113)
                        case (False, False, True):
                            print(num, num // 127)
