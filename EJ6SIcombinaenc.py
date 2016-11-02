# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 21:43:17 2016

@author: David Sanchez

"""

#
# 6. Programa que combine algoritmo Caesar + compresión, y otro con la
# operación inversa: descompresión + algoritmo Caesar.
#

import zlib 

# En este apartado ciframos con el cifrado cesar 

file = open("/home/david/code/SI/fichentrada.txt", "r")
outfile = open("/home/david/code/SI/fichsalida.enc", "w")

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

print "\nYa se ha finalizado el proceso de encriptacion (Cesar)\n"



fichentrada = open("/home/david/code/SI/fichsalida.txt", "r")
fichsalida = open("/home/david/code/SI/cesar_compresion.txt", "w")


for linea in fichentrada:

    linea = zlib.compress(linea)
    fichsalida.write(linea)

        
print "Realizado el proceso de encriptacion"

fichentrada.close()
fichsalida.close()



