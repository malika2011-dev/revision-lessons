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

print(sana.strftime(f"{x} haftadan keyingi sana %m - %B . Hafatning %A kuni bo'ladi "))