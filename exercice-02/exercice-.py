

def temperature_message(temp):
    if temp is None:
        return "la température est non définie"
    elif temp <0:
        return "gel"
    elif temp <15:
        return "froid"
    elif temp <25:
        return "doux"

    else:
        return "chaud"


a=temperature_message(-3)
b=temperature_message(0)
c=temperature_message(15)
d=temperature_message(31)

def annee_bissextile(annee):
    if annee%4==0 and annee%100!=0 or annee%400==0:
        return True
    else:
        return False

x=annee_bissextile(2024)
y=annee_bissextile(1900)
z=annee_bissextile(2000)
print(x)
print(y)
print(z)
