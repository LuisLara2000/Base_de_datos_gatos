import os
import MySQLdb
 
from time import sleep
import mysql.connector
import keyboard
import time
from colorama import Back, Fore, init

init()
gatoLogo = """        
        ██▄            ▄██
       ▄██████████████████▄
      ▄████████████████████▄
     ▄██████████████████████▄
    ▄████████████████████████▄
   ▄████████  ███████  ███████▄
  ▄██████████████▀█████████████▄
  ██████████▀███▀ ▀███▀█████████
  ███████████▄▄▄███▄▄▄██████████
  ██████████████████████████████
  ░░░░░░ MICHI ESTADISTICAS ░░░░
  ██████████████████████████████
  ██████████████████████████████    ▄██▄
  ██████████████████████████████    ████
  ██████████████████████████████    ████
  ██████████████████████████████   ▄████
  ██████████████████████████████ ██████
  █████████████████████████████████████
  ████████████████████████████████████
  ████ ██████        ██████ █████
  ████  ████          ████  ████
  ████  ████          ████  ████
  ████  ████          ████  ████
  ▀██▀  ▀██▀          ▀██▀  ▀██▀"""
def imprimirNumeroChidos(numero):
    cero = ["██████ ", "██  ██ ", "██  ██ ", "██  ██ ", "██████ "]
    uno = ["████   ", "  ██   ", "  ██   ", "  ██   ", "██████ "]
    dos = ["██████ ", "    ██ ", "██████ ", "██     ", "██████ "]
    tres = ["██████ ", "    ██ ", "██████ ", "    ██ ", "██████ "]
    cuatro = ["██  ██ ", "██  ██ ", "██████ ", "    ██ ", "    ██ "]
    cinco = ["██████ ", "██     ", "██████ ", "    ██ ", "██████ "]
    seis = ["██████ ", "██     ", "██████ ", "██  ██ ", "██████ "]
    siete = ["██████ ", "    ██ ", "    ██ ", "    ██ ", "    ██ "]
    ocho = ["██████ ", "██  ██ ", "██████ ", "██  ██ ", "██████ "]
    nueve = ["██████ ", "██  ██ ", "██████ ", "    ██ ", "    ██ "]
    renglon = ""
    for x in range(5):
        for i in range(len(numero)):
            if int(numero[i]) == 1:
                renglon += uno[x]
            if int(numero[i]) == 2:
                renglon += dos[x]
            if int(numero[i]) == 3:
                renglon += tres[x]
            if int(numero[i]) == 4:
                renglon += cuatro[x]
            if int(numero[i]) == 5:
                renglon += cinco[x]
            if int(numero[i]) == 6:
                renglon += seis[x]
            if int(numero[i]) == 7:
                renglon += siete[x]
            if int(numero[i]) == 8:
                renglon += ocho[x]
            if int(numero[i]) == 9:
                renglon += nueve[x]
            if int(numero[i]) == 0:
                renglon += cero[x]
        print(renglon.center(50, " "))
        renglon = ""
def imprimirGato():
    print(gatoLogo)
def crearTablas():
    # se conecta a la base de datos y cambiamos de cursor
    baseDatos = MySQLdb.connect(host="localhost", user="root",password="megaROOTman21", database="bd_michiestadisticas")
    cursor = baseDatos.cursor()
    # TABLA USUARIO
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS usuarios(IdUsuario TINYINT(255) UNSIGNED NOT NULL AUTO_INCREMENT, NombreUsuario CHAR(255),AliasUsuario CHAR(255),AliasOReal CHAR(1),Conocido CHAR(2),PRIMARY KEY (idUsuario))")
    # TABLA GATOS
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS gatos(IdGato SMALLINT(255) UNSIGNED,NombreGato TEXT,NombreGatuno CHAR(2),NombreHaSidoRepetido CHAR(2),LongitudNombre SMALLINT(255) UNSIGNED,ColorCuerpo CHAR(25), ConAccesorio CHAR(15),ColorAccesorio CHAR(25), GatoVanilla CHAR(2),llegada CHAR(10),PRIMARY KEY (IdGato))")
    # TABLA USUARIOS / GATOS
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS usuariosGatos(IdUsuario TINYINT(255) UNSIGNED,IdGato SMALLINT(255) UNSIGNED)")
    # TABLA USUARIOS / NOMBRES REPETIDOS
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS usuariosNombresrepetidos(IdUsuario TINYINT(255) UNSIGNED,NombreRepetido TEXT)")
    # TABLA USUARIOS / IMAGENES
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS usuariosImagenes(IdUsuario TINYINT(255) UNSIGNED,ImagenUsuario CHAR(100))")
    # TABLA GATOS / IMAGENES
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS gatosImagenes(IdGato SMALLINT(255) UNSIGNED,ImagenGato CHAR(100))")
def insertarNuevoUsuario():
    valores = []
    print("##### DAR DE ALTA UN NUEVO USUARIO #####")
    print("")
    valores.append(str(input("INGRESE EL NOMBRE -> ")))
    valores.append(input("INGRESE EL ALIAS -> "))
    valores.append(input("MODO PUBLICO ¿ALIAS O REAL? -> "))
    valores.append(input("¿LO CONOZCO? -> "))
    # se conecta a la base de datos y cambiamos de cursor
    baseDatos = MySQLdb.connect(host="localhost", user="root",password="megaROOTman21", database="bd_michiestadisticas")
    cursor = baseDatos.cursor()
    # ingresamos los datos 
    sentencia = str("INSERT INTO usuarios (NombreUsuario,AliasUsuario,AliasOReal,Conocido) VALUES (%s,%s,%s,%s)")
    valores = (valores[0], valores[1], valores[2], valores[3])
    cursor.execute(sentencia, valores)
    baseDatos.commit()
def insertarNuevoGato():
    valores = []
    valores.append(input("INGRESE EL ID -> "))
    valores.append(input("INGRESE EL NOMBRE -> "))
    valores.append(input("¿NOMBRE GATUNO? -> "))
    valores.append(input("¿EL NOMBRE HA SIDO REPETIDO? -> "))
    valores.append(input("LONGITUD DEL NOMBRE -> "))
    valores.append(input("COLOR DEL CUERPO -> "))
    valores.append(input("COLOR DEL COLLAR -> "))
    valores.append(input("¿VANILLA? -> "))
    # se conecta a la base de datos y cambiamos de cursor
    baseDatos = MySQLdb.connect(host="localhost", user="root",
                                password="megaROOTman21", database="bd_michiestadisticas")
    cursor = baseDatos.cursor()
    # ingresamos los datos
    sentencia = str(
        "INSERT INTO gatos (IdGato,NombreGato,NombreGatuno,NombreHaSidoRepetido,LongitudNombre,ColorCuerpo,ColorCollar,GatoVanilla) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
    valores = (valores[0], valores[1], valores[2], valores[3],
               valores[4], valores[5], valores[6], valores[7],)
    cursor.execute(sentencia, valores)
    baseDatos.commit()    
def insertarUsuarioImagen():
    valores = []
    valores.append(input("INGRESE EL ID DEL USUARIO -> "))
    valores.append(str(str("U")+str(valores[0])+str("IMG")))
    # se conecta a la base de datos y cambiamos de cursor
    baseDatos = MySQLdb.connect(host="localhost", user="root",
                                password="megaROOTman21", database="bd_michiestadisticas")
    cursor = baseDatos.cursor()
    # ingresamos los datos
    sentencia = str(
        "INSERT INTO usuariosImagenes(IdUsuario,ImagenUsuario) VALUES (%s,%s)")
    valores = (valores[0], valores[1])
    cursor.execute(sentencia, valores)
    baseDatos.commit()
def insertarUsuarioGato():
    valores = []
    valores.append(input("INGRESE EL ID DEL USUARIO -> "))
    valores.append(input("INGRESE EL ID DEL GATO -> "))
    # se conecta a la base de datos y cambiamos de cursor
    baseDatos = MySQLdb.connect(host="localhost", user="root",
                                password="megaROOTman21", database="bd_michiestadisticas")
    cursor = baseDatos.cursor()
    # ingresamos los datos
    sentencia = str(
        "INSERT INTO usuariosGatos(IdUsuario,IdGato) VALUES (%s,%s)")
    valores = (valores[0], valores[1])
    cursor.execute(sentencia, valores)
    baseDatos.commit()
def llegadaDeUnGato():
    valores = []
    valores.append(input("INGRESE EL ID -> "))
    # validamos que el gato no exista
    # se conecta a la base de datos y cambiamos de cursor
    baseDatos = MySQLdb.connect(host="localhost", user="root",password="megaROOTman21", database="bd_michiestadisticas")
    cursor = baseDatos.cursor()
    sentencia = "SELECT IdGato From gatos WHERE IdGato = "+str(valores[0])
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    print(resultado)
    os.system("cls")
    if str(resultado) == "()":
        print("INGRESE LOS DATOS DEL NUEVO GATO #"+str(valores[0]))
        valores.append(input("COLOR DEL CUERPO -> "))
        valores.append(input("¿ACCESORIO? -> "))
        valores.append(input("COLOR ACCESORIO -> "))
        valores.append(input("¿VANILLA? -> "))
        valores.append(input("FECHA DE LLEGADA -> "))
        # se conecta a la base de datos y cambiamos de cursor
        baseDatos = MySQLdb.connect(host="localhost", user="root",password="megaROOTman21", database="bd_michiestadisticas")
        cursor = baseDatos.cursor()
        # ingresamos los datos
        sentencia = str("INSERT INTO gatos(IdGato,ColorCuerpo,ConAccesorio,ColorAccesorio,GatoVanilla,llegada) VALUES (%s,%s,%s,%s,%s,%s)")
        valores = (valores[0], valores[1], valores[2], valores[3],valores[4],valores[5])
        cursor.execute(sentencia, valores)
        baseDatos.commit()
    else:
        sentencia = "SELECT IdGato,llegada From gatos WHERE IdGato = "+str(valores[0])
        cursor.execute(sentencia)
        resultado = cursor.fetchall()
        print("GATO YA EXISTENTE")
        print("IdGATO: ",end="")
        print(resultado[0][0], end="")
        print(" FECHA: ", end="")
        print(resultado[0][1], end="")
    print("")
    input("PRESIONE CUALQUIER TECLA PARA CONTINUAR")
def bautizar():
    valores = []
    valorIdUsuario = -1
    nombreUsuario = ""
    GatoId = 0
    ValorNombre = False
    nombreGato = ""
    Valorgato = -1
    repetido = "No"
    # se conecta a la base de datos y cambiamos de cursor
    baseDatos = MySQLdb.connect(host="localhost", user="root",password="megaROOTman21", database="bd_michiestadisticas")
    cursor = baseDatos.cursor()
    while valorIdUsuario == -1:
        # Validamos que el usuario exista
        os.system("cls")
        nombreUsuario = str(input("NOMBRE DEL BAUTIZADOR -> "))

        # Busco en la tabla usuarios
        sentencia = str("SELECT IdUsuario FROM usuarios WHERE NombreUsuario = '"+str(nombreUsuario)+"'")
        cursor.execute(sentencia)
        resultado = cursor.fetchall() # se obtiene el id del usuario
        baseDatos.commit()

        for i in resultado:
            valorIdUsuario = i[0]

        if valorIdUsuario == -1:
            os.system("cls")
            print("El usuario no existe, intente nuevamente")
            sleep(3)

    # debe ser un valor booleano
    while Valorgato == -1:
        GatoId = str(input("INGRESE EL ID DEL GATO ->"))
        # Busco en la tabla gatos
        sentencia = str("SELECT IdGato FROM gatos WHERE IdGato = '"+str(GatoId)+"'")
        cursor.execute(sentencia)
        resultado = cursor.fetchall()  # se obtiene el id del usuario
        baseDatos.commit()

        Valorgato = resultado[0][0]

        if Valorgato == -1:
            os.system("cls")
            print("El gato ya a sido nombrado o el gato no existe") 
            sleep(3)
            print("NOMBRE DEL BAUTIZADOR -> ",end="")
            print(nombreUsuario)

    valores.append(str(input("NOMBRE DEL GATO ->")))
    
    # validar que el nombre sea unico
    sentencia = str("SELECT IdGato FROM gatos WHERE NombreGato = '"+str(valores[0])+"'")
    cursor.execute(sentencia)
    resultado = cursor.fetchall()

    if len(resultado) > 0:
        sentencia = "INSERT into usuariosnombresrepetidos (IdUsuario,NombreRepetido) values ('"+str(valorIdUsuario)+"','"+str(valores[0])+"')"
        cursor.execute(sentencia)
        baseDatos.commit()
        repetido = "Si"
    valores.append(str(input("¿NOMBRE GATUNO? ->")))
    valores.append(str(repetido))
    print("¿HA SIDO REPETIDO? ->"+str(repetido))
    valores.append(str(len(valores[0])))
    print("¿LONGITUD NOMBRE? ->"+str(len(valores[0])))
    print("")
    print("PRESIONE ENTER PARA CONTINUAR")
    
    # INSERTAMOS LOS VALORES 
    sentencia = str("UPDATE gatos SET NombreGato='"+str(valores[0])+"', NombreGatuno='"+str(valores[1])+"', NombreHaSidoRepetido='"+str(valores[2])+"', LongitudNombre='"+str(valores[3])+"' WHERE IdGato = '"+str(Valorgato)+"'")
    #valor = (valores[0], valores[1], valores[2], valores[3])
    cursor.execute(sentencia)
    baseDatos.commit()
    sentencia = str("INSERT INTO usuariosGatos(IdUsuario,IdGato) VALUES (%s,%s)")
    valor2 = (str(valorIdUsuario),str(Valorgato))
    cursor.execute(sentencia,valor2)
    baseDatos.commit()
    input()
def GatosConSinNombre():
    renglon = ""
    numeroGato = ""
    # se conecta a la base de datos y cambiamos de cursor
    baseDatos = MySQLdb.connect(host="localhost", user="root",password="megaROOTman21", database="bd_michiestadisticas")
    cursor = baseDatos.cursor()   
    sentencia = "SELECT count(*) FROM bd_michiestadisticas.gatos where NombreGato is NULL"
    cursor.execute(sentencia)
    resultadoNoNombrados = cursor.fetchall()
    sentencia = "SELECT count(*) FROM bd_michiestadisticas.gatos where NombreGato is not NULL"
    cursor.execute(sentencia)
    resultadoNombrados = cursor.fetchall()
    sentencia = "SELECT count(*) FROM bd_michiestadisticas.gatos"
    cursor.execute(sentencia)
    resultadoCantidadGatos = cursor.fetchall()
    print(Back.BLUE + "  CANTIDAD DE GATOS  ".center(50, " ")+Back.RESET)
    print("")
    imprimirNumeroChidos(str(resultadoCantidadGatos[0][0]))
    print("")
    print(Back.BLUE + "  GATOS  NO       GATOS  SI".center(50, " ")+Back.RESET)
    print(Back.BLUE + "  NOMBRADOS       NOMBRADOS".center(50, " ")+Back.RESET)
    print(str("   "+str(resultadoNoNombrados[0][0])+"              "+str(resultadoNombrados[0][0])).center(50, " "))
    print("")
    sentencia = "SELECT IdGato FROM bd_michiestadisticas.gatos where NombreGato is NULL"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    print(Back.BLUE + "LISTA DE GATOS SIN NOMBRE".center(50, " ")+Back.RESET)
    for i in range(1,len(resultado)):
        numeroGato = str(resultado[i][0]).center(10, " ")
        renglon += numeroGato
        if i % 5 == 0:
            print(renglon)
            renglon = ""
        numeroGato = ""
    renglon += str(resultado[0][0]).center(10, " ")
    print(renglon)
        #print("              "+str(resultado[i][0]).rjust(4, ' '))
    print("")
    #.center(50, "=")
    input("PRESIONE CUALQUIER TECLA PARA CONTINUAR")
def verUsuariosYGatos():
    # se conecta a la base de datos y cambiamos de cursor
    baseDatos = MySQLdb.connect(host="localhost", user="root",password="megaROOTman21", database="bd_michiestadisticas")
    cursor = baseDatos.cursor()  
    sentencia = "SELECT IdUsuario,NombreUsuario FROM bd_michiestadisticas.usuarios order by IdUsuario"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    for i in range(len(resultado)):
        print(Back.MAGENTA +" #"+str(resultado[i][0]).rjust(2, '0'),end=" ")
        print(Back.BLUE +" "+str(resultado[i][1]).rjust(25, ' '),end=" ")
        print(Back.RESET+" ")
        # buscamos los gatos de cada usuario
        sentencia = "SELECT IdGato FROM bd_michiestadisticas.usuariosgatos where IdUsuario ="+str(resultado[i][0])
        cursor.execute(sentencia)
        resultadoGatos = cursor.fetchall()
        for x in range(len(resultadoGatos)):
            sentencia = "select NombreGato from bd_michiestadisticas.gatos where IdGato ="+str(resultadoGatos[x][0])
            cursor.execute(sentencia)
            resultadoNombres = cursor.fetchall()
            print(Back.RESET+str(resultadoNombres[0][0]).center(32," "))
    print("")
    input("PRESIONE CUALQUIER TECLA PARA CONTINUAR")
def principal():
    Respuesta = -1
    while Respuesta != 0:
        # MENU
        os.system("cls")   
        imprimirGato()
        print(" ")
        print("  1 -> DarDeAltaNuevoUsuario")
        print("  2 -> RegistarLlegadaDeNuevoGato")
        print("  3 -> BautizarUnGato")
        print("  4 -> GatosSinNombre")
        print("  5 -> NombresBautizadores")
        print("  0 -> Salir")
        #print(" ")
        Respuesta = int(input("  Respuesta -> "))
        if Respuesta == 1:
            os.system("cls")
            insertarNuevoUsuario()
        elif Respuesta == 2:
            os.system("cls")
            llegadaDeUnGato()
        elif Respuesta == 3:
            os.system("cls")
            bautizar()
        elif Respuesta == 4:
            os.system("cls")
            GatosConSinNombre()
        elif Respuesta == 5:
            os.system("cls")
            verUsuariosYGatos()
principal()  
"""     ██▄        ▄██
       ▄██████████████▄
      ▄████████████████▄
     ▄██████████████████▄
    ▄████████████████████▄
   ▄██████  ███████  █████▄
  ▄████████████▀███████████▄
  ████████▀███▀ ▀███▀███████
  █████████▄▄▄███▄▄▄████████
  ██████████████████████████
  ░░░░░░░░░░░░░░░░░░░░░░░░░░
  ██████████████████████████
  ██████████████████████████    ▄██▄
  ██████████████████████████    ████
  ██████████████████████████    ████
  ██████████████████████████   ▄████
  ███████████████████████████ ██████
  █████████████████████████████████
  ████████████████████████████████
  ████ ██████    ██████ █████
  ████  ████      ████  ████
  ████  ████      ████  ████
  ████  ████      ████  ████
  ▀██▀  ▀██▀      ▀██▀  ▀██▀"""
