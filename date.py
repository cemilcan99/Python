#Araç Muayne Takip
import datetime
tarih = (input("aracnızı hangi tarihte trafiğe çıktı (Yıl/Ay/Gün: "))
tarih= tarih.split("/")

aracıkıs= datetime.datetime(int(tarih[0]) ,int(tarih[1]),int(tarih[2]))
suan = datetime.datetime.now()
fark = suan - aracıkıs
days=fark.days

if days<=365:
    print("1.muayne")

elif (days >365) and (days <= 365*2):
    print("2.Yıl")
elif (days >365*2) and (days <= 365*3):
    print("3.Yıl")
elif (days >365) and (days <= 365*2):
    print("4.Yıl")
else:
    print("Çabuk muayneye")

