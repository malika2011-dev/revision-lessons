"""1-mashq"""
taomlar = []

x = int(input("Nechta taom kiritmoqchisiz: "))
for z in range(x):
    taomlar.append(input(f"{z+1} - taomni kiriting: "))

taomlar.append("Manti")
taomlar.insert(0, "Besh tekis")
taomlar.insert(1, "Osh")

print(taomlar)

"""2-mashq"""

ism = "  Sodiqjanov Mirazim   "

print(ism.title())
print(ism.upper())
print(ism.lower())
print(ism.rstrip())
print(ism.lstrip())

"""3-mashq"""
ranglar = ["oq", "qora", "qizil", "ko'k", "sariq", "yashil", "binafsha", "kulrang"]

colors = []

colors.append(ranglar.pop(-1))
colors.append(ranglar.pop(-2))
colors.append(ranglar.pop(-3))

print(colors)
print(ranglar)

