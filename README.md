# SI

Practicas para la asignatura de Seguridad Informatica

************************************************ PRÁCTICA 3 *****************************************************

************************************************ EJERCICIOS *****************************************************

1. Algoritmo de encriptación Caesar (desplazamiento=3) para que el programa principal funcione de la forma:
  
      $caesarenc entrada.txt -o salida.enc

2. Algoritmo de desencriptación Caesar (desplazamiento=3) para que el programa principal funcione de la forma:
  
     $caesardec entrada.enc -o salida.txt

3. Algoritmos enc/dec Caesar general (desplazamiento=k) para que el programa principal funcione de la forma:

     $caesarencg k entrada.txt -o salida.enc
     $caesardecg k entrada.enc -o salida.txt

4. Hacer una función que devuelva una cadena pasada como parámetro comprima. Usar el formato zlib del módulo 
Zlib de Ruby (buscar en Google: rdoc zlib).

5. Programa que comprima/descomprima un fichero mediante gzip. Usar el mismo módulo Zlib anterior. El programa 
principal debe funcionar:
  
      $comprime fichentrada -o fichsalida
      $descomprime fichentrada -o fichsalida

6. Programa que combine algoritmo Caesar + compresión, y otro con la operación inversa: descompresión + algoritmo 
Caesar.

      $combinaenc fichentrada -o fichsalida
      $combinadec fichentrada -o fichsalida

7. Programa que comprima todos los ficheros del directorio actual que se indiquen en un fichero de configuración 
comprime.conf que contendrá un nombre de fichero por cada línea. (Por ejemplo utilizar el módulo Dir de Ruby 
(rdoc Dir)). Lanzar un error por consola cuando el fichero no exista pero continuar con el resto de ficheros. 
Informar en consola sobre la tasa de reducción alcanzada. El programa principal debe admitir lossiguientes modos 
de ejecución:

      # Comprime la lista en comprime.conf
      $comprimedir
      # Comprime la lista en el fichero pasado
      $comprimedir -f fichero-configuracion

8. Ataque de fuerza-bruta. A partir de un fichero de texto cifrado mediante el cifrado Caesar mostrar todas las 
posibles combinaciones de dicho mensaje. El programa funcionará de la forma:
  
       $fuerzabrutacaesar entrada.enc

9. Evalúa como romper por fuerza bruta automáticamente la encriptación Caesar general de un fichero.

10.Hacer una función que devuelva todas las letras del alfabeto en un orden al azar (una permutación del alfabeto).

11.Programas enc/dec de un fichero mediante una sustitución mono-alfabética al azar obtenida con el ejercicio 
anterior y añadir la clave al principio de dicho fichero.

      $monoenc fichentrada -o fichsalida
      $monodec fichentrada -o fichsalida

12.Hacer un análisis de frecuencias de cada letra de un fichero texto de entrada. Probar con un fichero de texto 
grande (sugerencia: buscar en internet un texto grande).

13.Intentar romper el cifrado mono-alfabético anterior mediante análisis de frecuencias. Analiza e idea un plan 
con las herramientas de que dispones para llevarlo a cabo. ¿Podría automatizarse el proceso?

 
 
 ****************************************** EJERCICIOS ADICIONALES ***********************************************

14.Transposición diagonal de una cadena de texto. A partir de una cadena de entrada cifrar dicha cadena mediante 
el cifrado 'Rail Fence' (buscar este cifrado en la wikipedia). Permitir 2 o 3 raíles.

15.Transposición de columna (columnar cipher). A partir de una cadena de entrada y una longitud de columna dada 
'long', disponer el texto columna a columna. Obtener la cadena cifrada leyendo la caja de texto columna a columna
en un orden obtenido al azar. La clave de la encriptación será el orden de lectura de las columnas.

16.Acceder al enlace de ejercicios de encriptación de la página web de la asignatura y probar sus herramientas de 
encriptación.

17.Ejemplo de cifrado de doble trasposición. Con papel y bolígrafo seguir las instrucciones del 'Manual del Soldado',
Soldier's manual: prepare a double transposition cipher, que puedes encontrar en la web de la asignatura en el fichero 
FM-31-4.pdf

18.Busca en Internet varias 'Rotor Machines' (al menos 3) y anota el autor, año de fabricación y uso de cada una de 
ellas. Las rotor machines supusieron un gran avance en la historia de la criptografía y un paso hacia la criptografía
moderna.



**************************************************** NOTAS ********************************************************

Utilidad GNU zip (gzip, .gz files) y la librería Zlib GNU zip es un software que se usa para la comprimir y 
descomprimir ficheros con la extensión “.gz”. Fue creado por Jean-Loup Gailly y Mark Adler como software libre 
de compresión para sustituir la utilidad compress de los primeros sistemas UNIX. Se diseñó para ser usado por 
el proyecto GNU (la "g" es de "GNU"). La version 0.1 es de 1992, y la version 1.0 de 1993. La versión actual
es la 1.6 de junio de 2013.

Zlib es una librería creada también por Jean-Loup Gailly y Mark Adler en 1995 que usa el mismo algoritmo de 
compresión que usa gzip: el algoritmo DEFLATE. La versión actual es la 1.2.8 de abril de 2013.

Zlib tiene un formato propio, el formato zlib, que es diferente e incompatible con el formato gzip, a pesar de 
que ambas usan el mismo algoritmo y los datos comprimidos son iguales internamente, ya que usan diferente cabeceras 
y trailers en torno a los datos comprimidos.

Gzip fue diseñado para mantener información del fichero a comprimir y su directorio, nombre, fecha de modificación, 
etc., su cabecera es más grande; mientras que zlib se diseñó para ser más eficiente en la comunicación entre
aplicaciones y con una comprobación de integridad más rápida que gzip.

Módulo zlib de Ruby

El módulo zlib (require “zlib”) de Ruby proporciona acceso tanto a la librería zlib y al formato zlib, como al 
formato gzip.

  Más información y ejemplos en:

    http://ruby-doc.org/stdlib-1.9.3/libdoc/zlib/rdoc/Zlib/GzipWriter.html
    http://ruby-doc.org/stdlib-1.9.3/libdoc/zlib/rdoc/Zlib/GzipReader.html
    http://www.ruby-doc.org/stdlib-2.0.0/libdoc/zlib/rdoc/Zlib.html

  Módulo zlib de Python

    https://docs.python.org/2/library/zlib.html
