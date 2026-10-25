

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
print(a)

b=temperature_message(0)
print(b)

c=temperature_message(15)
print(c)

d=temperature_message(31)
print(d)

def annee_bissextile(annee):
    if annee%4==0 and annee%100!=0 or annee%400==0:
        return True
    else:
        return False

x=annee_bissextile(2024)
if x:
    print("2024 est une année bissextile")
else:
    print("2024 n’est pas une année bissextile")
y=annee_bissextile(1900)
if y:
    print("1900 est une année bissextile")
else:
    print("1900 n’est pas une année bissextile")

z=annee_bissextile(2000)
if z:
    print("2000 est une année bissextile")
else:
    print("2000 n’est pas une année bissextile")
