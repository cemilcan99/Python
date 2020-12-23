name= input("İsminizi giriniz: ")
isim = name 
şifre= input("Şifreyi giriniz: ")
hesap= {
    "adı" : name,
    "hesap no" : "12345667",
    "bakiye"  : 4000,
    "ek hesap" : 2000,
    "şifre": "fener1907"

}


          
           
    
    
        
      
def bakiyesorgu(hesap):
    print(f"Merhaba {hesap['adı']} {hesap['hesap no']} nolu hesabınızda {hesap['bakiye']} tl ek hesapta {hesap['ek hesap']} tl bulunmaktadır")
def paracekme(miktar):
    
    if hesap["bakiye"] >= miktar:
        print(print(f"{hesap['hesap no']} nolu hesabınızdan {miktar} tl paranızı alabilirsiniz."))
        hesap["bakiye"]-=miktar
        bakiyesorgu(hesap)
    else:
        toplam = hesap["bakiye"] + hesap["ek hesap"]
        if toplam >= miktar:
            ek= input("Ek hesap kullanılsın mı?(e/h): ")
            if ek=="e":
                print(f"Merhaba {hesap['adı']} paranızı alabilirsiniz")
                ekhesapkullanılıcak= miktar - hesap["bakiye"]
                hesap["bakiye"]=0
                hesap["ek hesap"]-= ekhesapkullanılıcak
                bakiyesorgu(hesap)
            else:
                print(f"{hesap['hesap no']} nolu hesabınızda {hesap['bakiye']} tl bakiye bulunmaktadır")
        else:
            print(f"Üzgünüz bakiye yetersiz , {hesap['hesap no']} nolu hesabınızda {hesap['bakiye']} tl ek hesabınızda {hesap['ek hesap']} TL bulunmaktadır ")
        

def giriş(şifre):
    if şifre ==hesap["şifre"]:
        print(f"Hoşgeldiniz {hesap['adı']}")
        miktar=int(input("Çekmek istediğiniz miktarı yazınız: ")) 
        paracekme(miktar)
         
    else:
        print("Hatalı giriş")
 

giriş(şifre)    






