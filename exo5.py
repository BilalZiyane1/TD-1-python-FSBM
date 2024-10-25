#? correction : Prof :

N = int(input("Entrer le terme de la suite"))
U1 = 1
U2 = 1
if N<= 2:
    print("la valeur final est :", 1)
else:
    for i in range(3, N+1):
        UN = U1 + U2
        U1 = U2
        U2 = UN
    