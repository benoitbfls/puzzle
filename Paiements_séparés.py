print("Bill Split Calculator")

bill_amount = float(input("Entrer le montant total de la facture: "))
tip_percentage = float(input("Entrer le pourcentage du total à verser en pourboire: "))
nbre_people = int(input("Entrer le nombre de convives: "))
tip_amount = (tip_percentage / 100) * bill_amount
total_amount = bill_amount + tip_amount
total_people = total_amount / nbre_people

print(f"Total (including tip): ${total_amount}")
print(f"Each person pays: ${total_people}")