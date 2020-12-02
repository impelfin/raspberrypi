for i in [0, 1, 2, 3, 4]:
    if i % 2 != 0:
        continue
    print("%d ^ 2 = %d" % (i, i * i))
