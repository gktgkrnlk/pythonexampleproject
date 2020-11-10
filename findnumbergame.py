import random

sayi = random.randint(1,100)
hak = 5

while hak > 0:
    hak -= 1
    tahmin = int(input('tahmin: '))

    if sayi == tahmin:
        print('tebrikler')
        break
    elif sayi > tahmin:
        print('yukarı')
    else:
        print('aşağı')
    
    if hak == 0:
        print(f'Hakkınız bitti.Tutulan Sayı: {sayi}')