def not_gir():
    ad= input("İsim: ")
    soyad= input("Soyad: ")
    not1= (input("not1: "))
    not2= (input("not2: "))
    not3=  (input("not3: "))
    with open("examresult.txt","a",encoding="utf-8") as file:
        file.write(ad + " "+soyad+":"+ not1+","+not2+","+not3+"\n")
    
     
    
    
def not_oku(satır):
    satır=satır[:-1]
    liste=satır.split(":")
    öğrencismi=liste[0]
    notlar=liste[1].split(",")
    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])
    ortalama= int((not1+not2+not3)/3)
    if ortalama >=90 and ortalama <=100:
        harf="AA"
    elif ortalama >=85 and ortalama <=89:
        harf="BA"
    elif ortalama >=65 :
        harf="CC"
    else:
        harf="FF"
    return öğrencismi + ":" + harf + "\n"


    

    
def not_kayıt():
    with open("examresult.txt","r",encoding="utf-8") as file:
        liste=[]
        for i in file:
            liste.append(not_oku(i))
        with open("examark.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)


def ortalama_oku():
    with open("examresult.txt","r",encoding="utf-8") as file:
        for satır in file:
            print(not_oku(satır))






while True:
    islem= input("1-Not gir\n2-Notları Oku\n3-Notları Kaydet\n4-Çıkış\n")
    if islem=="1":
        not_gir()
    elif islem=="2":
        ortalama_oku()
    elif islem=="3":
        not_kayıt()
    else:
        break

