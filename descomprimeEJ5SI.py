# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:32:07 2016

@author: david
"""

# 
# 5. Programa que comprima/descomprima un fichero mediante gzip. Usar el
# mismo módulo Zlib anterior. El programa principal debe funcionar:
# $comprime fichentrada -o fichsalida
# $descomprime fichentrada -o fichsalida
# 

import zlib
 
fichentrada = open("/home/david/code/SI/fichsalida.txt", "r")
fichsalida = open("/home/david/code/SI/fichentrada.txt", "w")

for linea in fichentrada:

    linea = zlib.decompress(linea)
    fichsalida.write(linea)
    
print "Realizado el proceso de descompresion"

fichentrada.close()
fichsalida.close()