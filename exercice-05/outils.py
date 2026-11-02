def convertir_note(texte):
    try:
        note=texte.replace(",", ".")
        note=float(note)
        return note
    except ValueError:
        return None
        

c="12,5"
d=convertir_note(c)
print(d)

notes_brutes = [12.5, 15, 9, 18.25]
def moyenne(valeurs):
    calcul_moyenne=sum(valeurs)/len(valeurs)
    return calcul_moyenne
resultat=moyenne(notes_brutes)
print(resultat)

def mention(resultat):
    if resultat<10:
        return "Mention: insuffisante"
    elif resultat<12:
        return "Mention: passable"
    elif resultat<14:
        return "Mention: assez-bien"
    elif resultat<16:
        return "Mention: bien "
    else:
        return "Mention: très bien"










