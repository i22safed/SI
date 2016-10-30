# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 19:50:10 2016

@author: david
"""

# 
# 5. Programa que comprima/descomprima un fichero mediante gzip. Usar el
# mismo módulo Zlib anterior. El programa principal debe funcionar:
# $comprime fichentrada -o fichsalida
# $descomprime fichentrada -o fichsalida
# 

import zlib 

fichentrada = open("/home/david/code/SI/fichentrada.txt", "r")
fichsalida = open("/home/david/code/SI/fichsalida.txt", "w")


for linea in fichentrada:

    linea = zlib.compress(linea)
    fichsalida.write(linea)

        
print "Realizado el proceso de encriptacion"

fichentrada.close()
fichsalida.close()

