#Numbers
i = 5000

print(i.bit_count())#retorna cuantos 1 hay en la exprecion binaria
print(i.bit_length())#retorna cuantos bit necesito
print(bin(i))#retorna la exprecion del numero binario
print(i.to_bytes(2,"little"))
print(i.from_bytes(i.to_bytes(2,"little"),"big"))
#Floating point
print("Floating point")
f = 200.10
print(f.as_integer_ratio())#retorna numerador y denominador que cuando se divide bota num que tiene
print(1_2000_300)#para cifras
print(1j+f)#numeros complejos
