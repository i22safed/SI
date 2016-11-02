# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 19:37:56 2016

@author: David Sánchez
"""

# 
# 4. Hacer una función que devuelva una cadena pasada como parámetro
# comprima. Usar el formato zlib del módulo Zlib de Ruby (buscar en
# Google: rdoc zlib).7
# 

import zlib 

cadena = "Programa en un lenguaje de programacion de tu eleccion"

print "La cadena sin comprimir: ", cadena 

compresion = zlib.compress(cadena)

print "La cadena comprimida: ", compresion 

print "\nEl tamaño de la cadena sin comprimir es: ", len(cadena)
print "El tamaño de la cadena comprimida es: ", len(compresion)