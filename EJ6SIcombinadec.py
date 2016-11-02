# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 18:46:59 2016

@author: david
"""

#
# 6. Programa que combine algoritmo Caesar + compresión, y otro con la
# operación inversa: descompresión + algoritmo Caesar.
#

import zlib
 
fichentrada = open("/home/david/code/SI/cesar_compresion.txt", "r")
fichsalida = open("/home/david/code/SI/cesar.txt", "w")

for linea in fichentrada:

    linea = zlib.decompress(linea)
    fichsalida.write(linea)
    
print "Realizado el proceso de descompresion"

fichentrada.close()
fichsalida.close()


file = open("/home/david/code/SI/cesar.txt", "r")
outfile = open("/home/david/code/SI/no_cesar_compresion.txt", "w")

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

print "\nYa se ha finalizado el proceso de desencriptacion\n"