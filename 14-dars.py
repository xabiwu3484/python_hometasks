# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 14:50:58 2021

@author: hbbdm
"""
# otam = {"ismi":"davron", "tyil":1970, "viloyat":"andijon"}
# tyil = otam["tyil"]
# vil = otam["viloyat"]
# print(f"Otamning ismi {otam["ismi"].title()}, {tyil}-yilda,
#       {vil.title()} viloyatda tug`ilgan")
      

# taomlar = {"Maryam":"Sut", "Guzaloy":"Go`sht", "Sevara":"Blinchik",
#            "Ayam":"Sho`rva", "Ayasi":"Osh", "Men":"Shashlik"}
# taom = taomlar["Maryam"]
# print(f"Maryamning sevimli taomi {taom}")

python_izohli_lugati = {"integer":"Butun son",
                        "float":"O`nlik sonlar",
                        "string":"Matn",
                        "list":"Ro`yxat",
                        "tuple":"O`zgarmas ro`yxat"}
kalit = input("Kalit so`z kiriting:").lower()
# print(python_izohli_lugati.get(kalit,"Bunday so`z mavjud emas"))
tarjima = python_izohli_lugati.get(kalit)
if tarjima == None:
    print("Bunday so`z mavjud emas")
else:
    print(f"{kalit.title()} so`zi {tarjima} deb tarjima qilinadi")
    

























