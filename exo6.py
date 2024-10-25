#? my draft 
N = int(input("Entrer la valeur souhaite :"))
if N == 0 or N == 1:
    print(f"{N} n'est pas un nbre premier")
elif N == 2:
    print(f"{N} est un nombre premier")
elif N % 2 == 0:
        print(f"{N} n'est pas un nombre premier")
else:
    premier = True
    for i in range(3, N):
        if N % i == 0:
            premier = False
            break
    if premier:
        print(f"{N} est un nombre premier")
    else:
        print(f"{N} n'est pas un nombre premier")
        
        
#? method better optimized : 
pr = True
for i in range(2, N // 2 + 1 ):
    if N % i == 0:
        pr = False
if pr:
    print(f"{N} est un nombre premier")
else:
    print(f"{N} n'est pas un nombre premier")
    
    
#? Prof correction :
cpt = 0
for i in range(1, N+1):
    if N % i == 0:
        cpt += 1
if cpt > 2:
    print(f"")
    
    