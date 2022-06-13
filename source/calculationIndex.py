# Yapacaginiz islemi secin
print("Islem sec: \n\n")
print("1. Toplama","\n2. Cikarma","\n3. Carpma","\n4. Bolme")

# secim operatörü
secmek = input("Seciminiz nedir? (1-2-3-4): ")
s1 = int(input("1. Sayi: "))
s2 = int(input("2. Sayi: "))

if secmek == "1":
    print(s1, "+", s2, "=",s1+s2)
elif secmek == "2":
    print(s1, "-", s2, "=",s1-s2)
elif secmek == "3":
    print(s1, "x", s2, "=",s1*s2)
elif secmek == "4":
    print(s1, "/", s2, "=",s1/s2)
else:
    print("Boyle bir secim numarasi bulunamadi. Lutfen dogru numarayi yazin.")