#nombre narcissique
n= int(input("donner votre nombre"))
somme ,count=0,0
#calcluler le nombre de chiffre
count = len(str(n))
'''m =n
while m>0:
    count+=1
    m=m//10 '''
m=n
while m>0:
    somme+=pow(m%10,count)
    m=m//10
if n==m:
    print(f"le nombre {n} est narcissique")
