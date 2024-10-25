#? My draft :
n = int(input("Entre l'ordre N :"))
list_An = []
for i in range(n+1):
    An = int(input(f"Entrer la valeur de A{i}:"))
    list_An.append(An)

X = int(input("Entrer la valeur de X:"))
s = 0
n_cp = n
for i in range(len(list_An) - 1, -1, -1):
    s += list_An[i]*(X**n_cp)
    n_cp -= 1
print("la somme :", s)
    


#? Prof correction :
print("===Prof Method===")
N = int(input("entre le degre de polynome"))
X = float(input("Entrer la valeur de X:"))
S = 0
for i in range(N, -1, -1):
    A = float(input(f"Entrer coefficient A {i}"))
    S += A * X**i
print("La valeur du polynome est Prof method:",S)


#? recursive approach : works :)
def poly(x, n):
    if n <0:
        return 0
    A = float(input(f"Entrer la valeur de A{n}"))
    return (A* x**n) + poly(x, n - 1)
print("Recursive somme :",poly(5, 3))