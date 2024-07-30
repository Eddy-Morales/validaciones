import random

detalleCompra =[[],[],[],[],[],[],[],[]]

def es_numero(val):
    return val.isdigit()

def validar_longitud_texto(texto, minimo, maximo):
    return minimo <= len(texto) <= maximo

def validar_alfabetico(texto):
    return texto.isalpha()

def menuOpciones():
    while True:
        try:
            print("¿Qué acción desea realizar?")
            print('*  1) Registrar pedidos')
            print('*  2) Mostrar pedidos')
            print('*  3) Mostrar detalle de un pedido')
            print('*  4) Salir del sistema')
            opcion = int(input("Ingrese la opción: "))
            if opcion in range(1, 5):
                return opcion
            else:
                print("Opción no válida. Por favor, elija una opción entre 1 y 4.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def ingresarPedido():
    print("\n\t\t Ingresar los datos del cliente \n")
    while True:
        nombre_cliente = input("Nombre: ")
        if validar_alfabetico(nombre_cliente) and validar_longitud_texto(nombre_cliente, 3, 10):
            break
        else:
            print("El nombre debe contener solo letras y tener entre 3 y 10 caracteres.")

    while True:
        apellido_cliente = input("Apellido: ")
        if validar_alfabetico(apellido_cliente) and validar_longitud_texto(apellido_cliente, 3, 10):
            break
        else:
            print("El apellido debe contener solo letras y tener entre 3 y 10 caracteres.")
    
    while True:
        telefono_cliente = input("Teléfono: ")
        if es_numero(telefono_cliente) and len(telefono_cliente) == 10:
            break
        else:
            print("El teléfono debe contener solo números y tener 10 dígitos.")

    print("\n\t\t Ingresar los datos de la policrush\n")
    while True:
        nombre_policrush = input("Nombre: ")
        if validar_alfabetico(nombre_policrush) and validar_longitud_texto(nombre_policrush, 3, 10):
            break
        else:
            print("El nombre debe contener solo letras y tener entre 3 y 10 caracteres.")
    
    while True:
        lugar_policrush = input("Dependencia: ")
        if validar_longitud_texto(lugar_policrush, 5, 15) and lugar_policrush.replace(" ", "").isalpha():
            break
        else:
            print("La dependencia debe tener entre 5 y 15 caracteres y no debe contener números.")
    
    while True:
        celular_policrush = input("Teléfono: ")
        if es_numero(celular_policrush) and len(celular_policrush) == 10:
            break
        else:
            print("El teléfono debe contener solo números y tener 10 dígitos.")

    detalleCompra[0].append(nombre_cliente)
    detalleCompra[1].append(apellido_cliente)
    detalleCompra[2].append(telefono_cliente)
    detalleCompra[3].append(nombre_policrush)
    detalleCompra[4].append(lugar_policrush)
    detalleCompra[5].append(celular_policrush)
    codigo_pedido = random.randrange(1000, 9999)
    detalleCompra[6].append(codigo_pedido)

    print("\n\t\t Selección del regalo \n")
    print("1) Opción 1: Poliflor + Polipeluche = $2.50")
    print("2) Opción 2: Poliflor + Policarta = $1.50")
    print("3) Opción 3: Poliflor + Polillavero = $2.00")
    print("4) Opción 4: Poliflor + Polivaso = $2.75")
    while True:
        try:
            opcion = int(input("Ingrese la opción: "))
            if opcion == 1:
                detalleCompra[7].append(2.50 + (0.1 * 2.50))
                break
            elif opcion == 2:
                detalleCompra[7].append(1.50 + (0.1 * 1.50))
                break
            elif opcion == 3:
                detalleCompra[7].append(2.00 + (0.1 * 2.00))
                break
            elif opcion == 4:
                detalleCompra[7].append(2.75 + (0.1 * 2.75))
                break
            else:
                print("Opción no válida. Por favor, elija una opción entre 1 y 4.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    print("\n-------- Pedido registrado con éxito --------\n")

def mostrarPedido(i):
    print("\t\n\n Datos del cliente")
    print("\t\t\t * Nombre:", detalleCompra[0][i])
    print("\t\t\t * Apellido:", detalleCompra[1][i])
    print("\t\t\t * Teléfono:", detalleCompra[2][i])
    print("\t\t\n Datos de la entrega")
    print("\t\t\t * Nombre:", detalleCompra[3][i])
    print("\t\t\t * Dependencia:", detalleCompra[4][i])
    print("\t\t\t * Teléfono:", detalleCompra[5][i])
    print("\t\t\n Datos del pago")
    print("\t\t\t * Código del pedido:", detalleCompra[6][i])      
    print("\t\t\t * Pago final: $", detalleCompra[7][i])

print("------------ MI POLICRUSH -------------")
print("\n\t\t *** Bienvenido(a) ***\n")
opcion = menuOpciones()
while opcion != 4:
    if opcion == 1:
        print("\n----- Nuevo pedido -----")
        ingresarPedido()
        opcion = menuOpciones()
    elif opcion == 2:
        if len(detalleCompra[0]) == 0:
            print("-------------------------------------\n")
            print("No existen pedidos registrados\n")
            print("-------------------------------------\n")
        else:
            print("\n------- Detalle de todos los pedidos ----------\n")
            for i in range(len(detalleCompra[0])):
                print("-------------------------------------")
                print("Detalle del pedido", i + 1)
                mostrarPedido(i)
                print("-------------------------------------")
        opcion = menuOpciones()
    elif opcion == 3:
        while True:
            codigo = input("\n Ingrese el código del pedido: ")
            if es_numero(codigo) and len(codigo) == 4:
                codigo = int(codigo)
                if codigo in detalleCompra[6]:
                    dato = detalleCompra[6].index(codigo)
                    print("\t\t\t\n Pedido encontrado")
                    print("-------------------------------------")
                    print("Detalle")
                    mostrarPedido(dato)
                    print("-------------------------------------")
                else:
                    print("No existe ese código de pedido registrado\n")
                break
            else:
                print("El código debe contener solo números y tener 4 dígitos.")
        opcion = menuOpciones()

print("Muchas gracias")
