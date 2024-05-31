
diccionario={}

try:
    while True: 
        print("Bienvenido al sistema de IA")
        print("1)insertar operaciónes")
        print("2)Eliminar")
        print("3) listar")
        print("4) Listar operaciónes")
        print("5) Salir")
        opciones=int(input("Ingrese su opción: "))
        if opciones < 1 and opciones > 5:
                    print('Opción inválida')
                  
     
        match opciones:
               
            case 1: 
                      insertar_op=int(input("INSERTAR VALORES: "))
                      for contador in range(insertar_op):
                            operacion=input(f"Ingrese la operación numero:  {contador+1}")
                            valor=input(f'ingrese el valor de la operacion número:  {contador+1}')
                            diccionario[operacion]= valor

            case 2: 
                        print("OPCIÓN DOS: ELIMINAR")
                        elim=input("ingrese la operación que desea eliminar: ")
                        diccionario.pop(elim)

            case 3:
                      print(diccionario)

            case 4: 
                        print("HA ENTRADO A LA OPCIÓN PROBAR")
                        llave=input("ingrese valor que desea probar: ")
                        print(diccionario[llave])
            case 5:
                        print ("Ha decidido salir del programa")
                      
except ValueError:
    print('Ha ocurrido un error de tipo de dato, se cerrará el programa.')




                   
                      
                              

                      

