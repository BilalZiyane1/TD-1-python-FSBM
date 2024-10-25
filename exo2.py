# ! exo2
# ? a) with 5 variables
s = 0
num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
num3 = int(input("Number 3:"))
num4 = int(input("Number 4:"))
s = num1 + num2 + num3+ num4
print("La somme : ", s)


# ? b) with only two variables
##? method1: 
a = int(input("Entre N1:"))
s2 = a
a = int(input("Entre N2:"))
s2 += a
a = int(input("Entre N3:"))
s2 += a
a = int(input("Entre N4:"))
s2 += a 
print("la somme est:", s2)


##? method2 :
s = 0
for i in range(5):
    a = int(input("Enter Number ", i+1))
    s += a 
print("la somme :", s)