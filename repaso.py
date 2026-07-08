intentos = 3
while intentos > 0:
    if input("Escriba la contraseña: ") == "hola":
        print("Correcto")
        break
    intentos = intentos - 1
    print("Contraseña incorrecta")
else:
    print("Se te han acabado los intentos")
        
 


