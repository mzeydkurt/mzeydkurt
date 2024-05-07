hesaplar = [
    {
        "ad":"Muhammed Zeyd KURT",
        "hesapNo": "12345",
        "bakiye": 200000,
        "username":"mzeydkurt",
        "password":"1234"
    },
    {
        "ad":"Mahmud KURT",
        "hesapNo": "12345",
        "bakiye": 50000,
        "username":"mahmudkurt",
        "password":"1234"
    },
    {
        "ad":"Zehra KURT",
        "hesapNo": "12345",
        "bakiye": 30000,
        "username":"zehrakurt",
        "password":"1234"
    }
]
def menu(hesap):
    print(f"Hosgeldiniz!, {hesap["ad"]}")
    print("\n")
    print("MENU")
    print("1-) Bakiye Sorgulama")
    print("2-) Para Cekme ")
    print("3-) Para Yatirma ")
    islem = input("Yapmak istediginiz islemi seciniz")
    if islem == "1":
        bakiyeSorgu(hesap)
    elif islem == "2":
        paracekme(hesap)
    elif islem == "3":
        parayatirma(hesap)
    else:
        print("Yanlis Secim")
def parayatirma(hesap):
    yatirma = int(input("Yatirmak istediginiz miktari giriniz"))
    yenibakiye = hesap["bakiye"] + yatirma
    print(f"Yeni Bakiyeniz {yenibakiye}")
def paracekme(hesap):
    miktar = int(input("Ne Kadar Para Cekmek Istiyorsunuz : "))
    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("Paranizi Cekebilirsiniz")
    else :
        print("Yetersiz Bakiye")
def bakiyeSorgu(hesap):
    print(f"Bakiyeniz : {hesap["bakiye"]}")
def loggin():
    username = input("Username : ")
    password = input("Password : ")
    isLoggin = False
    for hesap in hesaplar:
        if hesap["username"] == username and hesap["password"] == password:
            isLoggin = True
            menu(hesap)
            break
    if not(isLoggin):
        print("Kullanici Adi veya Parola Yanlis!!!")
loggin()
