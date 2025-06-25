matn = """#salom assalom #maktab_tugadi AD3746633 yettita 232324 #surish_kerak
323 24 va BA5240976 albatta maktab SS3940909
"""

"""1-MASHQ"""
from re import match, findall, search

p_pattern1 = r"^[A-Z]{2}[\s][0-9]{3}-[0-9]{2}[\s][A-Z]"
p_pattern2 = r"^[A-Z]{2}[\s][0-9]{7}"

print(match(p_pattern1, "JH 434-45 S"))
print(match(p_pattern2, "AD 2359875"))

"""2-mashq"""
pattern1 = r"[a-zA-Z]{7}"
print(findall(pattern1, matn))

"""3-mashq"""
pattern2 = r"[#][a-zA-Z0-9]{1,5}"
print(findall(pattern2, matn))

"""4-mashq"""
pattern3 = r"[A-Z]{2}[0-9]{7}"
print(search(pattern3, matn))
