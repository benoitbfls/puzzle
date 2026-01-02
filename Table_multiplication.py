nbre1 = int(input("Entre un nombre entre 1 et 10 : "))

if nbre1 < 1 or nbre1 > 10:
    print("Saisie incorrecte")
else:
    print(f"=== Table de multiplication de {nbre1} ===")
    
    for x in range(1, 11):
        result = nbre1 * x
        if result % 2 == 0:
            print(f"{nbre1} x {x} = {result}")
        else:
            print(f"{nbre1} x {x} = {result} (IMPAIR)")
              
    print("---")