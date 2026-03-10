print("A VER BRO, VAMOS A VER TU HOROSCOPO")

elnombredelwey = input("COMO TE LLAMAS BRO? ")
diacuandonaciste = int(input("QUE DIA NACISTE BRO? "))
mesdenacimientodelwey = input("QUE MES NACISTE WE? (todo en minusculas) ")

if ((diacuandonaciste >= 21 and diacuandonaciste <= 31) and mesdenacimientodelwey == "marzo") or ((diacuandonaciste <= 19 and diacuandonaciste > 0) and mesdenacimientodelwey == "abril"):
    print(elnombredelwey, "eres Aries, signo de fuego 🔥. Sueles ser valiente, impulsivo y te gusta liderar. Siempre quieres empezar cosas nuevas.")

elif ((diacuandonaciste >= 20 and diacuandonaciste <= 30) and mesdenacimientodelwey == "abril") or ((diacuandonaciste <= 20 and diacuandonaciste > 0) and mesdenacimientodelwey == "mayo"):
    print(elnombredelwey, "eres Tauro 🌿. Eres tranquilo, paciente y muy terco. Te gusta la estabilidad, la comida rica y las cosas bonitas.")

elif ((diacuandonaciste >= 21 and diacuandonaciste <= 31) and mesdenacimientodelwey == "mayo") or ((diacuandonaciste <= 20 and diacuandonaciste > 0) and mesdenacimientodelwey == "junio"):
    print(elnombredelwey, "eres Geminis 🌬️. Eres curioso, hablas mucho y te gusta aprender de todo. A veces cambias rápido de opinión.")

elif ((diacuandonaciste >= 21 and diacuandonaciste <= 30) and mesdenacimientodelwey == "junio") or ((diacuandonaciste <= 22 and diacuandonaciste > 0) and mesdenacimientodelwey == "julio"):
    print(elnombredelwey, "eres Cancer 🌊. Eres muy emocional, protector con tu familia y valoras mucho el hogar y las personas cercanas.")

elif ((diacuandonaciste >= 23 and diacuandonaciste <= 31) and mesdenacimientodelwey == "julio") or ((diacuandonaciste <= 22 and diacuandonaciste > 0) and mesdenacimientodelwey == "agosto"):
    print(elnombredelwey, "eres Leo 🦁. Te gusta destacar, eres creativo y tienes mucha confianza. Sueles ser líder y muy leal.")

elif ((diacuandonaciste >= 23 and diacuandonaciste <= 31) and mesdenacimientodelwey == "agosto") or ((diacuandonaciste <= 22 and diacuandonaciste > 0) and mesdenacimientodelwey == "septiembre"):
    print(elnombredelwey, "eres Virgo 📚. Eres muy observador, organizado y perfeccionista. Te gusta analizar todo y ayudar a los demás.")

elif ((diacuandonaciste >= 23 and diacuandonaciste <= 30) and mesdenacimientodelwey == "septiembre") or ((diacuandonaciste <= 22 and diacuandonaciste > 0) and mesdenacimientodelwey == "octubre"):
    print(elnombredelwey, "eres Libra ⚖️. Buscas equilibrio y justicia. Te gusta la armonía, el arte y evitar los conflictos.")

elif ((diacuandonaciste >= 23 and diacuandonaciste <= 31) and mesdenacimientodelwey == "octubre") or ((diacuandonaciste <= 21 and diacuandonaciste > 0) and mesdenacimientodelwey == "noviembre"):
    print(elnombredelwey, "eres Escorpio 🦂. Eres intenso, misterioso y muy apasionado. Cuando quieres algo vas con todo.")

elif ((diacuandonaciste >= 22 and diacuandonaciste <= 30) and mesdenacimientodelwey == "noviembre") or ((diacuandonaciste <= 21 and diacuandonaciste > 0) and mesdenacimientodelwey == "diciembre"):
    print(elnombredelwey, "eres Sagitario 🏹. Te gusta la aventura, aprender cosas nuevas y tener libertad.")

elif ((diacuandonaciste >= 22 and diacuandonaciste <= 31) and mesdenacimientodelwey == "diciembre") or ((diacuandonaciste <= 20 and diacuandonaciste > 0) and mesdenacimientodelwey == "enero"):
    print(elnombredelwey, "eres Capricornio 🐐. Eres disciplinado, trabajador y te enfocas mucho en lograr tus metas.")

elif ((diacuandonaciste >= 21 and diacuandonaciste <= 31) and mesdenacimientodelwey == "enero") or ((diacuandonaciste <= 19 and diacuandonaciste > 0) and mesdenacimientodelwey == "febrero"):
    print(elnombredelwey, "eres Acuario 🌌. Eres original, creativo y te gusta pensar diferente a los demás.")

elif ((diacuandonaciste >= 20 and diacuandonaciste <= 29) and mesdenacimientodelwey == "febrero") or ((diacuandonaciste <= 20 and diacuandonaciste > 0) and mesdenacimientodelwey == "marzo"):
    print(elnombredelwey, "eres Piscis 🐟. Eres soñador, sensible y muy imaginativo.")

else:
    print("BRO, ESA FECHA ESTA RARA O NO EXISTE.")
