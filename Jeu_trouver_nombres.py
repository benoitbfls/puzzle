a = 8
tentatives = 0 
b= int(input(f"Devine le nombre mystère (entre 1 et 10): "))
tentatives += 1

while a != b :
    if b < a:
        print("C'est plus")
        b = int(input(f"Devine le nombre mystère (entre 1 et 10): "))
        tentatives += 1
    elif b > a:
        print("C'est moins")
        b = int(input(f"Devine le nombre mystère (entre 1 et 10): "))
        tentatives += 1

print(f"Bravo ! tu as touvé en {tentatives} tentatives")
      