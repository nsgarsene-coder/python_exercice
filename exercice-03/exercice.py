temperature=[12.5, 14, 9.5, 17, 21, 19.5, 11]
print(round(sum(temperature)/len(temperature),2))

a=max(temperature)
print(a)
b=min(temperature)
print(b)
for i in temperature:
    if i>15:
        print(i)
    else:
        print("aucun")
      
fahrenheit=[]
for i in temperature:
    c=(i*9/5)+32
    fahrenheit.append(c)

print(fahrenheit)

for i, temperature in enumerate (temperature, start=1):
    print(f"jour {i}: {temperature}") 
    
   
    
      


