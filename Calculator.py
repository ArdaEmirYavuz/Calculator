import math
def Sum(args):
    return sum(args)
def Extract(args):
    total = 0
    for i in args:
        total = total - i 
    return total
def İmpact(args):
    total = 1
    for i in args:
        total *= i
    return total
def Divide(args):
    total = args[0]
    for i in args[1:]:
        if(i == 0):
            continue
        total = total / i
    return total 
def Comb():
    n = input("Kombinasyonunu almak istediğiniz sayıyı giriniz:")
    while(True):
        try:
            n = int(n)
            if(n <= 0):
                print("Lütfen 0 dan büyük pozitif bir sayı giriniz!")
                continue
            else:
                break
        except(ValueError):
            print("Lütfen geçerli bir sayı giriniz")
            continue
    k = input("Sayının kaçlı kombinasyonunu almak istiyorsunuz:")
    while(True):
        try:
            k = int(k)
            if(k <= 0):
                print("Lütfen 0 dan büyük pozitif bir sayı giriniz!")
                continue
            elif(k >n):
                print("Sayınız bu kombinasyon değerine uymuyor.Tekrar deneyin.")
                continue
            else:
                break
        except(ValueError):
            print("Lütfen geçerli bir sayı giriniz")
            continue
    return math.comb(n,k)
def Pow():
    a = input("Sayının tabanını giriniz:")
    while(True):
        try:
            a = int(a)
            break
        except(ValueError):
            print("Lütfen geçerli bir sayı giriniz")
            continue
    b = input("Sayının üssünü giriniz:")
    while(True):
        try:
            b = int(b)
            break
        except(ValueError):
            print("Lütfen geçerli bir sayı giriniz")
            continue
    return pow(a,b)
def Sqrt():
    a = input("Sayının tabanını giriniz:")
    while(True):
        try:
            a = int(a)
            if(a < 0):
                print("Kareköklü ifadenin içi tanım gereği 0 veya 0'dan büyük olmalıdır.Tekrar deneyin.")
                continue
            break
        except(ValueError):
            print("Lütfen geçerli bir sayı giriniz")
            continue
    return math.sqrt(a)
