"""1-mashq"""

from datetime import date, datetime , timedelta

ramazon = date(2026, 2, 20)
bugun = date.today()

qoldi = (ramazon - bugun).days

print(f"Ramazon oyiga yana {qoldi} kun qoldi")

"""2-mashq"""

print(bugun.strftime(f"Bugun yilning %B oyi "))
print(bugun.strftime(f"Bugun haftaning %w kuni "))

"""3-mashq"""

x = int(input("Haftani kiriting: "))

sana = bugun + timedelta(weeks=x)

print(sana.strftime(f"{x} haftadan keyingi sana %m - %B %Y - yil. Hafatning %A kuni bo'ladi "))


"""vazifa"""

"""1-mashq"""

sana = date(2010, 3, 10)
keyingi_sana = sana - timedelta(weeks =8, hours= 325, minutes=854)

print(f"{(keyingi_sana)}")


"""2-mashq"""

yil = int(input("Yilni kiriitng (maktabga birinchi borgan): "))
oy = int(input("Oyni kiriting (maktabga birinchi borgan): "))
kun = int(input("Kunni kiriitng (maktabga birinchi borgan): "))

birinchi_qongiroq = date(yil, oy, kun)
farq = (bugun - birinchi_qongiroq).days

print(f"Maktabga birinchi borganingnizga {farq} kun bo'libdiyey`")

"""3-mashq"""

try:
    soat = int(input("Sotni kriitng: "))

    keyingi_vaqt = bugun + timedelta(hours= soat)
    print(keyingi_vaqt.strftime(f"{soat} soatdan keyin vaqt %H:%M  bo'ladi."))

except ValueError:
    print("Sanani raqamlarda kriitng: ")
except OverflowError:
    print("Siz chegaradan chqib ketdingiz")
except:
    print("Funksiya ishlashida xatolik yuz berdi")

