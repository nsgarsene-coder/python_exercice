from outils import convertir_note, moyenne, mention

notes_brutes = ["12,5", "15", "abc", "9", "18,25"]
nouvelle_notes=[]
compteur=0
nbr=[]
for i in notes_brutes:
    if convertir_note(i) is not None:
        nouvelle_notes.append(convertir_note(i))
    else:
        compteur+=1
        nbr.append(i)
print(nouvelle_notes)
print(compteur)
print(nbr)

moyenne_nouvelle=moyenne(nouvelle_notes)
mention_nouvelle=mention(moyenne_nouvelle)
print(f"Moyenne : {moyenne_nouvelle:.2f}")
print(f"Mention : {mention_nouvelle}")
