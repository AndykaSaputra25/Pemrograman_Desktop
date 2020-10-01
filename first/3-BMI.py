def BMI():
    print("\tBody Mass Index (BMI)")
    b = int(input("\nBerapa berat badan Anda(kg): "))
    t = int(input("Berapa tinggi badan Anda(cm): "))
    tinggi = t/100
    bmi = b / tinggi**2
    
    if bmi <= 18.5:
        print("\n\tBerat Badan Kurang")
    elif bmi > 18.5 and bmi < 24.9:
        print("\n\tNormal (ideal)")
    elif bmi >25 and bmi < 29.9:
        print("\n\tKelebihan berat badan")
    else:
        print("\n\tKegemukan (obesitas)")
BMI()