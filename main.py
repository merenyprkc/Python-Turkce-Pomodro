from win11toast import toast
import time
import os

os.system("cls||clear")
print("💻 github.com/merenyprkc")
print("✖️ Eğer kapatmak istersen terminale gelip CTRL+C tuşlarına basman yeterli.\n")

dersDakika = float(input("⏰ Kaç dakika boyunca ders çalışacaksın: "))
araDakika = float(input("⏰ Kaç dakika ara vereceksin: "))
uzunAraDakika = float(input("⏰ Kaç dakika uzun ara vereceksin: "))

dersSayi = 0

while True:
    os.system("cls||clear")
    if(dersSayi < 3):
        print("\n⏳ Ders çalışma süren başladı, süren bittiğinde bildirim gelecektir.")
        time.sleep(dersDakika * 60)
        toast(
            "github.com/merenyprkc",
            "Ders çalışma süren bitti, ara verme vakti.",
            duration="short",
            audio = {"src": "ms-winsoundevent:Notification.Looping.Alarm", "loop": "true"}
        )
    else:
        print("\n⏳ Bu dersten sonra uzun ara zamanı, süren bittiğinde bildirim gelecektir.")
        time.sleep(dersDakika * 60)
        toast(
            "github.com/merenyprkc",
            "Ders çalışma süren bitti, uzun ara verme vakti.",
            duration="short",
            audio = {"src": "ms-winsoundevent:Notification.Looping.Alarm", "loop": "true"}
        )
    dersSayi += 1
    os.system("cls||clear")
    if(dersSayi < 4):
        print("\n⏳ Ara verme vakti, süren başladı. Bittiğinde bildirim gelecektir.")
        time.sleep(araDakika * 60)
        toast(
            "github.com/merenyprkc",
            "Ara verme vaktin bitti, ders çalışma vakti.",
            duration="short",
            audio = {"src": "ms-winsoundevent:Notification.Looping.Alarm6", "loop": "true"}
        )
    elif(dersSayi >= 4):
        print("\n⏳ Uzun ara verme vakti, süren başladı. Bittiğinde bildirim gelecektir. Keyifli dinlenmeler!")
        time.sleep(uzunAraDakika * 60)
        toast(
            "github.com/merenyprkc",
            "Uzun aran bitti, şimdi tekrardan ders vakti.",
            duration="short",
            audio = {"src": "ms-winsoundevent:Notification.Looping.Alarm6", "loop": "true"}
        )
        dersSayi = 0