# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 23:53:58 2016

@author: David Sánchez
"""

# Algoritmo de desencriptación Caesar (desplazamiento=3) para que el
# programa principal funcione de la forma:

# Algoritmo de encriptación Caesar (desplazamiento=3) para que el
# programa principal funcione de la forma:
#
# caesarenc entrada.txt -o salida.enc
# 
# Codificacion realizada solo utilizando mayusculas y minusculas, sin contemplar
# signos, etc.

# Utilizar la funcion isUpper(letra)

file = open("/home/david/code/SI/entrada.enc", "r")
outfile = open("/home/david/code/SI/salida.txt", "w")

while True:

#Para espacios

    letra = file.read(1)

    if letra==" ":    
        outfile.write(letra)
        
# Para letras mayusculas/minusculas
        
    # Minusculas

    if letra.islower() :
        
        letra = ord(letra) - 3 
        if letra < 97:
            letra = letra + 25
            letra = chr(letra)
            outfile.write(letra)
        else:
            letra = chr(letra)
            outfile.write(letra)

    # Mayusculas

    if letra.isupper():
        
       letra = ord(letra) - 3 
       if letra < 65:
            letra = letra + 25
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