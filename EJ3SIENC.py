# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 19:17:59 2016

@author: David Sanchez
"""

# Encripta para un desplazamiento de K

# 3. Algoritmos enc/dec Caesar general (desplazamiento=k) para que el
# programa principal funcione de la forma:
#
# $caesarencg k entrada.txt -o salida.enc
# $caesardecg k entrada.enc -o salida.txt
#

k = input("Introduzca el valor de K [0,25]: ")     # Leemos el valor de desplazamiento

while k < 0 or k > 25:     

    k = input("Introduzca el valor de K: ")     # Leemos el valor de desplazamiento


# Abrimos para mostrar el contenido del fichero 

file = open("/home/david/code/SI/entrada.txt", "r")
outfile = open("/home/david/code/SI/salida.enc", "w")
    
print "Contenido sin encriptar: "
for line in file: 
    print(line)


# Proceso de encriptado 

file.close()
file = open("/home/david/code/SI/entrada.txt", "r")

while True:
    
    letra = file.read(1)
    
    if letra == " ":
        
        outfile.write(letra)
    
    if letra.islower():
        
        letra = ord(letra) + k
        
        if letra > 122:

            letra = (letra%122) + 97
            letra = chr(letra)
            outfile.write(letra)

        else:
    
            letra = chr(letra)
            outfile.write(letra)
    
    if letra.isupper():
        
       letra = ord(letra) + k 
       if letra > 90:
            letra = (letra%90) + 65
            letra = chr(letra)
            outfile.write(letra)
       else:
            letra = chr(letra)
            outfile.write(letra)
        
# Si no son letras salimos
        
    if not letra:
        break

# Proceso de desencriptado 

file.close()
outfile.close()

outfile = open("/home/david/code/SI/salida.enc", "r")

print "Contenido encriptado: "
for line in outfile: 
    print(line)
    
