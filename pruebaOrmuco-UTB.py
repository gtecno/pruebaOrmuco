#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb
def main():

 bd = MySQLdb.connect("127.0.0.1","root","root","test_python" )
 cursor = bd.cursor()

 print("===================================================\n")
 print("Bienvenido al sistema para la gestión de emociones ")
 print("===================================================\n")
 print("\n")
 print("Por favor, dinos tu nombre : ")
 nombre = raw_input()
 print("mucho gusto en conocerte %s \n" % nombre)
 print("¿podrias indicarme cual es tu color favorito ?")
 color = raw_input()
 print("me agrada el color %s \n " % color)
 print "Me guataría conocerte un poco más \n ahora necesito saber con cual de estas  mascotas \n simpatizas más, ¡debes escoger una!"
 print("======================================")
 print("		MASCOTAS                     ")
 print("======================================")
 print("		1.  PERRO  		     ")
 print("		2.  GATO		     ")
 print("	        3.  HAMSTER		     ")
 print("======================================")
 print ("Introduzca valor numerico para seleccionar la mascota de tu agardo (0 para salir)")
 valor = int(raw_input())	
 while valor != 0:
  if(valor == 1):
   mascota = "PERRO"
   print("")
   break
  elif(valor == 2):
   mascota = "GATO" 
   print("")
   break
  elif(valor == 3):
   mascota = "HAMSTER"
   print("")
   break
  else:
   print ("opcion incorrecta") 
 print("Introduzca valor numerico para seleccionar la mascota de tu agardo (0 para salir)")
 valor = int(raw_input())
 print("Gracias por su colaboración")
 print("Revise su registro por favor : \n") 
         
 # Insertar registro 
 sql = "INSERT INTO prueba_python VALUES (null,'%s','%s','%s')"  % (nombre, color, mascota) 
 # se persisten los cambios en la BD 
 cursor.execute(sql)
 # Efectuamos los cambios en la base de datos
 bd.commit()

 sql = "SELECT * FROM prueba_python"
 cursor.execute(sql)
 # Obtenemos todos los registros en una lista de listas
 resultados = cursor.fetchall()
 for registro in resultados:
     identificador = registro[0]
     nombre = registro[1]
     color = registro[2]
     mascota = registro[3]
 # Imprimimos los resultados obtenidos
 print "identificador=%d, nombre=%s, color=%s, mascota=%s" % (identificador, nombre, color, mascota)
  
 print('\n\n')
 print('=============================================================================================')
 print('      			TOTAL DE USUARIOS ENCUESTADOS           ')
 print('=============================================================================================')
 print("%-20s%-40s%-25s%-15s" % ('IDENTIFICADOR','NOMBRE','COLOR','MASCOTA'))
 print('=============================================================================================')
 sql = "SELECT * FROM prueba_python"
 cursor.execute(sql)
 listado = cursor.fetchall()
 for registro in listado:
  print("%-20d%-40s%-25s%-15s" %(registro[0],registro[1], registro[2],registro[3]))
 
 print('=============================================================================================') 
 #Desconectamos la base de datos MySQL 
 bd.close()
main()
 