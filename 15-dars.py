# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 22:03:55 2021

@author: hbbdm
"""
# py_words = {
#         "integer":"Butun son",
#         "float":"O`nlik son",
#         "boolean":"Mantiqiy qiymat",
#         "for":"Biror amalni qayta-qayta bajarish tsikli",
#         "if":"Shartlarni tekshirish operatori"}

# for key, value in sorted(py_words.items()):
#     print(f"{key.title()} - {value}")


davlatlar = {
    "o`zbekiston":"toshkent",
    "aqsh":"washington d.c.",
    "rossiya":"moskva",
    "angliya":"london",
    "koreya":"seul",
    "yaponiya":"tokiyo",
    "australiya":"sidney",
    "germaniya":"berlin",
    "ispaniya":"madrid"}
print("Dunyo davlatlari:")
for davlat in sorted(davlatlar):
    print(davlat.upper())

print("\nDavlatlarning poytaxtlari")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())
    
country = input("Qaysi davlatning poytaxtimi bilishni istaysiz?:").lower()
capital = davlatlar.get(country)
if capital==None:
    print("Kechirasiz, bizda bu haqida ma`lumot yo`q")
else:
    print(f"{country.upper()}ning poytaxti {capital.title()}shahri")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    