
def powerset(pole):
    n = len(pole)
    pocet_podmnozin = 2 ** n
    podmnoziny = []

    for i in range(pocet_podmnozin):
        podmnozina = []
        for j in range(n):
            if i & (1 << j): #pokud je jtý bin binarniho cisla i 1 pridej do podmnoziny jty prvek pole
                podmnozina.append(pole[j])
        podmnoziny.append(podmnozina)
    
    podmnoziny.sort(key=len)
    return podmnoziny

pole = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] 
vysledek = powerset(pole)  

for podmnozina in vysledek:
    print(podmnozina)
