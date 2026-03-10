print("A VER BRO, VAMOS A VER TU HOROSCOPO")

elnombredelwey = input("COMO TE LLAMAS BRO? ")
diacuandonaciste = int(input("QUE DIA NACISTE BRO? "))
mesdenacimientodelwey = input("QUE MES NACISTE WE? (todo en minusculas) ")

if ((diacuandonaciste >= 21 and diacuandonaciste <= 31) and mesdenacimientodelwey == "marzo") or ((diacuandonaciste <= 19 and diacuandonaciste > 0) and mesdenacimientodelwey == "abril"):
    print(elnombredelwey, "eres Aries, signo de fuego, bien intenso.")

elif ((diacuandonaciste >= 20 and diacuandonaciste <= 30) and mesdenacimientodelwey == "abril") or ((diacuandonaciste <= 20 and diacuandonaciste > 0) and mesdenacimientodelwey == "mayo"):
    print(elnombredelwey, "eres Tauro.")

elif ((diacuandonaciste >= 21 and diacuandonaciste <= 31) and mesdenacimientodelwey == "mayo") or ((diacuandonaciste <= 20 and diacuandonaciste > 0) and mesdenacimientodelwey == "junio"):
    print(elnombredelwey, "eres Geminis.")

elif ((diacuandonaciste >= 21 and diacuandonaciste <= 30) and mesdenacimientodelwey == "junio") or ((diacuandonaciste <= 22 and diacuandonaciste > 0) and mesdenacimientodelwey == "julio"):
    print(elnombredelwey, "eres Cancer.")

elif ((diacuandonaciste >= 23 and diacuandonaciste <= 31) and mesdenacimientodelwey == "julio") or ((diacuandonaciste <= 22 and diacuandonaciste > 0) and mesdenacimientodelwey == "agosto"):
    print(elnombredelwey, "eres Leo.")

elif ((diacuandonaciste >= 23 and diacuandonaciste <= 31) and mesdenacimientodelwey == "agosto") or ((diacuandonaciste <= 22 and diacuandonaciste > 0) and mesdenacimientodelwey == "septiembre"):
    print(elnombredelwey, "eres Virgo.")

elif ((diacuandonaciste >= 23 and diacuandonaciste <= 30) and mesdenacimientodelwey == "septiembre") or ((diacuandonaciste <= 22 and diacuandonaciste > 0) and mesdenacimientodelwey == "octubre"):
    print(elnombredelwey, "eres Libra.")

elif ((diacuandonaciste >= 23 and diacuandonaciste <= 31) and mesdenacimientodelwey == "octubre") or ((diacuandonaciste <= 21 and diacuandonaciste > 0) and mesdenacimientodelwey == "noviembre"):
    print(elnombredelwey, "eres Escorpio.")

elif ((diacuandonaciste >= 22 and diacuandonaciste <= 30) and mesdenacimientodelwey == "noviembre") or ((diacuandonaciste <= 21 and diacuandonaciste > 0) and mesdenacimientodelwey == "diciembre"):
    print(elnombredelwey, "eres Sagitario.")

elif ((diacuandonaciste >= 22 and diacuandonaciste <= 31) and mesdenacimientodelwey == "diciembre") or ((diacuandonaciste <= 20 and diacuandonaciste > 0) and mesdenacimientodelwey == "enero"):
    print(elnombredelwey, "eres Capricornio.")

elif ((diacuandonaciste >= 21 and diacuandonaciste <= 31) and mesdenacimientodelwey == "enero") or ((diacuandonaciste <= 19 and diacuandonaciste > 0) and mesdenacimientodelwey == "febrero"):
    print(elnombredelwey, "eres Acuario.")

elif ((diacuandonaciste >= 20 and diacuandonaciste <= 29) and mesdenacimientodelwey == "febrero") or ((diacuandonaciste <= 20 and diacuandonaciste > 0) and mesdenacimientodelwey == "marzo"):
    print(elnombredelwey, "eres Piscis.")

else:
    print("BRO, ESA FECHA ESTA RARA O NO EXISTE.")
