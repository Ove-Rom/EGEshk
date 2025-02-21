for z in "0123456789":
    for o in "0123456789":
        for v in "0123456789":
            goyda = int(f"12{z}345{o}67089{v}")
            if goyda % 206 == 0:
                print(goyda, goyda//206)