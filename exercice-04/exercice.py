ventes=[{"produit":"café", "prix": 2.5, "quantite": 120},
        {"produit": "thé", "prix":2.0, "quantite": 80},
        {"produit": "juis", "prix":3.5, "quantite": 45}]
ca_par_produit={}
for i in ventes:
        ca_par_produit[i["produit"]]=i["prix"]*i["quantite"]
print(ca_par_produit) 

Total=sum(ca_par_produit.values())
print(Total)


for produit, chiffre_affaires in ca_par_produit.items():
        if chiffre_affaires==max(ca_par_produit.values()):
                 print(f"le produit qui rapporte le plus est : {produit} avec un chiffre d’affaire de {chiffre_affaires}")

