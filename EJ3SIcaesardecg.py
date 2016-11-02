# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 17:26:22 2016

@author: david
"""

# Desencripta para un desplazmientode K 
#
# 3. Algoritmos enc/dec Caesar general (desplazamiento=k) para que el
# programa principal funcione de la forma:
# 
#   $caesarencg k entrada.txt -o salida.enc
#   $caesardecg k entrada.enc -o salida.txt
#



file = open("/home/david/code/SI/salida.enc", "r")
outfile = open("/home/david/code/SI/entrada.enc", "w")

# Leemos el valor de desplazamiento

k = input("Introduzca el valor de K [0,25]: ")     

while k < 0 or k > 25:     

    k = input("Introduzca el valor de K: ")


# Primero cogemos el fichero lo abrimos y copiamos la salida encriptada 
# a la entrada encriptada

while True:
    letra = file.read(1)
    outfile.write(letra)
    
    if not letra: 
        break


file.close()
outfile.close()


# Realizamos el proceso de desencriptado para el valor determinado de K 

file = open("/home/david/code/SI/entrada.enc", "r")
outfile = open("/home/david/code/SI/salida.txt", "w")

while True:
    
    letra = file.read(1)
    
    if letra == " ":
        
        outfile.write(letra)
    
    if letra.islower():
        
        letra = ord(letra) - k
        
        if letra > 122:

            letra = (letra%122) + 97
            letra = chr(letra)
            outfile.write(letra)

        else:
    
            letra = chr(letra)
            outfile.write(letra)
    
    if letra.isupper():
        
       letra = ord(letra) - k 
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


print "Finalizado proceso de encriptacion"