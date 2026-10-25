produit="clavier"

prix_ht=19.90

quantite=3

taux_tva=0.2

total_ht=prix_ht*quantite

total_ttc=total_ht*(1+taux_tva)
print(f"3 x clavier: {total_ttc:.2f} euros TTC")

prix_texte="19.90"
prix_ht=float(prix_texte)

total_ht=prix_ht*quantite

total_ttc=total_ht*(1+taux_tva) 


print(total_ttc)

print(f"3 x clavier: {total_ttc:.2f} euros TTC")