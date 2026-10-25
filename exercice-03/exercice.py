temperatures = [12.5, 14, 9.5, 17, 21, 19.5, 11]
moyenne=round(sum(temperatures)/len(temperatures), 2)
print(moyenne)
print(min(temperatures))
print(max(temperatures))

compteur=0
for i in temperatures:
    if i>15:
        compteur+=1

print(f"jours > 15  °C: {compteur}")

fahrenheit=[]
for i in temperatures:
    fahrenheit.append(i*9/5 +32)
print(fahrenheit)

for jour, temperature in enumerate(temperatures, start=1):
    print(f"jour {jour} : {temperature}  °C")



