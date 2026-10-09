ventes=[{"produit":"café", "prix": 2.5, "quantite": 120},
        {"produit": "thé", "prix":2.0, "quantite": 80},
        {"produit": "juis", "prix":3.5, "quantite": 45}]


ca_par_produit={ventes[0]["produit"]: ventes[0]["prix"]*ventes[0]["quantite"], ventes[1]["produit"]: ventes[1]["prix"]*ventes[1]["quantite"],
                ventes[2]["produit"]: ventes[2]["prix"]*ventes[2]["quantite"]}
print(ca_par_produit)

total=ca_par_produit["café"]+ca_par_produit["thé"]+ca_par_produit["juis"]

print(total)

