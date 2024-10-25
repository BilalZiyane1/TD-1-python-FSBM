for i in range(0, 101):
    if i == 0 or i == 1:
        continue
    
    pr = True
    for j in range(i + 1, i // 2 + 1):
        if i % j == 0:
            pr = False
    if pr:
        print(f"{i} ", end="")
            