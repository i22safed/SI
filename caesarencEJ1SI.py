# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:17:56 2016

@author: David Sanchez
"""

# Algoritmo de encriptación Caesar (desplazamiento=3) para que el
# programa principal funcione de la forma:
#
# caesarenc entrada.txt -o salida.enc
# 
# Codificacion realizada solo utilizando mayusculas y minusculas, sin contemplar
# signos, etc.

# Utilizar la funcion isUpper(letra)

file = open("/home/david/code/SI/entrada.txt", "r")
outfile = open("/home/david/code/SI/salida.enc", "w")

while True:

#Para espacios

    letra = file.read(1)

    if letra==" ":    
        outfile.write(letra)
        
# Para letras mayusculas/minusculas
        
    # Minusculas

    if letra.islower() :
        
        letra = ord(letra) + 3 
        if letra > 122:
            letra = (letra%122) + 97
            letra = chr(letra)
            outfile.write(letra)
        else:
            letra = chr(letra)
            outfile.write(letra)

    # Mayusculas

    if letra.isupper():
        
       letra = ord(letra) + 3 
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
    
file.close()
outfile.close()

print "\nYa se ha finalizado el proceso de encriptacion\n"